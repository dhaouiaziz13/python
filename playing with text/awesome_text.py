import pyfiglet
from colorama import Fore,Back,init
import base64

#dont forget to istall the needed libraries(pyfiglet,colorama) using : pip install <librarie name>
styles={'1':"digital",'2':"bulbhead",'3':"bubble",'4':"dotmatrix",'5':"alligator",'6':"letters",'7':"isometric1",'8':"doh",'9':"banner3-D",'10':"alphabet",'11':"5lineoblique",'12':"3x5",'13':"3-d",'14':"slant"}




name=base64.b64decode('TUFERSBCWSBESEFPVUkK').decode('utf-8')
print(Fore.BLUE+name.center(50))
init(autoreset=True,convert=True)

while True:
    text=input(Fore.MAGENTA+'type something :')
    text=str(text)
    if text :
        break
    else:
        print(Fore.RED+'please type something')
        continue

i=0
while True:
    string='type help to learn more about styles :'
    try:
        if i>0:
            string=''
        style=input(Fore.GREEN+'gimme style number ==> '+ string)
        style=str(style)
        i+=1
        if style=='exit()':
            break
        elif style =='help':
            for key,value in styles.items():
                print(Fore.BLUE+(key+' : '+value))
                continue
        word=pyfiglet.figlet_format(text,font=styles.get(style))
        print(word)
    except Exception as e:
        print(Fore.RED+'wrong font style')
input()
