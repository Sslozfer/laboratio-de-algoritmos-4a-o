numeros = []
numerito = 1 
nomillon = True
while nomillon:
    numeros.append(numerito)
    if numerito == 1000000:
        nomillon = False
    numerito += 1
print(min(numeros) , "es el minimo y" , max(numeros) , "es el maximo")
print(sum(numeros)) 