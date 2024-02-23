# powiedz mi w takim razie ile mam ci tych podpunktow zrobic
# dwa pierwsze sa ez
# c jest w miare
# d jest ez ale nie da sie go zrobic bez c
# do ktorej piszeccie?
# do 13:50
# powiedz co chcesz miec ba tescie
# nizez masz zrobione a i b


import requests

path = 'plik_wejsciowy'
with open(path, 'w') as file:
    file.write('P10321\nP04439\nP01889\nP17693\nP13747')

with open(path, 'r') as file:
    daneUniprot = file.read().split('\n')

def uniprotIDtoKEGG_ID(uniprotID):
    url = f'https://rest.uniprot.org/uniprotkb/{uniprotID}.txt'

    resp = requests.get(url)
    if resp.ok:
        resp = resp.text.split('\n')
        for line in resp:
            if line.startswith('DR   KEGG'):
                keggID = line.split(';')[1].strip()
                print(f'UniprotID: {uniprotID}\tKeggID: {keggID}')
    else: 
        print('blad linku')

def main():
    for uniprotID in daneUniprot:
        uniprotIDtoKEGG_ID(uniprotID)

    fastas = []
    for uniprotID in daneUniprot:
        url = f'https://rest.uniprot.org/uniprotkb/{uniprotID}.fasta'

        resp = requests.get(url)
        if resp.ok:
            fastas.append(resp.text)

    with open('fastas.txt', 'w') as f:
        f.writelines(fastas)
