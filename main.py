# Algorithms for Coursera course "Genome Sequencing: Bioinformatics II."

def divide(sequence, k):
    """
    Divides a genome sequence into n k-mer fragments to be sorted in lexicographic order.

    :param sequence: Genome sequence input as a string.
    :param k: K-mer length (nucleotide length of each genome fragment).
    :return: Divided genome fragment within an array.
    """

    div_string = [sequence[i:i+k] for i in range(0, len(sequence), k)]

    return div_string

