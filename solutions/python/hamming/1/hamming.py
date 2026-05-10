def distance(strand_a, strand_b):

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    
    strand_length = len(strand_a)
    differences = 0

    if strand_length == 0:
        return differences
    
    for index in range(strand_length):
        if strand_a[index] != strand_b[index]:
            differences += 1
    
    return differences
