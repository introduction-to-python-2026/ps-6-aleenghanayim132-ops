def create_codon_dict(file_path):
  codon_to_amino_acid = {}
  path = "data/codons.txt"
  with open(file_path ,"r") as f:
    rows = f.readlines()
  for row in rows:
   LG=row.strip().split('\t')
   codon = LG[0]
   amino_acid = LG[2]
   codon_to_amino_acid[codon] = amino_acid
  return codon_to_amino_acid
