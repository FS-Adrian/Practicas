#English Thesaurus
#Hacer una GUI y una Interfaz Web en el futuro 

import json
from difflib import get_close_matches

data = json.load(open("C:/Users/CeciliaRodríguez/Desktop/Proyectos/Practicas/App 1 English Thesaurus/data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if Yes or N if No" % get_close_matches(word,data.keys())[0]).upper()
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
    
        elif yn == "N":
            word = word.capitalize()
            x = 0
            while yn == "N" or x < len(data[data.keys()]):
                yn = input("Did you mean %s instead? Enter Y if Yes or N if No" % get_close_matches(word,data.keys())[x]).upper()
                if yn == "Y":
                    return data[get_close_matches(word,data.keys())[x]]
                elif yn == "N":
                    word = word.upper()
                    x = 0
                    while yn == "N" or x<len(data[data.keys()]):
                        yn = input("Did you mean %s instead? Enters Y if Yes or N if No" % get_close_matches(word,data.keys())[x]).upper()
                        if yn == "Y":
                            return data[get_close_matches(word,data.keys())[x]]
                        else:
                            print ("Comando incorrecto intente de nuevo")
                            return yn == "N"
                
                else:
                    print("Comando incorrecto intente de nuevo")
                    return yn == "N"
            
        else: 
            return "Invalid entry, try again"

    
word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
    else: 
        print(output)


#Explicacion, %s tiene la misma funcionalidad que en C
#Get_close_matches toma  un valor lo compara con lo que le das y 
#procede a regresar el valor que es similar, se pone [0] para que te de el 
#primer elemento de la lista.  