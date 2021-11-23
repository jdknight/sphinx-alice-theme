# -*- coding: utf-8 -*-
# Copyright 2020-2021 James Knight

from . import __version__
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(prog='sphinx-alice-theme',
        description='Alice Theme for Sphinx')
    parser.add_argument(
        '--version', action='version', version='%(prog)s ' + __version__)

    parser.parse_args()
    parser.print_help()
    return 0


if __name__ == '__main__':
    sys.exit(main())
