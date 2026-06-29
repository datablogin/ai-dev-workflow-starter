"""Phase 2 (tdd): failing tests for the Break 100 gap calculation.

Run: python3 -m unittest discover -s tests -v
These are written BEFORE break100.py exists and should fail until Phase 3.

Gap convention under test: gap = target_sg - you_sg, so a POSITIVE gap means
strokes the user could save by reaching that target tier.
"""

import csv
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import break100  # noqa: E402  (import-after-path-setup is intentional)


REAL_CSV = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "benchmarks.csv",
)


def write_csv(text):
    """Write text to a temp CSV and return its path."""
    fd, path = tempfile.mkstemp(suffix=".csv")
    with os.fdopen(fd, "w") as f:
        f.write(text)
    return path


VALID = (
    "category,you_25,target_20,target_15,source\n"
    "off_the_tee,-4.2,-3.4,-2.7,src\n"
    "approach,-9.0,-7.5,-6.0,src\n"
    "short_game,-3.0,-2.5,-2.0,src\n"
    "putting,-2.2,-1.8,-1.5,src\n"
)


class LoadBenchmarksTests(unittest.TestCase):
    def test_loads_four_categories_with_numeric_values(self):
        path = write_csv(VALID)
        self.addCleanup(os.remove, path)
        rows = break100.load_benchmarks(path)
        self.assertEqual(len(rows), 4)
        cats = {r["category"] for r in rows}
        self.assertEqual(cats, set(break100.CATEGORIES))
        row = next(r for r in rows if r["category"] == "approach")
        self.assertAlmostEqual(row["you_25"], -9.0)
        self.assertIsInstance(row["you_25"], float)

    def test_real_data_file_loads(self):
        rows = break100.load_benchmarks(REAL_CSV)
        self.assertEqual({r["category"] for r in rows}, set(break100.CATEGORIES))

    def test_missing_required_column_raises(self):
        path = write_csv("category,you_25,target_20,source\noff_the_tee,-4.2,-3.4,src\n")
        self.addCleanup(os.remove, path)
        with self.assertRaises(ValueError):
            break100.load_benchmarks(path)

    def test_non_numeric_value_raises(self):
        path = write_csv(VALID.replace("-9.0", "oops"))
        self.addCleanup(os.remove, path)
        with self.assertRaises(ValueError):
            break100.load_benchmarks(path)

    def test_missing_category_raises(self):
        # only three categories present
        path = write_csv(
            "category,you_25,target_20,target_15,source\n"
            "off_the_tee,-4.2,-3.4,-2.7,src\n"
            "approach,-9.0,-7.5,-6.0,src\n"
            "putting,-2.2,-1.8,-1.5,src\n"
        )
        self.addCleanup(os.remove, path)
        with self.assertRaises(ValueError):
            break100.load_benchmarks(path)


class GapMathTests(unittest.TestCase):
    def setUp(self):
        path = write_csv(VALID)
        self.addCleanup(os.remove, path)
        self.rows = break100.load_benchmarks(path)

    def test_gap_direction_positive_is_saveable(self):
        # target is less negative than you, so saveable strokes are positive
        self.assertAlmostEqual(break100.gap(you_sg=-4.2, target_sg=-3.4), 0.8)
        # if you were already better than target, gap is negative
        self.assertAlmostEqual(break100.gap(you_sg=-2.0, target_sg=-3.0), -1.0)

    def test_gaps_for_break_100_tier(self):
        g = break100.gaps_for_tier(self.rows, "target_20")
        self.assertAlmostEqual(g["off_the_tee"], 0.8)
        self.assertAlmostEqual(g["approach"], 1.5)
        self.assertAlmostEqual(g["short_game"], 0.5)
        self.assertAlmostEqual(g["putting"], 0.4)

    def test_gaps_for_stretch_tier(self):
        g = break100.gaps_for_tier(self.rows, "target_15")
        self.assertAlmostEqual(g["off_the_tee"], 1.5)
        self.assertAlmostEqual(g["approach"], 3.0)
        self.assertAlmostEqual(g["short_game"], 1.0)
        self.assertAlmostEqual(g["putting"], 0.7)

    def test_biggest_gap_is_approach_for_both_tiers(self):
        self.assertEqual(break100.biggest_gap(self.rows, "target_20")[0], "approach")
        self.assertEqual(break100.biggest_gap(self.rows, "target_15")[0], "approach")

    def test_total_gap_sums_categories(self):
        self.assertAlmostEqual(break100.total_gap(self.rows, "target_20"), 3.2)
        self.assertAlmostEqual(break100.total_gap(self.rows, "target_15"), 6.2)


class RenderTests(unittest.TestCase):
    def test_render_mentions_both_targets_and_headline_category(self):
        rows = break100.load_benchmarks(REAL_CSV)
        out = break100.render(rows)
        self.assertIn("approach", out.lower())
        # both tiers represented somewhere in the output
        self.assertIn("20", out)
        self.assertIn("15", out)


if __name__ == "__main__":
    unittest.main()
