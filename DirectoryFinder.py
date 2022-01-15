# [+]==================[Creditos]==================[+]
#  #                                                #
#  #     Devs: Ghosty / xNullCode / Deneb           #
#  #     Discord:                                   #
#  #        Ghostykdi#7168                          #
#  #     Derechos de Author:                        #
#  #         Ghosty / xNullCode / Deneb             #
# [+]==================[Creditos]==================[+]
#
#                        |\**/|
#                        \ == /
#                         |  |
#                         |  |
#                         \  /
#                          \/
#
# [+]==================[Start Code]==================[+]
#

import requests, colorama, os, sys
from colorama import *
init(convert=True)
url = ""

dirs = []

banner = rf"""{Fore.LIGHTCYAN_EX}
       .--.                   .---.
   .---|__|           .-.     |~~~|
.--|===|--|_          |_|     |~~~|--.
|  |===|  |'\     .---!~|  .--|   |--|     
|D |   |  |.'\    |===| |--|MA|   |  |      {Fore.LIGHTWHITE_EX}'{Fore.LIGHTCYAN_EX}@{Fore.LIGHTWHITE_EX}': {Fore.LIGHTWHITE_EX}'{Fore.LIGHTCYAN_EX}DirectoryFinder{Fore.LIGHTWHITE_EX}',{Fore.LIGHTCYAN_EX}
|e |   |  |\.'\   |   | |__|  |   |  |      {Fore.LIGHTWHITE_EX}'{Fore.LIGHTCYAN_EX}@{Fore.LIGHTWHITE_EX}': {Fore.LIGHTWHITE_EX}'{Fore.LIGHTCYAN_EX}By DenebS4c{Fore.LIGHTWHITE_EX}'{Fore.LIGHTCYAN_EX}
|n |   |  | \  \  |===| |==|  |   |  |     
|e |   |__|  \.'\ |   |_|__|  |~~~|__|
|b |===|--|   \.'\|===|~|--|TH|~~~|--|
^--^---'--^    `-'`---^-^--^--^---'--'
{Fore.RESET}"""

if len(sys.argv) != 4:
    print(banner)
    print(f"{Fore.LIGHTCYAN_EX}Use: {Fore.RESET}{sys.argv[0]}{Fore.LIGHTCYAN_EX} <{Fore.RESET}https://example.com or https://example.com/DF.php{Fore.LIGHTCYAN_EX}> <{Fore.RESET}wordlist{Fore.LIGHTCYAN_EX}> <{Fore.RESET}show all status code 'y/n'{Fore.LIGHTCYAN_EX}>")
    sys.exit(0)

url = str(sys.argv[1])
wordlist = str(sys.argv[2])
show_all_status_code = str(sys.argv[3])

with open(wordlist, "r") as f:
    for i in f:
        dirs.append(i.replace('\n', ''))

def main(url, dir):
    os.system("cls || clear")
    print(banner)
    print(Fore.LIGHTWHITE_EX+"-"*70); print()

    try:
        url_split = url.split("DF")
        #print(url_split)
        for dirs in dir:
            try:
                URL = url_split[0] + dirs + url_split[1]
                req = requests.request('GET',URL, timeout=20)
                if show_all_status_code == "y":
                    if req.status_code == 200:
                        print(Fore.LIGHTGREEN_EX+str(req.status_code)+"\t"+Fore.LIGHTCYAN_EX+URL)
                    elif req.status_code == 404:
                        print(Fore.LIGHTRED_EX+str(req.status_code)+"\t"+Fore.LIGHTCYAN_EX+URL)
                    elif req.status_code == 403:
                        print(Fore.LIGHTYELLOW_EX+str(req.status_code)+"\t"+Fore.LIGHTCYAN_EX+URL)
                else:
                    if req.status_code == 200:
                        print(Fore.LIGHTGREEN_EX+str(req.status_code)+"\t"+Fore.LIGHTCYAN_EX+URL)
            except KeyboardInterrupt:
                sys.exit(0)

    except:

        for dirs in dir:
            try:
                if url.endswith("/"):
                    URL = url + dirs
                else:
                    URL = url + "/" + dirs
                req = requests.request('GET',URL, timeout=20)
                if show_all_status_code == "y":
                    if req.status_code == 200:
                        print(Fore.LIGHTGREEN_EX+str(req.status_code)+"\t"+Fore.LIGHTCYAN_EX+URL)
                    elif req.status_code == 404:
                        print(Fore.LIGHTRED_EX+str(req.status_code)+"\t"+Fore.LIGHTCYAN_EX+URL)
                    elif req.status_code == 403:
                        print(Fore.LIGHTYELLOW_EX+str(req.status_code)+"\t"+Fore.LIGHTCYAN_EX+URL)
                else:
                    if req.status_code == 200:
                        print(Fore.LIGHTGREEN_EX+str(req.status_code)+"\t"+Fore.LIGHTCYAN_EX+URL)
            except KeyboardInterrupt:
                sys.exit(0)

main(url, dirs)

#
# [+]==================[End Code]==================[+]
#
#                          /\           
#                         /  \    
#                         |  |     
#                         |  |     
#                        / == \    
#                        |/**\|  
#    
# [+]==================[Creditos]==================[+]
#  #                                                #
#  #     Devs: Ghosty / xNullCode / Deneb           #
#  #     Discord:                                   #
#  #        Ghostykdi#7168                          #
#  #     Derechos de Author:                        #
#  #         Ghosty / xNullCode / Deneb             #
# [+]==================[Creditos]==================[+]