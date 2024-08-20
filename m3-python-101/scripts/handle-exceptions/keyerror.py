usuarios = {'001': 'Marca', '002': 'Mónica', '003': 'Jacob'}
id_usuario = '004'
try:
    print(usuarios[id_usuario])
except KeyError as e:
    print(f"La clave {id_usuario} no está en el diccionario. Añadiendo clave...")
    usuarios[id_usuario] = "Ninguno"
    print(usuarios)