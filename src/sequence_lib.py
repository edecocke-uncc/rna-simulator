#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Erin Nicole Decocker
# edecocke@charlotte.edu
# ID: 801442694

import random
from typing import List, Tuple


VALID_RNA = {"A", "U", "G", "C"}
AMBIGUOUS = {"N", "R", "Y", "S", "W", "K", "M", "B", "D", "H", "V"}


def get_gc_content(sequence: str) -> float:
    """
    Calculate the GC content of an RNA sequence.

    Args:
        sequence: RNA sequence string (uppercase, U for uracil)

    Returns:
        float: GC content as a percentage (0-100)

    Raises:
        ValueError: If sequence is empty or contains invalid nucleotides

    Example:
        >>> get_gc_content("AUGC")
        50.0
    """
    if not sequence:
        raise ValueError("Sequence cannot be empty")

    sequence = sequence.upper()
    if any(n not in VALID_RNA for n in sequence):
        raise ValueError("Invalid RNA sequence")

    gc_count = sum(1 for n in sequence if n in {"G", "C"})
    return (gc_count / len(sequence)) * 100


def get_ambiguity_content(sequence: str) -> float:
    """
    Calculate percentage of ambiguous IUPAC nucleotides.

    Args:
        sequence: RNA sequence string

    Returns:
        float: Percentage of ambiguous nucleotides (0-100)

    Raises:
        ValueError: If sequence is empty

    Example:
        >>> get_ambiguity_content("AUGN")
        25.0
    """
    if not sequence:
        raise ValueError("Sequence cannot be empty")

    sequence = sequence.upper()
    amb_count = sum(1 for n in sequence if n in AMBIGUOUS)
    return (amb_count / len(sequence)) * 100


def generate_random_codon() -> str:
    """
    Generate a random RNA codon (3 nucleotides).

    Returns:
        str: Random codon string

    Example:
        >>> generate_random_codon()
        'AUG'
    """
    return "".join(random.choice(list(VALID_RNA)) for _ in range(3))


def is_start_codon(codon: str) -> bool:
    """
    Check if a codon is a start codon (AUG).

    Args:
        codon: 3-nucleotide RNA codon

    Returns:
        bool: True if start codon, else False

    Raises:
        ValueError: If codon is not length 3

    Example:
        >>> is_start_codon("AUG")
        True
    """
    if len(codon) != 3:
        raise ValueError("Codon must be length 3")

    return codon.upper() == "AUG"


def is_stop_codon(codon: str) -> bool:
    """
    Check if a codon is a stop codon (UAA, UAG, UGA).

    Args:
        codon: 3-nucleotide RNA codon

    Returns:
        bool: True if stop codon, else False

    Raises:
        ValueError: If codon is not length 3

    Example:
        >>> is_stop_codon("UAA")
        True
    """
    if len(codon) != 3:
        raise ValueError("Codon must be length 3")

    return codon.upper() in {"UAA", "UAG", "UGA"}


def generate_random_sequence(length: int) -> str:
    """
    Generate a random RNA sequence.

    Args:
        length: Length of sequence

    Returns:
        str: Random RNA sequence

    Raises:
        ValueError: If length <= 0

    Example:
        >>> generate_random_sequence(5)
        'AUGCU'
    """
    if length <= 0:
        raise ValueError("Length must be positive")

    return "".join(random.choice(list(VALID_RNA)) for _ in range(length))


def write_fasta(sequences: List[Tuple[str, str, str]], output_file: str) -> None:
    """
    Write sequences to a FASTA file.

    Args:
        sequences: List of tuples (id, description, sequence)
        output_file: Output file path

    Returns:
        None

    Raises:
        ValueError: If sequences list is empty

    Example:
        >>> seqs = [("seq1", "example", "AUGC")]
        >>> write_fasta(seqs, "out.fasta")
    """
    if not sequences:
        raise ValueError("Sequences list cannot be empty")

    with open(output_file, "w") as f:
        for seq_id, desc, seq in sequences:
            f.write(f">{seq_id} {desc}\n")
            f.write(f"{seq}\n")
