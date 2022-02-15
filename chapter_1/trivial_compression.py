class CompressedGene():

    def __init__(self, gene: str) -> None:

        self._compress(gene)

    def _compress(self, gene: str) -> None:

        # start with a sentinel (a point to start bit operation)
        self.bit_string = 1
        
        for nucleotide in gene.upper():
            
            self.bit_string <<= 2

            if nucleotide == 'A':

                self.bit_string |= 0b00
            
            elif nucleotide == 'C':

                self.bit_string |= 0b01

            elif nucleotide == 'G':

                self.bit_string |= 0b10

            elif nucleotide == 'T':

                self.bit_string |= 0b11

            else:

                raise ValueError(f'Invalid Nucleotide: {nucleotide}')

    def _decompress(self):

        gene: str = ''

        for bin_pair in range(self.bit_string.bit_length() - 1, 2):

            compressed_nucleotide: int = self.bit_string >> bin_pair & 0b11

            if compressed_nucleotide == 0b00:

                gene += 'A'

            elif compressed_nucleotide == 0b01:

                gene += 'C'

            elif compressed_nucleotide == 0b10:

                gene += 'G'

            elif compressed_nucleotide == 0b11:

                gene += 'T'

        
        gene = gene[::-1]

        return gene 

    def __str__(self) -> str:

        return self._decompress()



