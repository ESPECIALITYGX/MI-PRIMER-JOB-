import random
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobacion",
            "CREEPY": "Aterrador, siniestro",
            "AGGRO": "Ponerse agresivo/enejado",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(word,":",meme_dict[word])
else:
    print("ERROR, PALABRA NO ENCONTRADA")
    print("Pero te peudo dar otraas palabras:")
    new = random.choice( meme_dict.keys() )
    print( new,":",,meme_dict[new] ) 
    
