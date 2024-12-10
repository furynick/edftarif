import urllib3
from pypdf import PdfReader
from io import BytesIO
from re import search

url = "https://particulier.edf.fr/content/dam/2-Actifs/Documents/Offres/Grille_prix_Tarif_Bleu.pdf"
http = urllib3.PoolManager()
remoteFile = http.request("GET", url)
memoryFile = BytesIO(remoteFile.data)
reader = PdfReader(memoryFile)

page = reader.pages[0]
text = page.extract_text()
lines = text.split("\n")
option = "None"
for line in lines:
  if "option" in line.lower():
    words = line.split(" ")
    option = words[1].lower()
  if option != "None" and search("^[0-9]", line):
    print(option + " " + line)
