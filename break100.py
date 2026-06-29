"""Break 100: strokes-gained gap diagnosis for an amateur golfer.

Reads published strokes-gained-by-handicap benchmarks (vs the PGA Tour
baseline) and reports, per game category, how many strokes the user could
save by reaching each target tier. The largest gap is the highest-leverage
place to practice.

Descriptive, not causal: the benchmarks are population averages by handicap,
not a measurement of the user's own game. See data/SOURCES.md.

Usage:
    python3 break100.py [data/benchmarks.csv]
"""

import csv
import sys

CATEGORIES = ("off_the_tee", "approach", "short_game", "putting")

# CSV columns holding strokes-gained-vs-tour values (negative numbers).
VALUE_COLUMNS = ("you_25", "target_20", "target_15")
REQUIRED_COLUMNS = ("category",) + VALUE_COLUMNS + ("source",)

# Human-readable labels for output.
CATEGORY_LABELS = {
    "off_the_tee": "Off the tee",
    "approach": "Approach",
    "short_game": "Short game",
    "putting": "Putting",
}
TARGETS = (
    ("target_20", "20-handicap (just break 100)"),
    ("target_15", "15-handicap (stretch)"),
)


def load_benchmarks(path):
    """Load and validate the benchmark CSV.

    Returns a list of dicts with float value columns. Raises ValueError if a
    required column is missing, a value is non-numeric, or the four expected
    categories are not present exactly once each.
    """
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames or []
        missing = [c for c in REQUIRED_COLUMNS if c not in header]
        if missing:
            raise ValueError(
                "benchmark file missing required column(s): " + ", ".join(missing)
            )

        rows = []
        for line_no, raw in enumerate(reader, start=2):
            row = {"category": (raw["category"] or "").strip(), "source": raw["source"]}
            for col in VALUE_COLUMNS:
                value = (raw[col] or "").strip()
                try:
                    row[col] = float(value)
                except ValueError:
                    raise ValueError(
                        "non-numeric value %r in column %r (line %d)"
                        % (value, col, line_no)
                    )
            rows.append(row)

    found = [r["category"] for r in rows]
    if sorted(found) != sorted(CATEGORIES):
        raise ValueError(
            "expected exactly these categories %s, got %s"
            % (sorted(CATEGORIES), sorted(found))
        )
    return rows


def gap(you_sg, target_sg):
    """Strokes saveable by reaching the target.

    Both inputs are strokes-gained vs tour (negative). The target is less
    negative, so target - you is positive == strokes the user could save.
    """
    return target_sg - you_sg


def gaps_for_tier(rows, target_key):
    """Map each category to its gap for the given target column."""
    return {r["category"]: gap(r["you_25"], r[target_key]) for r in rows}


def biggest_gap(rows, target_key):
    """Return (category, gap) for the largest gap in the given tier."""
    gaps = gaps_for_tier(rows, target_key)
    category = max(gaps, key=gaps.get)
    return category, gaps[category]


def total_gap(rows, target_key):
    """Total strokes saveable across all categories for the given tier."""
    return sum(gaps_for_tier(rows, target_key).values())


def render(rows):
    """Render a plain-text report of the gaps for both target tiers."""
    lines = ["Break 100 - strokes-gained gap diagnosis", ""]
    for target_key, label in TARGETS:
        gaps = gaps_for_tier(rows, target_key)
        top_cat, _ = biggest_gap(rows, target_key)
        lines.append("Target: %s" % label)
        lines.append("  %-12s %s" % ("category", "strokes saveable"))
        # Show categories largest-gap first.
        for cat in sorted(gaps, key=gaps.get, reverse=True):
            marker = "  <- highest leverage" if cat == top_cat else ""
            lines.append("  %-12s %+5.1f%s" % (CATEGORY_LABELS[cat], gaps[cat], marker))
        lines.append("  %-12s %+5.1f" % ("TOTAL", total_gap(rows, target_key)))
        lines.append("")
    lines.append(
        "Descriptive, not causal: benchmarks are population averages by "
        "handicap, not your own game. See data/SOURCES.md."
    )
    return "\n".join(lines)


def main(argv):
    path = argv[1] if len(argv) > 1 else "data/benchmarks.csv"
    rows = load_benchmarks(path)
    print(render(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
