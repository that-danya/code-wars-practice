def DNA_strand(dna):
    # code here
    dna_dict = { 'A': 'T',
            'T': 'A',
            'G': 'C',
            'C': 'G', }
    compl = []
    for i in dna:
        compl.append(dna_dict[i])
    compl = ''.join(compl)
    
    return compl