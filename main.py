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

def reconstruct_sequence(kmers_file_path):
    """
    Identifies the

    :param kmers: Space-delimited txt file of kmers
    :return: Reconstructed sequence
    """

    # Open and read space-delimited txt file
    with open(kmers_file_path) as file:
        kmers = [line.strip().split(" ") for line in file.readlines()]

    # Convert kmers to a 1-dimensional array
    kmers_array = kmers[0]
    current_kmer = kmers_array[0]

    # Initialize output sequence
    sequence = current_kmer
    for i in kmers_array:
        match_index = dict()
        match_index[i] = len(list(filter(lambda xy: xy[0] == xy[1], zip(current_kmer, i))))
        print(match_index)
        next_kmer = max(match_index, key=match_index.get)
        kmers_array.remove(i)
        sequence += next_kmer

    return sequence


# Example output
kmers_file_path = "Data/dataset_198_3.txt"
reconstruct_sequence(kmers_file_path)
