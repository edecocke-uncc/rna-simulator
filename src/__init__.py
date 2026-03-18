#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Erin Nicole Decocker
# edecocke@charlotte.edu
# ID: 801442694

"""
rna-simulator: Generate synthetic RNA sequences.

A Python package for creating synthetic RNA sequences with configurable
characteristics for bioinformatics research.
"""

__version__ = "1.0.0"
__author__ = "Nicole_Decocker"


import sys
import argparse

from .simulator import Simulator


def create_parser() -> argparse.ArgumentParser:
    """
    Create and configure argument parser.

    Returns:
        argparse.ArgumentParser: Configured parser
    """
    parser = argparse.ArgumentParser(description="RNA Sequence Simulator")

    parser.add_argument("-n", "--num-sequences", type=int, default=10)
    parser.add_argument("-o", "--output", type=str, default="sequences.fasta")
    parser.add_argument("--min-length", type=int, default=100)
    parser.add_argument("--max-length", type=int, default=1000)
    parser.add_argument("--flanking-prob", type=float, default=0.5)
    parser.add_argument("--flanking-length", type=int, default=50)
    parser.add_argument("--completeness", type=float, default=0.7)

    return parser


def validate_arguments(args: argparse.Namespace) -> None:
    """
    Validate parsed arguments.

    Args:
        args: Parsed arguments

    Raises:
        ValueError: If arguments are invalid
    """
    if args.num_sequences <= 0:
        raise ValueError("num-sequences must be positive")

    if args.min_length <= 0:
        raise ValueError("min-length must be positive")

    if args.max_length < args.min_length:
        raise ValueError("max-length must be >= min-length")

    if not (0 <= args.flanking_prob <= 1):
        raise ValueError("flanking-prob must be between 0 and 1")

    if args.flanking_length < 0:
        raise ValueError("flanking-length must be >= 0")

    if not (0 <= args.completeness <= 1):
        raise ValueError("completeness must be between 0 and 1")


def main() -> int:
    """
    Main entry point.

    Returns:
        int: Exit code (0 = success, 1 = error)
    """
    parser = create_parser()
    args = parser.parse_args()

    try:
        validate_arguments(args)

        sim = Simulator(
            num_sequences=args.num_sequences,
            min_orf_length=args.min_length,
            max_orf_length=args.max_length,
            flanking_probability=args.flanking_prob,
            flanking_length=args.flanking_length,
            completeness_ratio=args.completeness,
        )

        sim.save_fasta(args.output)

        sys.stdout.write(
            f"Generated {args.num_sequences} sequences → {args.output}\n"
        )
        return 0

    except ValueError as e:
        sys.stderr.write(f"Error: {e}\n")
        return 1

    except Exception as e:
        sys.stderr.write(f"Unexpected error: {e}\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
