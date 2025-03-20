pizzas = ["margarita" , "capresse" , "de salamin"]
for i in pizzas:
    print("la pizza" , i , " es la mejor")
print("las pizzas me gustan mucho, tanto a la piedra como al molde, todas las pizzas me gustan muchisimo, pero si tendria que elegir una lo haria dependiendo de mi estado de animo, si me ciento feliz me elijo una capresse, si me siento triste una de salamin y si estoy con mucha hambre me elijo una margarita, en fin ¡Que ricas las pizzas!")

pizzas_amigo = pizzas[:]
pizzas.append("palmitos")
pizzas_amigo.append("fugazetta")
print("Mis pizzas favoritas son:", ", ".join([i for i in pizzas]))
print("Las pizzas favoritas de mis amigos son:", ", ".join([i for i in pizzas_amigo]))