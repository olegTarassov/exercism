import timeit

# My solution
def to_rna(dna_strand):
    dna_rna = {'G':'C', 'C': 'G', 'T': 'A','A':'U'}

    return "".join( [dna_rna[x] for x in dna_strand])

def to_rna_2(dna_strand):
    dna_rna = dict( G='C', C= 'G', T='A', A='U')

    return dna_strand.translate(dna_rna)

def to_rna_3(dna_strand):
    trans = str.maketrans("GCTA", "CGAU")

    return dna_strand.translate(trans)

# Needed for timeit.
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


wrapped = wrapper(to_rna, "ACGTGGTCTTAA")
print( timeit.timeit(wrapped, number=1000))

wrapped = wrapper(to_rna_2, "ACGTGGTCTTAA")
print( timeit.timeit(wrapped, number=1000))

wrapped = wrapper(to_rna_3, "ACGTGGTCTTAA")
print( timeit.timeit(wrapped, number=1000))
