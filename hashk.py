import argparse
from tqdm import tqdm
import time
import termcolor
from termcolor import colored
import hashlib
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def main():
    print("""

    ██╗  ██╗ █████╗ ███████╗██╗  ██╗██╗  ██╗
    ██║  ██║██╔══██╗██╔════╝██║  ██║██║ ██╔╝
    ███████║███████║███████╗███████║█████╔╝ 
    ██╔══██║██╔══██║╚════██║██╔══██║██╔═██╗ 
    ██║  ██║██║  ██║███████║██║  ██║██║  ██╗
    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
                                            
                                     
""")
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--wordlist", help="Path de la wordlist", action="store")
    parser.add_argument("-H", "--hash", help="Le hash (sha256)", action="store")
    args = parser.parse_args()

    wordlist_path = args.wordlist
    hash_sha = args.hash


    file = open(hash_sha, "r")   
    hash256 = file.read().strip()
    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as wsl:
        try:
            total_passwords = sum(1 for _ in wsl)
        except FileNotFoundError:
            print(Fore.RED + "[-] Aucun fichier trouver")
            return
        if total_passwords == 0:
            print(Fore.RED + "[-] la wordlist est vide")
            return    

    password_found = False

    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as wsl:
        progress_bar = tqdm(total=total_passwords, desc=Fore.GREEN + "brute force en cours...", dynamic_ncols=True)
        for password in wsl:
            password = password.strip()
            hashed = hashlib.sha256(password.encode()).hexdigest()
            if hashed == hash256:
                password_found = True
                break
            progress_bar.update(1)

    progress_bar.close()

    if password_found:
            print(colored("[+]", "green"), colored("mot de passe trouvé :", "blue"), password)
    else:
            print(Fore.RED + "[-] Aucun mot de passe n'a était trouvé...")
if __name__ == "__main__":
    main()
