import sys

idseq=False
idvar=False
seq=''
var=''


def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap_penalty=-2):
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)
    score_matrix=[]
    for i in range (len_seq1+1) : #Création de la matrice
        for j in range (len_seq2+1) :
            L.append(0)
        score_matrix.append(L)    
    
    for i in range(len_seq1 + 1):
        score_matrix[i][0] = i * gap_penalty

    for j in range(len_seq2 + 1):
        score_matrix[0][j] = j * gap_penalty

    return 

for line in sys.stdin:
    line=line.rstrip()
    if line.startswith('>') and 'var' not in line:
        idseq=True
        idvar=False
        if var!='' and seq!='':
            print('seq',seq)
            print('var',var)
        var=''
        seq=''
    if line.startswith('>') and 'var' in line:
        idseq=False
        idvar=True
    if line.startswith('A') or line.startswith('T') or line.startswith('G') or line.startswith('C') :
        if idseq :
            seq= seq + line
        if idvar :
            var = var + line

