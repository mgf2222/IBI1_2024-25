def find_restriction_sites(dna, recognition):
    # Validate the DNA sequence
    valid_chars = {'A', 'C', 'G', 'T'}
    for char in dna:
        if char not in valid_chars:
            raise ValueError("Invalid character in DNA sequence")
    
    # Validate the recognition sequence
    for char in recognition:
        if char not in valid_chars:
            raise ValueError("Invalid character in recognition sequence")
    
    # Check if recognition sequence is empty
    if len(recognition) == 0:
        raise ValueError("Recognition sequence cannot be empty")
    
    len_rec = len(recognition)
    cut_sites = []
    
    # Iterate through the DNA to find all occurrences of the recognition sequence
    for i in range(len(dna) - len_rec + 1):
        if dna[i:i+len_rec] == recognition:
            cut_sites.append(i)
    
    return cut_sites

# Example usage:
dna_sequence = "ACGTACGT"
recognition_sequence = "ACG"
print(find_restriction_sites(dna_sequence, recognition_sequence))  # Output: [0, 4]