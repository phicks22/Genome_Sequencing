# Algorithms for Coursera course "Genome Sequencing: Bioinformatics II."
import numpy as np


def divide_sequence(sequence, k):
    """
    Divides a genome sequence into n k-mer fragments to be sorted in lexicographic order.

    :param sequence: Genome sequence input as a string.
    :param k: K-mer length (nucleotide length of each genome fragment).
    :return: Divided kmer fragments as a space delimited .txt file.
    """

    # Iterate along the sequence storing i:i+k characters as a kmer in a numpy array.
    div_string = np.array([sequence[i:i + k] for i in range(0, len(sequence) - k + 1)])

    # Save each kmer within a space delimited .txt file.
    with open("output.txt", 'w') as filehandle:
        filehandle.writelines("%s " % kmer for kmer in div_string)

    return filehandle


# Example output
# sequence = open("Data/dataset_197_3.txt", "r").read()
# divide_sequence(sequence, 100)

def reconstruct_sequence(file, prefix_length, error):
    """
    Identifies the

    :param kmers: Space-delimited txt file of kmers
    :return: Reconstructed sequence
    """

    # Open and read space-delimited txt file
    with open(file) as f:
        kmers = [line.strip().split(" ") for line in f.readlines()]

    # Convert kmers to a 1-dimensional array
    kmers_array = kmers[0]
    # Initialize the current kmer. The beginning of the sequence will always start with the first entry in the file
    current_kmer = kmers_array[0]
    kmer_length = len(current_kmer)

    # Ensure that the prefix length != the kmer length
    try:
        assert prefix_length != kmer_length
    except:
        print("Prefix length cannot be equal to the kmer length.")

    # Initialize output sequence
    sequence = ''
    for kmer in kmers_array[1::]:
        prefix = current_kmer[0:prefix_length]
        match_index = dict()
        match_index[kmer] = len(list(filter(
            lambda xy: xy[0] == xy[1], zip(current_kmer[prefix_length-1::], kmer[0:kmer_length-1]))))
        next_kmer = max(match_index, key=match_index.get)
        kmers_array.remove(kmer)
        sequence += (prefix + next_kmer)

    return sequence


# Example output
kmers_file_path = "Data/dataset_198_3.txt"
print(reconstruct_sequence(file=kmers_file_path, prefix_length=1, error=0))

# The following 9 lines were used to move past a question for genome reconstruction where all that was required was to
# place one kmer in front of the other. No intuitive thought was required here. The reconstruct_sequence above was my
# attempt to create a function based on the match indices of each kmer. The course even mentions that the selection of
# kmers is pretty arbitrary anyway.

with open(kmers_file_path) as file:
    geno_list = [line.strip().split(" ") for line in file.readlines()]
    geno_list = geno_list[0]

path = ''
for i in geno_list[:-1]:
    path += i[0]

path = path + geno_list[-1]
print(path)
