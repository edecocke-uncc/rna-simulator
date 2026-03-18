#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Erin Nicole Decocker
# edecocke@charlotte.edu
# ID: 801442694

import argparse
import sys

from simulator import Simulator


def create_parser() -> argparse.ArgumentParser:
    """
    Create and configure the argument parser.

    Returns:
        argparse.ArgumentParser: Configured parser

    Example:
        >>> parser = create_parser()
    """
    parser = argparse.ArgumentParser(
        description="RNA ORF Sequence Simulator"
    )

    parser.add_argument(
        "-n", "--num-sequences",
        type=int,
        default=10,
        help="Number of sequences to generate (default: 10)"
    )

    parser.add_argument(
        "-o", "--output",
        type=str,
        default="sequences.fasta",
        help="Output FASTA file (default: sequences.fasta)"
    )

    parser.add_argument(
        "--min-length",
        type=int,
        default=100,
        help="Minimum ORF length in codons (default: 100)"
    )

    parser.add_argument(
        "--max-length",
        type=int,
        default=1000,
        help="Maximum ORF length in codons (default: 1000)"
    )

    parser.add_argument(
        "--flanking-prob",
        type=float,
        default=0.5,
        help="Probability of adding flanking regions (0-1, default: 0.5)"
    )

    parser.add_argument(
        "--flanking-length",
        type=int,
        default=50,
        help="Length of flanking regions (default: 50)"
    )

    parser.add_argument(
        "--completeness",
        type=float,
        default=0.7,
        help="Ratio of complete ORFs (0-1, default: 0.7)"
    )

    return parser


def validate_arguments(args: argparse.Namespace) -> None:
    """
    Validate parsed command-line arguments.

    Args:
        args: Parsed arguments

    Raises:
        ValueError: If any argument is invalid

    Example:
        >>> validate_arguments(args)
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


def main() -> None:
    """
    Main entry point for the simulator.

    Parses arguments, validates input, runs simulation,
    and writes output FASTA file.
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
            f"Successfully generated {args.num_sequences} sequences "
            f"and saved to '{args.output}'\n"
        )
        sys.exit(0)

    except ValueError as e:
        sys.stderr.write(f"Error: {str(e)}\n")
        sys.exit(1)

    except Exception as e:
        sys.stderr.write(f"Unexpected error: {str(e)}\n")
        sys.exit(2)


if __name__ == "__main__":
    main()
