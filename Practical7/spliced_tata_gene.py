import re
import os
"""
The provided Python code first sets the working directory to "Practical7", then defines two functions: `extract_gene_name` 
to extract gene names from header lines and `main` to handle the core processing.
In the `main` function, it prompts the user to enter one of the valid splice donor/acceptor combinations (GTAG, GCAG, ATAC), validates the input, and processes a FASTA file (`Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa`). 
For each gene entry in the file, it extracts the gene name, accumulates the sequence, and after processing all lines, checks for TATA box motifs using a regular expression. 
If TATA box motifs are found, it writes the gene sequence along with the count of TATA motifs to an output file named based on the user's input. Finally, it prints a completion message with the output file name.
"""

# Set working directory
os.chdir('Practical7')
#If the file cannot be read correctly, use the absolute path below
#os.chdir(r"D:\IBI\IBImidterm\IBI1_2024-25\Practical7")
def extract_gene_name(header_line):
    parts = header_line.split()
    for part in parts:
        if part.startswith('gene:'):
            gene_part = part.split(':')
            if len(gene_part) >= 2:
                return gene_part[1]
    return None

def main():
    # Get user input for splice donor/acceptor combination
    valid_combinations = {'GTAG', 'GCAG', 'ATAC'}
    while True:
        user_input = input("Please enter one of the splice donor/acceptor combinations (GTAG, GCAG, ATAC): ").strip().upper()
        if user_input in valid_combinations:
            break
        print("Invalid input. Please enter one of the specified combinations.")
    
    input_filename = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
    output_filename = f'{user_input}_spliced_genes.fa'
    tata_pattern = re.compile(r'TATA[AT]A[AT]', re.IGNORECASE)
    
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        current_gene_name = None
        current_sequence = []
        
        for line in infile:
            if line.startswith('>'):
                # Process the previous gene
                if current_gene_name is not None:
                    full_sequence = ''.join(current_sequence)
                    tata_matches = tata_pattern.findall(full_sequence)
                    if tata_matches:
                        tata_count = len(tata_matches)
                        outfile.write(f'>{current_gene_name}_TATA_count:{tata_count}\n')
                        outfile.write(f'{full_sequence}\n')
                # Parse the new header
                header_content = line[1:].strip()
                current_gene_name = extract_gene_name(header_content)
                current_sequence = []
            else:
                current_sequence.append(line.strip())
        
        # Process the last gene after the loop
        if current_gene_name is not None:
            full_sequence = ''.join(current_sequence)
            tata_matches = tata_pattern.findall(full_sequence)
            if tata_matches:
                tata_count = len(tata_matches)
                outfile.write(f'>{current_gene_name}_TATA_count:{tata_count}\n')
                outfile.write(f'{full_sequence}\n')
    
    print(f"Processing complete. Output written to {output_filename}")

if __name__ == "__main__":
    main()