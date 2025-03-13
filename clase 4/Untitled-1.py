tabla_traduccion = str.maketrans({"a": "4", "e": "3", "i": "1", "o": "0", "u": "7"}) # asocio las vocales con los numeros
texto_original = "Hola, bienvenido al mundo de Python." 
texto_traducido = texto_original.translate(tabla_traduccion) # tradusco las letras por los numeros que les asocie

print(f"Texto original: {texto_original}")
print(f"Texto traducido: {texto_traducido}")