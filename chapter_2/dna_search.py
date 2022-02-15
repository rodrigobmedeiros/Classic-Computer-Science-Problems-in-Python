from enum import IntEnum 
from typing import Tuple, List 

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

# How IntEnum works?
# It's a variation of Enum where the created class is subclass of int too.
# With that it's possible to compare elements from different IntEnum Classes.
# As IntEnum is callable we can create as showed above (like namedtuples) or
# like bellow:

class Nucleotide(IntEnum):

    A = 1
    C = 2
    G = 3
    T = 4

# In this case the class is used directly.

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide] # Codon is a combination of three Nucleotides
Gene = List[Codon] # Gene is a list of codons

teste: str = 'ABCDEFGHI'

def string_to_gene(gene: str) -> Gene:

    for nuc_group in range(0, len(gene), 3):

        codon: Codon = (
            gene[nuc_group],
            gene[nuc_group + 1], 
            gene[nuc_group + 2]
        )

        print(codon)

string_to_gene(teste)