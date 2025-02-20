from datetime import datetime

def bienvenida():
    print("¡Bienvenido a Dreams Journeys! Vamos a ayudarte a planificar el viaje perfecto para ti y tu familia.\n")

def crear_usuario():
    print("Registro de Usuario")
    usuario = input("Elige un nombre de usuario: ")
    contrasena = input("Elige una contraseña: ")
    print("Usuario creado exitosamente. Ahora inicia sesión.")
    return usuario, contrasena

def inicio_sesion(usuario_correcto, contrasena_correcta):
    print("Inicio de sesión")
    
    while True:
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")
        
        if usuario == usuario_correcto and contrasena == contrasena_correcta:
            print("Inicio de sesión exitoso.\n")
            return True
        else:
            print("Usuario o contraseña incorrectos. Inténtalo de nuevo.\n")

def obtener_datos_usuario():
    while True:
        try:
            adultos = int(input("¿Cuántos adultos viajan? "))
            ninos = int(input("¿Cuántos niños viajan? "))
            equipaje = int(input("¿Cuántas maletas por persona? "))
            if adultos < 0 or ninos < 0 or equipaje < 0:
                raise ValueError("Los números no pueden ser negativos.")
            return adultos, ninos, equipaje
        except ValueError as e:
            print(f"Error: {e}. Por favor ingresa un valor válido.\n")

def seleccionar_destino():
    destinos = {
        '1': ('Playa', ['Cancun', 'Maldivas', 'Hawái']),
        '2': ('Ciudades', ['Paris', 'Nueva York', 'Roma']),
    }
    
    print("\nElige el tipo de destino:")
    for clave, (categoria, _) in destinos.items():
        print(f"{clave}. {categoria}")
    
    while True:
        opcion = input("Ingresa el número de la categoría que te interesa: ")
        if opcion in destinos:
            categoria_seleccionada, lista_destinos = destinos[opcion]
            print(f"\nHas elegido la categoría: {categoria_seleccionada}")
            print("Los destinos disponibles son:")
            for i, destino in enumerate(lista_destinos, 1):
                print(f"{i}. {destino}")
            while True:
                try:
                    opcion_destino = int(input("Selecciona un destino (número): "))
                    if 1 <= opcion_destino <= len(lista_destinos):
                        return lista_destinos[opcion_destino - 1]
                    else:
                        raise ValueError("Número fuera de rango.")
                except ValueError:
                    print("Error: Selecciona un número válido de la lista.")
        else:
            print("Error: Ingresa una opción válida.")

def obtener_fechas_viaje():
    while True:
        try:
            ida = input("Ingresa la fecha de ida (formato DD/MM/AAAA): ")
            vuelta = input("Ingresa la fecha de vuelta (formato DD/MM/AAAA): ")
            
            formato = "%d/%m/%Y"
            fecha_ida = datetime.strptime(ida, formato)
            fecha_vuelta = datetime.strptime(vuelta, formato)
            
            hoy = datetime.now().date()
            if fecha_ida.date() < hoy:
                print("Error: La fecha de ida no puede ser en el pasado.")
                continue
            if fecha_vuelta <= fecha_ida:
                print("Error: La fecha de vuelta debe ser posterior a la de ida.")
                continue
            
            return ida, vuelta
        except ValueError:
            print("Error: Ingresa las fechas en el formato correcto (DD/MM/AAAA).\n")

def sugerir_alojamiento(destino):
    alojamientos = {
        'Cancun': [('Hotel Playa', 100), ('Resort Cancún', 200),('Sunset Beach Hotel', 180)],
        'París': [('Hotel Parisien', 150), ('Luxury Paris', 250), ('Eiffel Tower View', 230)],
        'Nueva York': [('NY Grand Hotel', 180), ('Central Park Suites', 300), ('Times Square Hotel', 280)],
        'Maldivas': [('Maldivas Paradise', 400), ('Ocean View Resort', 350),('Blue Lagoon Retreat', 370)],
        'Hawái': [('Aloha Resort', 250), ('Beachside Villas', 220),('Tropical Haven Resort', 260)],
        'Roma': [('Colosseum Inn', 200), ('Historic Rome Suites', 270),('Vatican Boutique Hotel',240)]
    }
    
    opciones = alojamientos.get(destino, [])
    if not opciones:
        print(f"No hay opciones de alojamiento para el destino: {destino}")
        return None
    
    print("\nOpciones de alojamiento:")
    for i, (nombre, precio) in enumerate(opciones, 1):
        print(f"{i}. {nombre} - ${precio} por noche")
    
    while True:
        try:
            opcion = int(input(f"Elige un alojamiento (1-{len(opciones)}): "))
            if opcion < 1 or opcion > len(opciones):
                raise ValueError("Opción no válida.")
            nombre, precio = opciones[opcion - 1]
            return nombre, precio
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")

