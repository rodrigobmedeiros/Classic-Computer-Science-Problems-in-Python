from trivial_compression import CompressedGene
from sys import getsizeof
from random import choice

nucleotide_options = ['A', 'C', 'T', 'G']

gene: str = ''.join([choice(nucleotide_options) for i in range(86)])
gene = gene * 100

print(f'original bytes consumed: {getsizeof(gene)} bytes')

gene_compressor = CompressedGene(gene)
compresed_gene = gene_compressor._decompress()

print(f'compressed gene bytes consumed: {getsizeof(compresed_gene)} bytes')