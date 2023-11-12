from Bio import SeqIO
def hamm(s1,s2):
    hamm = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            hamm += 1
    return hamm

def CORR(data):
    corrections = []
    correct_seqs = []
    incorrect_seqs = []
    comp_dict = {'A':'T','T':'A','C':'G','G':'C'}
    
    for line in data:
        reversed_seq = "".join([comp_dict[i] for i in line[::-1]])
        if data.count(line) + data.count(reversed_seq) >= 2:
            correct_seqs.append(line)
        else:
            incorrect_seqs.append(line)
    
    for n in incorrect_seqs:
        for correction in correct_seqs:
            reversed_corr = "".join([comp_dict[i] for i in correction[::-1]])
            if hamm(n,correction) == 1:
                corrections.append((n,correction))
                break
            if hamm(n,reversed_corr) == 1:
                corrections.append((n,reversed_corr))
                break
            
    return corrections

seq_name = []
seq_str = []
with open(r'C:\Users\newma\Downloads\rosalind_corr (1).txt','r') as file:
    for record in SeqIO.parse(file,'fasta'):
        #seq_name.append(str(record.name))
        seq_str.append(str(record.seq))
        
    corr = CORR(seq_str)
    for n, correction in corr:
        print("{}->{}".format(n,correction))