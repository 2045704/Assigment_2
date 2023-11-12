from Bio import SeqIO
#import networkx as nx
from math import floor

'''def overlapping_seq(s1,s2):
    comb_seq = []
    overlap_seq = []
    
    for i in range(len(s1)):
        if s1[i:] == s2[:len(s1)-i]:
            comb_seq.append(s1+s2[len(s1)-i:])
            overlap_seq.append(s1[i:])
            break
    for i in range(len(s2)):
        if s2[i:] == s1[:len(s2)-i]:
            comb_seq.append(s1+s2[len(s2)-i:])
            overlap_seq.append(s2[i:])
            break
    
    comb_seq = min(comb_seq,key=len)
    overlap_seq = max(overlap_seq,key=len)
    return comb_seq,overlap_seq

def LONG(dataset):
    while len(dataset) > 1:
        most_overlapping_seq = ""
        most_overlapping_pair = []
        
    
        dataset_copy = dataset
        
        for i in range(len(dataset_copy)-1):
            for j in range(i+1, len(dataset_copy)):
                comb_seq, overlap_seq = overlapping_seq(dataset_copy[i],dataset_copy[j])
                if len(overlap_seq) > len(most_overlapping_seq):
                    most_overlapping_seq = comb_seq
                    most_overlapping_pair = [dataset_copy[i],dataset_copy[j]]             
        
        if most_overlapping_pair:
            dataset.remove(most_overlapping_pair[0])
            dataset.remove(most_overlapping_pair[1])
            dataset.append(most_overlapping_seq)
    
    return dataset'''

def overlapping_seq(s1, s2, min_overlap=None):
    i = 1
    if min_overlap is None:
        min_overlap = floor(len(s2) / 2)
    while i < len(s1):
        i = s1.find(s2[:min_overlap], i)
        if i == -1:
            break
        if s2.startswith(s1[i:]):
            return len(s1) - i
        i += 1

def LONG(seqs):
    fmap, rmap, starts, ends = ({}, {}, {}, {})
    for p1 in seqs.keys():
        for p2 in seqs.keys():
            if p1 in starts or p2 in ends or p1 in p2:
                continue
            n = overlapping_seq(seqs[p1], seqs[p2])
            if n:
                fmap[p1] = {"overlap": n, "next": p2}
                rmap[p2] = p1
                starts[p1] = True
                ends[p2] = True
                break

    k = next(iter(seqs)) 
    while k in rmap:
        k = rmap[k]

    seq = [seqs[k]]
    while k in fmap:
        seq.append(seqs[fmap[k]["next"]][fmap[k]["overlap"] :])
        k = fmap[k]["next"]

    return "".join(seq)


with open(r"C:\Users\newma\Downloads\rosalind_long (3).txt", "r") as file:
    records = SeqIO.to_dict(SeqIO.parse(file, "fasta"))
    seqs = {record.id: str(record.seq) for record in records.values()}
    print(LONG(seqs))