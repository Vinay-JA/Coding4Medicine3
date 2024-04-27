import re
def find_subsequence_locations_in_fasta(file_path):
    sequences = {}
    current_header = None
    current_sequence = ""
    with open(file_path, 'r') as fasta_file:
        for line in fasta_file:
            line = line.strip()
            if line.startswith('>'):
                if current_header is not None:
                    sequences[current_header] = current_sequence
                current_header = line[1:].split()[0]
                current_sequence = ""
            else:
                current_sequence += line
        if current_header is not None:
            sequences[current_header] = current_sequence
    pattern = re.compile(r'AT[A|T|G|C]GT[A|T|G|C]A[A|C]A')
    matches = {}
    for header, sequence in sequences.items():
        matches[header] = [
            match.start() + 1 for match in re.finditer(pattern, sequence)]
    print("matches", matches)
    return matches
fasta_file_path = "/Users/vinayjagtiani/Code/Coding4Medicine/Project 3/fasta.txt"
subsequence_locations = find_subsequence_locations_in_fasta(fasta_file_path)
print("subsequence_locations", subsequence_locations)
for header, locations in subsequence_locations.items():
    print("Sequence:", header)
    if locations:
        print("Locations:", locations)
    else:
        print("No matches found.")
    print()
