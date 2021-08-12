import argparse
import filecmp
import logging
import os.path
import unittest
import subprocess
import sys

from distutils import spawn
from functools import lru_cache
from pathlib import Path
from subprocess import run
from unittest_expander import foreach, expand

from decaf2many.cli import main

TESTS_DIR = Path(__file__).parent.absolute()
ROOT_DIR = TESTS_DIR.parent
BUILD_DIR = TESTS_DIR / "build"
GENERATED_DIR = BUILD_DIR
FORMATTER = "black"

KEEP_GENERATED = os.environ.get("KEEP_GENERATED", False)
SHOW_ERRORS = os.environ.get("SHOW_ERRORS", False)
UPDATE_EXPECTED = os.environ.get("UPDATE_EXPECTED", False)


TEST_CASES = [item.name for item in (TESTS_DIR / "cases").glob("*.java")]

logger = logging.Logger("test_cli")


@expand
class CodeGeneratorTests(unittest.TestCase):
    maxDiff = None

    SHOW_ERRORS = SHOW_ERRORS
    KEEP_GENERATED = KEEP_GENERATED
    UPDATE_EXPECTED = UPDATE_EXPECTED

    def setUp(self):
        os.makedirs(BUILD_DIR, exist_ok=True)
        os.chdir(BUILD_DIR)

    @staticmethod
    def format_code(filename):
        return subprocess.run([FORMATTER, filename]).returncode

    @foreach(sorted(TEST_CASES))
    def test_generated(self, case):
        out_file = Path(case).stem + ".py"
        expected_filename = TESTS_DIR / "expected" / f"{out_file}"

        if (
            not self.UPDATE_EXPECTED
            and not self.KEEP_GENERATED
            and not os.path.exists(expected_filename)
        ):
            raise unittest.SkipTest(f"{expected_filename} not found")

        case_filename = TESTS_DIR / "cases" / f"{case}"
        case_output = GENERATED_DIR / f"{out_file}"

        args = ["--outdir", str(GENERATED_DIR), str(case_filename)]

        try:
            rv = main(args)
            format_rv = self.format_code(case_output)
            if format_rv != 0:
                raise unittest.SkipTest(f"{FORMATTER} not available")
            with open(case_output) as actual:
                generated = actual.read()
                if os.path.exists(expected_filename) and not self.UPDATE_EXPECTED:
                    with open(expected_filename) as f2:
                        expected_case_contents = f2.read()
                        self.assertEqual(expected_case_contents, generated)

            if self.UPDATE_EXPECTED or not os.path.exists(expected_filename):
                with open(expected_filename, "w") as f:
                    f.write(generated)

        finally:
            if not self.KEEP_GENERATED:
                case_output.unlink(missing_ok=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--keep-generated",
        type=bool,
        default=False,
        help="Keep generated code for debug",
    )
    parser.add_argument(
        "--update-expected", type=bool, default=False, help="Update tests/expected"
    )
    args, rest = parser.parse_known_args()

    CodeGeneratorTests.KEEP_GENERATED |= args.keep_generated
    CodeGeneratorTests.UPDATE_EXPECTED |= args.update_expected

    rest = [sys.argv[0]] + rest
    unittest.main(argv=rest)
