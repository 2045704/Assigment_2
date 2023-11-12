from Bio import SeqIO
from Bio.Seq import Seq

def SPLC(s,introns):
    for i in introns:
        s = s.replace(i,'')
    protein = Seq(s).transcribe().translate()
    return protein

with open(r'C:\Users\newma\Downloads\rosalind_splc (1).txt','r') as file:
    dataset = list(SeqIO.parse(file,"fasta"))
    #print(dataset[0]) HO CAPITOOOOOOOOO
    s = dataset[0].seq
    introns = [intron.seq for intron in dataset[1:]]
    splc = SPLC(s,introns)
    for char in splc:
        if char == '*':
            splc = splc.replace('*','')
    print(splc)