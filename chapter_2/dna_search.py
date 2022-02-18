from enum import IntEnum 
from typing import Tuple, List 



# How IntEnum works?
# It's a variation of Enum where the created class is subclass of int too.
# With that it's possible to compare elements from different IntEnum Classes.
# As IntEnum is callable we can create as showed above (like namedtuples) or
# like bellow:

# 1° implementation of IntEnum subclass
Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

# 2° implementation of IntEnum subclass
class Nucleotide(IntEnum):

    A = 1
    C = 2
    G = 3
    T = 4

# In this case the class is used directly.

# Remember that it's a type definition
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide] # Codon is a combination of three Nucleotides
Gene = List[Codon] # Gene is a list of codons

def string_to_gene(gene_str: str) -> Gene:
    """
    Convert gene information from strings into Gene Type.
    """
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

def linear_search(gene: Gene, codon: Codon) -> bool:
    """
    Linear search implementation, to look for a codon into a gene.
    """
    for current_codon in gene:

        if current_codon == codon:

            return True 

    return False

gene_str: str = 'ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT'
gene: Gene = string_to_gene(gene_str)

codon_to_search: Codon = (
    Nucleotide.G,
    Nucleotide.G,
    Nucleotide.G
)

is_codon_in_gene: bool = linear_search(gene, codon_to_search)
print(is_codon_in_gene)