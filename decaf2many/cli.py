"""Console script for decaf2many."""
import argparse
import sys

from antlr4 import CommonTokenStream, FileStream

from .decaf2many import Transpiler
from .lang.JavaLexer import JavaLexer
from .lang.JavaParser import JavaParser


def run_one(filename):
    lexer = JavaLexer(FileStream(filename))
    stream = CommonTokenStream(lexer)
    parser = JavaParser(stream)
    tree = parser.compilationUnit()
    tx = Transpiler()
    tx.visit(tree)


def main():
    """Console script for decaf2many."""
    parser = argparse.ArgumentParser()
    args, rest = parser.parse_known_args()

    return run_one(rest[0])


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
