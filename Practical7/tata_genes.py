import re

def extract_gene_name(header_line):
    parts = header_line.split()
    for part in parts:
        if part.startswith('gene:'):
            gene_part = part.split(':')
            if len(gene_part) >= 2:
                return gene_part[1]
    return None

input_filename = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_filename = 'tata_genes.fa'
tata_pattern = re.compile(r'TATA[AT]A[AT]', re.IGNORECASE)

with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
    current_gene_name = None
    current_sequence = []
    
    for line in infile:
        if line.startswith('>'):
            # Process the previous gene
            if current_gene_name is not None:
                full_sequence = ''.join(current_sequence)
                if tata_pattern.search(full_sequence):
                    outfile.write(f'>{current_gene_name}\n')
                    outfile.write(full_sequence + '\n')
            # Parse the new header
            header_content = line[1:].strip()
            current_gene_name = extract_gene_name(header_content)
            current_sequence = []
        else:
            current_sequence.append(line.strip())
    
    # Process the last gene after the loop
    if current_gene_name is not None:
        full_sequence = ''.join(current_sequence)
        if tata_pattern.search(full_sequence):
            outfile.write(f'>{current_gene_name}\n')
            outfile.write(full_sequence + '\n')
