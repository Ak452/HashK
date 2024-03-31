## Description :

HashK est un outil en python qui permet de déchiffrer des hash "sha256", cette outil peut-être utiliser lors de pentest ou de CTF(Capture The Flag) et que l'on à un hash sha256 à déchiffrer. Le but de l'outil est de comparé le hash à une liste de mots donnée et de trouvé une correspondance entre les 2.

## Utiilisation :
python3 hashk.py -w [chemin_de_la_wordlist] -H [chemin_du_hash]
ex : python3 hashk.py -w /usr/share/wordlists/rockyou.txt -H /home/kali/hash.txt

## Options utiles :
-w : chemin pour accedez au fichier de la wordlist
-H : chemin pour accedez au fichier du hash
-h : pour afficher le menu d'aide

## Installation :
1. Vérifier que python3 est installer sur votre système
2. cloner le programme via git clone :
**git clone https://github.com/Ak452/HashK.git**
3. accédez au bon répertoire :
   **cd HashK**
4. Installer les éléments requis :
   **pip install -r requirements.txt**
5. Le programme est prêt à être utiliser.
