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

gene_str: str = 'ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT'

def string_to_gene(gene_str: str) -> Gene:

    gene: Gene = []

    for nuc_group in range(0, len(gene_str), 3):

        if (nuc_group + 2) >= len(gene_str):
            
            return gene

        codon: Codon = (
            Nucleotide[gene_str[nuc_group]],
            Nucleotide[gene_str[nuc_group + 1]], 
            Nucleotide[gene_str[nuc_group + 2]]
        )

        gene.append(codon)

    return gene

gene: Gene = string_to_gene(gene_str)

for g in gene:

    print(f'{g[0].name}-{g[1].name}-{g[2].name}')