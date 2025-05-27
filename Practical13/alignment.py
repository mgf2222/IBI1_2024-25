# import the necessary libraries
import os

# change the working directory to the location of the script
os.chdir(r"d:\IBI\IBImidterm\IBI1_2024-25\Practical13")

# function to read FASTA files
def read_fasta(file):
    seq = ""
    with open(file, 'r') as f:
        for line in f:
            # skip header lines that start with ">"
            if not line.startswith(">"):
                seq += line.strip()
    return seq

# function to read BLOSUM62 scoring matrix
def read_matrix(file):
    matrix = {}
    with open(file, 'r') as f:
        lines = f.readlines()
    
    # find the header row with column names
    cols = []
    for line in lines:
        if line.startswith(" "):
            cols = line.split()
            break
    
    # read the scoring data
    for line in lines:
        # skip header and comment lines
        if line.startswith(" ") or line.startswith("#"):
            continue
        parts = line.split()
        row = parts[0]  # amino acid for this row
        scores = parts[1:]  # scores for this amino acid
        # store scores in dictionary with amino acid pair as key
        for i, score in enumerate(scores):
            matrix[(row, cols[i])] = int(score)
    
    return matrix

# function to perform sequence alignment
def align(seq1, seq2, matrix):
    score = 0  # total BLOSUM score
    same = 0   # count of identical amino acids
    length = min(len(seq1), len(seq2))  # use shorter sequence length
    
    # compare sequences position by position
    for i in range(length):
        a1 = seq1[i]  # amino acid from first sequence
        a2 = seq2[i]  # amino acid from second sequence
        if a1 == a2:
            same += 1  # count identical matches
        # add BLOSUM score for this amino acid pair
        score += matrix.get((a1, a2), 0)  # use 0 if pair not found
    
    # calculate percentage of identical amino acids
    percent = (same / length) * 100
    return score, percent

# main program
def main():
    # read sequence files
    h = read_fasta("human_sod2.fasta")
    m = read_fasta("mouse_sod2.fasta") 
    r = read_fasta("random_sequence.fasta")
    
    # read scoring matrix
    matrix = read_matrix("BLOSUM.txt")
    
    # define sequence pairs to compare
    tests = [("Human vs Mouse", h, m), 
             ("Human vs Random", h, r), 
             ("Mouse vs Random", m, r)]
    
    # perform alignments and display results
    for name, s1, s2 in tests:
        score, percent = align(s1, s2, matrix)
        print(f"{name}:")
        print(f" Score = {score}")
        print(f" Same = {percent:.2f}%\n")

# run the main program
main()