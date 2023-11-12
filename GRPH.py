from Bio import SeqIO

def GRPH(dataset):
    name = []
    seq = []
    #result = ''
    for line in SeqIO.parse(dataset,"fasta"):
        name.append(str(line.name))
        seq.append(str(line.seq))
    for i in range(len(seq)):
        for j in range(len(seq)):
            if i != j:
                if seq[i][-3:] == seq[j][:3]:
                    print(name[i],name[j])
                    #result = name[i],name[j] +'/n'
                    

with open(r'C:\Users\newma\OneDrive\Desktop\PCS_II\Assignment2\sample_dataset.txt','r') as file:
    GRPH(file)