# Algorithms for Coursera course "Genome Sequencing: Bioinformatics II."
import numpy as np


def divide_sequence(sequence, k):
    """
    Divides a genome sequence into n k-mer fragments to be sorted in lexicographic order.

    :param sequence: Genome sequence input as a string.
    :param k: K-mer length (nucleotide length of each genome fragment).
    :return: Divided kmer fragments as a space delimited .txt file.
    """

    div_string = np.array([sequence[i:i + k] for i in range(0, len(sequence) - k + 1)])

    with open("output.txt", 'w') as filehandle:
        filehandle.writelines("%s " % kmer for kmer in div_string)

    return filehandle


# Example output
sequence = open("Data/dataset_197_3.txt", "r").read()
divide_sequence(sequence, 100)