def gestionar_transporte():
    opciones = ['Vuelo', 'Transporte local']
    print("\nElige el tipo de transporte:")
    for idx, opcion in enumerate(opciones, 1):
        print(f"{idx}. {opcion}")
    
    while True:
        try:
            opcion = int(input("Ingresa el número de la opción que prefieres: "))
            if opcion < 1 or opcion > len(opciones):
                raise ValueError("Opción no válida.")
            transporte_seleccionado = opciones[opcion - 1]
            return transporte_seleccionado
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")

def sugerir_actividades(destino, adultos, ninos):
    actividades = {
        'Cancun': [('Snorkel', 50), ('Parques temáticos', 100),('Paseo en catamarán', 80)],
        'Maldivas': [('Buceo', 150), ('Excursiones privadas', 200),('Pesca nocturna', 130)],
        'Hawái': [('Senderismo', 40), ('Surf', 60),('Paseo en helicóptero', 250)],
        'París': [('Tour Eiffel', 30), ('Museos', 40),('Crucero por el Sena', 50)],
        'Nueva York': [('Broadway', 120), ('Central Park', 0), ('Mirador Empire State', 45)],
        'Roma': [('Coliseo', 25), ('Visita guiada', 50),('Catacumbas de Roma',35)]
    }
    
    actividades_seleccionadas = actividades.get(destino, [])
    if not actividades_seleccionadas:
        print(f"No hay actividades disponibles para el destino: {destino}")
        return []
    
    print("\nActividades sugeridas:")
    for i, (actividad, precio) in enumerate(actividades_seleccionadas, 1):
        print(f"{i}. {actividad} - ${precio} por persona")
    
    seleccion_actividades = []
    while True:
        try:
            seleccion = input(f"Selecciona actividades (separa con comas, ej. 1,2): ")
            seleccion = [int(x) for x in seleccion.split(',')]
            if any(i < 1 or i > len(actividades_seleccionadas) for i in seleccion):
                raise ValueError("Selección inválida.")
            seleccion_actividades = [actividades_seleccionadas[i - 1] for i in seleccion]
            break
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")
    
    return seleccion_actividades

def ver_resumen(destino, alojamiento, transporte, actividades, adultos, ninos, noches, equipaje):
    print("\nResumen de tu viaje:")
    print(f"Destino: {destino}")
    
    if alojamiento:
        print(f"Alojamiento: {alojamiento[0]} - ${alojamiento[1]} por noche")
    else:
        print("No se seleccionó alojamiento.")

    print(f"Transporte: {transporte}")
    
    if actividades:
        costo_actividades = sum([actividad[1] for actividad in actividades])  # Sumar el costo de actividades
        print(f"Actividades: {', '.join([actividad[0] for actividad in actividades])} - ${costo_actividades} por persona")
    else:
        print("No se seleccionaron actividades.")
    
    # Cálculos
    # Costo de alojamiento: El adulto paga el costo completo y el niño la mitad
    costo_alojamiento_adultos = alojamiento[1] * noches * adultos
    costo_alojamiento_ninos = (alojamiento[1] * 0.5) * noches * ninos  # Niños pagan la mitad
    costo_alojamiento = costo_alojamiento_adultos + costo_alojamiento_ninos
    
    # Costo de actividades
    costo_actividades = sum([actividad[1] for actividad in actividades]) * adultos  # Solo adultos pagan el precio completo
    if ninos > 0:
        costo_actividades += sum([actividad[1] * 0.5 for actividad in actividades]) * ninos  # Los niños pagan la mitad
    
    # Costo de maletas
    costo_maletas = equipaje * 60 * (adultos + ninos)  # Las maletas cuestan 60 por persona

    # Cálculo total
    costo_total = costo_alojamiento + costo_actividades + costo_maletas

    print(f"\nCosto estimado total: ${costo_total:.2f}")



def menu():
    usuario = ""
    contrasena = ""
    bienvenida()
    while True:
        print("\n--- Menú ---")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            if usuario and contrasena:
                if inicio_sesion(usuario, contrasena):
                    return True
            else:
                print("Primero debes registrarte.")
        elif opcion == "2":
            usuario, contrasena = crear_usuario()
        elif opcion == "3":
            print("Gracias por usar Dreams Journeys. Hasta pronto!")
            return False
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def main():
    if menu():
        bienvenida()
        adultos, ninos, equipaje = obtener_datos_usuario()  # Aquí ya obtienes el valor de equipaje
        destino = seleccionar_destino()
        ida, vuelta = obtener_fechas_viaje()

        # Calcular el número de noches del viaje
        formato = "%d/%m/%Y"
        fecha_ida = datetime.strptime(ida, formato)
        fecha_vuelta = datetime.strptime(vuelta, formato)
        noches = (fecha_vuelta - fecha_ida).days  # Calcula la cantidad de noches

        alojamiento = sugerir_alojamiento(destino)
        transporte = gestionar_transporte()
        actividades = sugerir_actividades(destino, adultos, ninos)

        # Pasamos todos los argumentos a la función ver_resumen
        ver_resumen(destino, alojamiento, transporte, actividades, adultos, ninos, noches, equipaje)
main()
