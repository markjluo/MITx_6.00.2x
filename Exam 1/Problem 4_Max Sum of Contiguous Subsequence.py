def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """

    l = len(L)
    seq = {}
    sum_seq = []
    for i in range(l):
        for j in range(l+1-i):
            start_ind = i
            end_ind = i+j
            seq[tuple(L[start_ind:end_ind])] = sum(L[start_ind:end_ind])
            sum_seq.append(sum(L[start_ind:end_ind]))
    return max(sum_seq)

print(max_contig_sum([3, 4, -1, 5, -4]))