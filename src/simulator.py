#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Erin Nicole Decocker
# edecocke@charlotte.edu
# ID: 801442694

import random
from typing import List, Tuple

from sequence_lib import (
    generate_random_codon,
    generate_random_sequence,
    is_stop_codon,
    get_gc_content,
    get_ambiguity_content,
    write_fasta,
)


class Simulator:
    """
    Simulator class for generating RNA sequences with ORFs and metadata.
    """

    def __init__(
        self,
        num_sequences: int,
        min_orf_length: int,
        max_orf_length: int,
        flanking_probability: float,
        flanking_length: int,
        completeness_ratio: float,
    ) -> None:
        """
        Initialize the Simulator.

        Args:
            num_sequences: Number of sequences to generate
            min_orf_length: Minimum ORF length (codons)
            max_orf_length: Maximum ORF length (codons)
            flanking_probability: Probability of adding flanking regions (0-1)
            flanking_length: Length of flanking regions
            completeness_ratio: Fraction of complete ORFs (0-1)

        Raises:
            ValueError: If parameters are invalid
        """
        if num_sequences <= 0:
            raise ValueError("num_sequences must be positive")
        if min_orf_length <= 0 or max_orf_length < min_orf_length:
            raise ValueError("Invalid ORF length range")
        if not (0 <= flanking_probability <= 1):
            raise ValueError("flanking_probability must be between 0 and 1")
        if flanking_length < 0:
            raise ValueError("flanking_length must be >= 0")
        if not (0 <= completeness_ratio <= 1):
            raise ValueError("completeness_ratio must be between 0 and 1")

        self.num_sequences = num_sequences
        self.min_orf_length = min_orf_length
        self.max_orf_length = max_orf_length
        self.flanking_probability = flanking_probability
        self.flanking_length = flanking_length
        self.completeness_ratio = completeness_ratio


    def generate_orf(self, complete: bool = True) -> str:
        """
        Generate a single ORF.

        Args:
            complete: Whether to generate a complete ORF

        Returns:
            str: RNA sequence of the ORF

        Example:
            >>> sim.generate_orf(True)
            'AUGGCU...UAA'
        """
        codon_count = random.randint(self.min_orf_length, self.max_orf_length)

        if complete:
            middle = "".join(generate_random_codon() for _ in range(codon_count - 2))
            stop = random.choice(["UAA", "UAG", "UGA"])
            return "AUG" + middle + stop

        return generate_random_sequence(codon_count * 3)


    def generate_sequence(self) -> str:
        """
        Generate a full sequence with optional flanking regions.

        Returns:
            str: Final RNA sequence
        """
        is_complete = random.random() < self.completeness_ratio
        orf = self.generate_orf(complete=is_complete)

        if random.random() < self.flanking_probability:
            left = generate_random_sequence(self.flanking_length)
            right = generate_random_sequence(self.flanking_length)
            return left + orf + right

        return orf


    def generate_sequences(self) -> List[Tuple[str, str, str]]:
        """
        Generate multiple sequences with metadata.

        Returns:
            List of tuples: (sequence_id, description, sequence)

        Example:
            >>> sim.generate_sequences()
        """
        results = []

        for i in range(1, self.num_sequences + 1):
            seq = self.generate_sequence()
            gc = get_gc_content(seq)
            amb = get_ambiguity_content(seq)

            seq_type = "complete" if seq.startswith("AUG") else "partial"
            flanked = "yes" if len(seq) > self.max_orf_length * 3 else "no"

            desc = (
                f"length={len(seq)} "
                f"GC={gc:.2f}% "
                f"amb={amb:.2f}% "
                f"type={seq_type} "
                f"flanked={flanked}"
            )

            results.append((f"seq_{i:03d}", desc, seq))

        return results


    def save_fasta(self, output_file: str) -> None:
        """
        Generate sequences and save to a FASTA file.

        Args:
            output_file: Output FASTA file path

        Returns:
            None

        Example:
            >>> sim.save_fasta("output.fasta")
        """
        sequences = self.generate_sequences()
        write_fasta(sequences, output_file)
