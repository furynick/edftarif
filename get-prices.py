from pypdf import PdfReader
import re

reader = PdfReader("https://particulier.edf.fr/content/dam/2-Actifs/Documents/Offres/Grille_prix_Tarif_Bleu.pdf")
page = reader.pages[0]
text = page.extract_text()
lines = text.split("\n")
found = False
for line in lines:
  if "tempo" in line.lower():
    found = True
  if found and re.search("^[0-9]", line):
    print(line)
