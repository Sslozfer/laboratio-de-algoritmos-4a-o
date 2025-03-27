def mostrar_mensajes(mensajes):
    for mensaje in mensajes:
        print(mensaje)

def enviar_mensajes(mensajes, mensajes_enviados):
    while mensajes:
        mensaje = mensajes.pop(0)
        print(f"Enviando: {mensaje}")
        mensajes_enviados.append(mensaje)