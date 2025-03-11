import sys

from Bio import SeqIO

PDBFile = sys.argv[1]

with open(PDBFile) as pdb_file:
    for record in SeqIO.parse(pdb_file, "pdb-atom"):
        print(">" + record.id)
        print(record.seq)

# PDB file 속의 서열을 출력하는 스크립트
