from enum import IntEnum 
from typing import Tuple, List 

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

# How IntEnum works?
# It's a variation of Enum where the created class is subclass of int too.
# With that it's possible to compare elements from different IntEnum Classes.
# As IntEnum is callable we can create as showed above (like namedtuples) or
# like bellow:

nucleotide: Nucleotide = Nucleotide

class Nucleotide(IntEnum):

    A = 1
    C = 2
    G = 3
    T = 4

# In this case the class is used directly.