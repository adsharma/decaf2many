"""Console script for decaf2many."""
import argparse
import logging

from antlr4 import CommonTokenStream, FileStream
from antlr4.tree.Trees import Trees
from pathlib import Path

from .decaf2many import Transpiler
from .lang.JavaLexer import JavaLexer
from .lang.JavaParser import JavaParser

logger = logging.getLogger("decaf2many")


def run_one(args, file_name):
    lexer = JavaLexer(FileStream(file_name))
    stream = CommonTokenStream(lexer)
    parser = JavaParser(stream)
    tree = parser.compilationUnit()
    if args.dump:
        print(Trees.toStringTree(tree, None, parser))
        return
    tx = Transpiler()
    out = tx.visit(tree)
    file_path = Path(file_name)
    if args.outdir:
        out_dir = Path(args.outdir)
        out_dir.mkdir(parents=True, exist_ok=True)
    else:
        out_dir = Path(".")
    out_path = out_dir / Path(file_path.stem + ".py")
    with open(out_path, "w") as f:
        f.write(out)
    logger.info(f"wrote output to: {out_path}")
    return


def main(args=None):
    """Console script for decaf2many."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dump",
        default=False,
        action="store_true",
        help="dump ast instead of transpiling",
    )
    parser.add_argument("--outdir", default=None, help="Output directory")
    parser.add_argument("-l", "--log-level", default="INFO", help="set log level")

    args, rest = parser.parse_known_args(args=args)

    try:
        logging.basicConfig(level=args.log_level)
        console = logging.StreamHandler()
        console.setLevel(logging.root.level)
        formatter = logging.Formatter("%(name)-12s: %(levelname)-8s %(message)s")
        console.setFormatter(formatter)
        logger.addHandler(console)
    except ValueError:
        logging.error(f"Invalid log level: {args.log_level}")
        sys.exit(1)

    return run_one(args, rest[0])
