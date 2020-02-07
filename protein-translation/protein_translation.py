
RNA_DICT = {
            'AUG' :'Methionine',
            'UUU' :'Phenylalanine',
            'UUC' :'Phenylalanine',
            'UUA' :'Leucine',
            'UUG' :'Leucine',
            'UCU' :'Serine',
            'UCC' :'Serine',
            'UCA' :'Serine',
            'UCG' :'Serine',
            'UAU' :'Tyrosine',
            'UAC' :'Tyrosine',
            'UGU' :'Cysteine',
            'UGC' :'Cysteine',
            'UGG' :'Tryptophan',
            'UAA' :'STOP',
            'UAG' :'STOP',
            'UGA' :'STOP'
}

def proteins_me(strand):
    step = 3
    proteins_translated = [ RNA_DICT[ strand[x:x+step] ] for x in range(0,len(strand),step) ]
    stop = proteins_translated.index('STOP') if 'STOP' in proteins_translated else None

    return proteins_translated[ : stop ]





from itertools import takewhile
from textwrap import wrap


catalogue = {
    'AUG': 'Methionine',
    'UUC': 'Phenylalanine',
    'UUU': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAC': 'Tyrosine',
    'UAU': 'Tyrosine',
    'UGC': 'Cysteine',
    'UGU': 'Cysteine',
    'UGG': 'Tryptophan',
}


def is_not_stop(pattern):
    return pattern not in ('UAG', 'UAA', 'UGA')


def proteins(strand):
    print(wrap(strand, 3))
    return [protein
            for pattern in takewhile(is_not_stop, wrap(strand, 3))
            for protein in (catalogue.get(pattern, None),)
            if protein]

print( proteins('AUGUUUUGG'))