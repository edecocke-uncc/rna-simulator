# PASS (Python RNA sequence simulator)

## Overview
PASS (Python RNA sequence simulator) is a tool that generates synthetic RNA sequences in FASTA format. It produces configurable sets of Open Reading Frames (ORFs) sequences that may be complete (bounded by start and stop codons), partial, or flanked by non-coding regions, making it useful for testing bioinformatics pipelines, generating mock datasets, and exploring RNA sequence properties. Each output sequence is annotated with metadata including length, GC content, ambiguity content, and structural type.

### Features:
  - Flexible ORF generation: produces complete ORFs (AUG → stop codon) or partial sequences of configurable length
  - Non-coding flanking regions: randomly appends upstream/downstream flanking sequences with tunable probability
  - Configurable output: controls sequence count, length range, completeness ratio, and flanking behavior via command-line arguments
  - Sequence metadata: each FASTA header includes length, GC content (%), ambiguity content (%), ORF type, and flanked status
  - IUPAC ambiguity support: sequences may contain standard ambiguity codes

## Usage 
### Dependency Requirements:
  - python=3.10
  - numpy
  - Biopython
### Installation
### Setup
1. Clone the repository:
```bash
git clone https://github.com/edecocke-uncc/rna-simulator.git
```
2. Go into your project folder:
```bash
cd rna-simulator
```
3. Environment Setup
This project uses a Conda environment to manage dependencies.

4. Create the Environment: 
```bash
conda env create -f environment.yml
```
5. Activate the Environment
```bash
conda activate rna-simulator
```

### Usage Examples:
**Example 1: Default parameters**
```bash
python src/main.py
```
Output:
  - Successfully generated 10 sequences
  - Output saved to: sequences.fasta

**Example 2: Specify output file**
```bash
python src/main.py -o test.fasta
```
Output:
  - Successfully generated 10 sequences
  - Output saved to 'test.fasta'

**Example 3: Custom parameters**
```bash
python src/main.py -n 50 -o my_seqs.fasta --min-length 200 --max-length 2000
```
Output:
  - Successfully generated 50 sequences
  - Output saved to: my_seqs.fasta

### Command-Line Arguments: All flags and defaults
Arguments:
  - --num-sequences / -n: Number of sequences(default: 10)
  - --output / -o: Output FASTA file (default:sequences.fasta)
  - --min-length: Minimum ORF length (default: 100)
  - --max-length: Maximum ORF length (default:1000)
  - --flanking-prob: Flanking probability 0-1 (default: 0.5)
  - --flanking-length: Flanking sequence length (default: 50)
  - --completeness: Ratio of complete ORFs 0-1 (default: 0.7)
  - --ambiguity-rate: Probability of ambiguous bases (0-1, default: 0.0)
### Output Format
```bash
>seq_003 length=585 GC=52.80% amb=1.20% type=complete flanked=no
AUGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGNCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUACGCGCGCGGCUAA
```

### Project Structure: Directory layout explanation
```bash
rna-simulator/
├── README.md 
├── LICENSE 
├── pseudocode.txt 
├── environment.yml 
├── src/
│ ├── __init__.py 
│ ├── main.py 
│ ├── simulator.py 
│ └── sequence_lib.py 
└── examples/
 ├── example_output.fasta 
 └── example_run.txt
```
9. Algorithm Description: How sequences are
generated
10. Metadata: How GC and ambiguity are calculated

## References:
- IUPAC Codes: https://www.bioinformatics.org/sms/iupac.html
- FASTA Format: https://en.wikipedia.org/wiki/FASTA_format
- Open Reading Frames: https://en.wikipedia.org/wiki/Open_reading_frame
- Biopython: https://biopython.org/Python argparse: https://docs.python.org/3/library/argparse.html
- Python Type Hints: https://docs.python.org/3/library/typing.html
- PEP 8: https://www.python.org/dev/peps/pep-0008/

## License
This project is licensed under the GNU GPL v2.1. Chosen for open collaboration, ease of edits, and public use.

## Author
- Erin Nicole Decocker
- edecocke@charlotte.edu
- ID: 801442694
Include at least 3 example commands showing
different use cases.
