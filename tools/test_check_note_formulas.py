#!/usr/bin/env python3
"""Regression tests for block math inside endnote definitions."""

from __future__ import annotations

import collections
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import check_math  # noqa: E402
import check_structure  # noqa: E402

REPO = pathlib.Path(__file__).resolve().parent.parent


class NoteFormulaTests(unittest.TestCase):
    def test_indented_display_math_is_counted_only_for_endnotes(self) -> None:
        note = """[^ch06n1]: Intro with inline $x=1$.

    ::: {.displayeq}

    $$y=2$$

    :::

    Continuation with $z=3$.
"""

        self.assertEqual(check_math.formulas(note), ["x=1", "z=3"])
        self.assertEqual(
            check_math.formulas(note, include_indented_display=True),
            ["y=2", "x=1", "z=3"],
        )
        self.assertEqual(check_structure.metrics(note)["公式"], 2)
        self.assertEqual(
            check_structure.metrics(note, include_indented_display=True)["公式"],
            3,
        )

    def test_all_translated_endnote_formulas_match_source(self) -> None:
        en_text = (REPO / "en" / "25_Notes.md").read_text(encoding="utf-8")
        cn_text = (REPO / "cn-book" / "21.注释.md").read_text(encoding="utf-8")

        en_formulas = check_math.formulas(en_text)
        cn_formulas = check_math.formulas(
            cn_text, include_indented_display=True
        )

        self.assertEqual(len(en_formulas), 74)
        self.assertEqual(len(cn_formulas), 74)
        self.assertEqual(collections.Counter(en_formulas), collections.Counter(cn_formulas))
        self.assertEqual(check_structure.metrics(en_text)["公式"], 74)
        self.assertEqual(
            check_structure.metrics(cn_text, include_indented_display=True)["公式"],
            74,
        )


if __name__ == "__main__":
    unittest.main()
