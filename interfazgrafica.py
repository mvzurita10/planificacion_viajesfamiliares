import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, date, timedelta

root = tk.Tk()

destinos = {"Playa": ["Cancún", "Maldivas", "Hawái"], "Ciudades": ["París", "Nueva York", "Roma"]}

alojamientos = {
    'Cancún': [('Hotel Playa', 100), ('Resort Cancún', 200), ('Sunset Beach Hotel', 180)],
    'París': [('Hotel Parisien', 150), ('Luxury Paris', 250), ('Eiffel Tower View', 230)],
    'Nueva York': [('NY Grand Hotel', 180), ('Central Park Suites', 300), ('Times Square Hotel', 280)],
    'Maldivas': [('Maldivas Paradise', 400), ('Ocean View Resort', 350), ('Blue Lagoon Retreat', 370)],
    'Hawái': [('Aloha Resort', 250), ('Beachside Villas', 220), ('Tropical Haven Resort', 260)],
    'Roma': [('Colosseum Inn', 200), ('Historic Rome Suites', 270), ('Vatican Boutique Hotel', 240)]
}

transporte = [('Vuelo', 500), ('Transporte local', 100)]

actividades = {
    'Cancún': [('Snorkel', 50), ('Parques temáticos', 100), ('Paseo en catamarán', 80)],
    'Maldivas': [('Buceo', 150), ('Excursiones privadas', 200), ('Pesca nocturna', 130)],
    'Hawái': [('Senderismo', 40), ('Surf', 60), ('Paseo en helicóptero', 250)],
    'París': [('Tour Eiffel', 30), ('Museos', 40), ('Crucero por el Sena', 50)],
    'Nueva York': [('Broadway', 120), ('Central Park', 0), ('Mirador Empire State', 45)],
    'Roma': [('Coliseo', 25), ('Visita guiada', 50), ('Catacumbas de Roma', 35)]
}

# Inicializa el diccionario de usuarios (se cargará desde un archivo si existe)
usuarios = {}

data = {"Registro": {"Adultos": 0, "Niños": 0, "Maletas": 0},
        "Destino": {"Lugar": "", "Ida": "", "Regreso": ""},
        "Alojamiento": "", "Transporte": "", "Actividades": []}

def resize_image(imagen, max_width=150, max_height=200):
    original_width = imagen.width()
    original_height = imagen.height()
    aspect_ratio = original_width / original_height

    if original_width > original_height:
        new_width = min(max_width, original_width)
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = min(max_height, original_height)
        new_width = int(new_height * aspect_ratio)

    resized_img = imagen.subsample(
        max(1, original_width // new_width),  # Evitar dividir por 0
        max(1, original_height // new_height)
    )
    return resized_img

def limpiar_ventana():
    for widget in root.winfo_children():
        widget.destroy()

def guardar_usuarios(usuario, contraseña, correo):
    """Guarda la información del usuario en el diccionario y muestra un mensaje."""
    usuarios[usuario] = {"contraseña": contraseña, "correo": correo}
    print(f"Usuario registrado con éxito: {usuarios}")
    messagebox.showinfo("Éxito", "Usuario registrado con éxito.")  # Usar messagebox para mostrar el éxito

def inicio_sesion():
    global Fondo
    limpiar_ventana()
    root.geometry("400x400+550+100")
    root.title("Dreams Journeys")
    
    Fondo = tk.PhotoImage(file="./imgs/FondoPP.png")
    lblFondo = tk.Label(root, image=Fondo)
    lblFondo.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    
    lblBievenida = tk.Label(root, text="✨Dreams Journeys✨", font=("Arial", 26,"bold"), fg="#1b639e", bg="white")
    lblBievenida.place(relx=0.5 , rely=0.13, anchor="center")
    
    lbliniciosecion = tk.Label(root, text="Inicio de sesion", font=("Arial", 16), bg="white")
    lbliniciosecion.place(relx=0.5, rely=0.29, anchor="center")
    
    lblNuevo_usuario = tk.Label(root, text="Usuario: ", bg="white", font=("calibri", 14))
    lblNuevo_usuario.place(relx=0.5, rely=0.39, anchor="center")
    txtusuario = ttk.Entry(root)
    txtusuario.place(relx=0.5, rely=0.44, anchor="center")
    
    lblNueva_contraseña = tk.Label(root, text="Contraseña:", bg="white",font=("calibri", 14))
    lblNueva_contraseña.place(relx=0.5, rely=0.54, anchor="center")
    txtcontraseña = ttk.Entry(root, show="*")
    txtcontraseña.place(relx=0.5, rely=0.59, anchor="center")
    
    lblError = tk.Label(root, text="", fg="Red", bg="white")
    lblError.place(relx=0.5, rely=0.7, anchor="center")
    
    def validar_inicio():
        usuario = txtusuario.get()
        contraseña = txtcontraseña.get()
        
        if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña:
            planificacion(usuario)
        else:
            lblError.config(text="Usuario o contraseña INCORRECTOS.",fg="Red")
    
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("RedButton.TButton",font=('Arial', 11,'bold'),foreground="white",background="red",borderwidth=2,relief="solid")
    style.map("RedButton.TButton",background=[('active', 'darkred'), ('!active', 'red')],foreground=[('disabled', 'gray')])
    style.configure("GreenButton.TButton", font=('Arial', 11,'bold'), foreground="white", background="green", borderwidth=2, relief="solid")
    style.map("GreenButton.TButton", background=[('active', 'darkgreen'), ('!active', 'green')], foreground=[('disabled', 'gray')])
    
    btnEntrar = ttk.Button(root, text="Entrar", command=validar_inicio, style="GreenButton.TButton")
    btnEntrar.place(relx=0.35, rely=0.84, anchor="center")
    
    btnVolver = ttk.Button(root, text="Volver", command=pantallaInicio, style="RedButton.TButton")
    btnVolver.place(relx=0.65, rely=0.84, anchor="center")
    
    lblEmpresa = tk.Label(root, text="By: MIKVA")
    lblEmpresa.place(relx=0.85, rely=0.95, anchor="center")
    
def registro_Usuarios():
    global Fondo
    limpiar_ventana()
    root.geometry("400x400+550+100")
    root.title("Dreams Journeys")
    
    Fondo = tk.PhotoImage(file="./imgs/FondoPP.png")
    lblFondo = tk.Label(root, image=Fondo)
    lblFondo.place(x=0, y=0, relwidth=1, relheight=1)
    
    lblBievenida = tk.Label(root, text="✨Dreams Journeys✨", font=("Arial", 26, "bold"), fg="#1b639e", bg="white")
    lblBievenida.place(relx=0.5, rely=0.1, anchor="center")
    
    lblRegistrarse = tk.Label(root, text="Registrarse", font=("Arial", 16, "underline"), bg="white")
    lblRegistrarse.place(relx=0.5, rely=0.22, anchor="center")
    
    lblNuevo_usuario = tk.Label(root, text="Nuevo Usuario: ", bg="white", font=("calibri", 13))
    lblNuevo_usuario.place(relx=0.5, rely=0.3, anchor="center")
    txtusuario = ttk.Entry(root)
    txtusuario.place(relx=0.5, rely=0.35, anchor="center")
    
    lblNP = tk.Label(root, text="Nombre y Apellido: ", bg="white", font=("calibri", 13))
    lblNP.place(relx=0.5, rely=0.42, anchor="center")
    txtNom = ttk.Entry(root)
    txtNom.place(relx=0.5, rely=0.47, anchor="center")
    
    lblCorreo = tk.Label(root, text="Correo: ", bg="white", font=("calibri", 13))
    lblCorreo.place(relx=0.5, rely=0.54, anchor="center")
    txtcorreo = ttk.Entry(root)
    txtcorreo.place(relx=0.5, rely=0.59, anchor="center")
    
    lblNueva_contraseña = tk.Label(root, text="Nueva Contraseña:", bg="white", font=("calibri", 13))
    lblNueva_contraseña.place(relx=0.5, rely=0.66, anchor="center")
    txtcontraseña = ttk.Entry(root, show="*")
    txtcontraseña.place(relx=0.5, rely=0.71, anchor="center")
    
    # Funciones de validación dentro de la función principal
    def validar_nombre(nombre):
        # Solo letras y espacios
        if re.match("^[A-Za-z\s]+$", nombre):
            return True
        else:
            return False

    def validar_correo(correo):
        # Expresión regular para correo electrónico
        if re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            return True
        else:
            return False

    def validar_contraseña(contraseña):
        # Asegurarse de que la contraseña tenga al menos 6 caracteres
        if len(contraseña) >= 6:
            return True
        else:
            return False

    # Función para guardar el usuario
    def guardar_usuario():  # Corregido el nombre de la función
        usuario = txtusuario.get()
        contraseña = txtcontraseña.get()
        correo = txtcorreo.get()
        nombre = txtNom.get()

        # Validaciones
        if not usuario:
            messagebox.showerror("Error", "El campo 'Usuario' no puede estar vacío.")
            return
        if not validar_nombre(nombre):
            messagebox.showerror("Error", "El nombre debe contener solo letras y espacios.")
            return
        if not validar_correo(correo):
            messagebox.showerror("Error", "El correo no es válido.")
            return
        if not validar_contraseña(contraseña):
            messagebox.showerror("Error", "La contraseña debe tener al menos 6 caracteres.")
            return

        # Aquí deberías agregar el código para guardar los datos del usuario en tu sistema
        guardar_usuarios(usuario, contraseña, correo)  # Llama a la función guardar_usuarios
        pantallaInicio()

    # Estilo para los botones
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("RedButton.TButton", font=('Arial', 11, 'bold'), foreground="white", background="red", borderwidth=2, relief="solid")
    style.map("RedButton.TButton", background=[('active', 'darkred'), ('!active', 'red')], foreground=[('disabled', 'gray')])
    style.configure("GreenButton.TButton", font=('Arial', 11, 'bold'), foreground="white", background="green", borderwidth=2, relief="solid")
    style.map("GreenButton.TButton", background=[('active', 'darkgreen'), ('!active', 'green')], foreground=[('disabled', 'gray')])

    btnGuardar = ttk.Button(root, text="Guardar", command=guardar_usuario, style="GreenButton.TButton")
    btnGuardar.place(relx=0.35, rely=0.84, anchor="center")
    
    btnVolver = ttk.Button(root, text="Volver", command=pantallaInicio, style="RedButton.TButton")
    btnVolver.place(relx=0.65, rely=0.84, anchor="center")
    
    lblEmpresa = tk.Label(root, text="By: MIKVA", bg="white")
    lblEmpresa.place(relx=0.85, rely=0.95, anchor="center")


def planificacion(usuario):
    global logo, nuevo_Logo, Fondo
    limpiar_ventana()
    root.geometry("1200x700+175+50")
    
    Fondo = tk.PhotoImage(file="./imgs/FondoVP.png")
    lblFondo = tk.Label(root, image=Fondo)
    lblFondo.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    
    logo = tk.PhotoImage(file="./imgs/logo_miky.png")
    nuevo_Logo = resize_image(logo)
    lblLogo = tk.Label(root, image=nuevo_Logo, bg="white")
    lblLogo.place(relx=0.5, rely=0.1, anchor="center")
    
    lblBievenida = tk.Label(root, text="✨Dreams Journeys✨", font=("Arial", 36,"bold"), fg="#1b639e", bg="white")
    lblBievenida.place(relx=0.5, rely=0.25, anchor="center")
    
    def validate_date(date_str):
        try:
            datetime.strptime(date_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def calcular_costo_alojamiento(dias_estadia, alojamiento_seleccionado):
        """Calcula el costo total del alojamiento."""
        try:
            precio_por_noche = float(alojamiento_seleccionado.split('$')[1])
            return dias_estadia * precio_por_noche
        except (IndexError, ValueError):
            return 0.0

    def calcular_costo_transporte(transporte_seleccionado):
        """Calcula el costo del transporte."""
        try:
            costo_transporte = float(transporte_seleccionado.split('$')[1])
            return costo_transporte
        except (IndexError, ValueError):
            return 0.0

    def calcular_costo_actividades():
         """Calcula el costo total de las actividades seleccionadas."""
         costo_total = 0
         for act, (var, precio) in actividades_vars.items():
            if var.get():
                costo_total += precio
         return costo_total

    # Funciones para mostrar secciones
    def show_section(section):
        global current_section
        current_section = section
        for widget in content_frame.winfo_children():
            widget.destroy()

        tk.Label(content_frame, text=f"Sección: {section}", font=("Arial", 14), bg="white").pack(pady=10)
        global message_label
        message_label = tk.Label(content_frame, text="", fg="red", font=("Arial", 10), bg="white")
        message_label.pack(pady=5)

        if section == "Registro":
            for key in ["Adultos", "Niños", "Maletas"]:
                frame = tk.Frame(content_frame)
                frame.pack(pady=5)
                tk.Label(frame, text=f"{key}:", bg="white").pack(side="left")
                tk.Entry(frame, textvariable=entry_vars[key]).pack(side="right")

        elif section == "Destino":
            tk.Label(content_frame, text="Selecciona tipo de destino:", bg="white").pack(pady=5)
            global tipo_destino_box, lugar_box
            tipo_destino_box = ttk.Combobox(content_frame, values=list(destinos.keys()))
            tipo_destino_box.pack(pady=5)
            tipo_destino_box.bind("<<ComboboxSelected>>", update_destinos)

            tk.Label(content_frame, text="Lugar:", bg="white").pack()
            lugar_box = ttk.Combobox(content_frame)
            lugar_box.pack(pady=5)

            tk.Label(content_frame, text="Fecha de ida (DD/MM/AAAA):", bg="white").pack()
            tk.Entry(content_frame, textvariable=entry_vars["Ida"]).pack()

            tk.Label(content_frame, text="Fecha de regreso (DD/MM/AAAA):", bg="white").pack()
            tk.Entry(content_frame, textvariable=entry_vars["Regreso"]).pack()

        elif section == "Alojamiento":
            destino_seleccionado = data["Destino"]["Lugar"]
            if destino_seleccionado in alojamientos:
                opciones_alojamiento = [f"{nombre} - ${precio}" for nombre, precio in alojamientos[destino_seleccionado]]
                tk.Label(content_frame, text=f"Alojamientos en {destino_seleccionado}:", bg="white").pack(pady=5)
                global alojamiento_selection
                alojamiento_selection = ttk.Combobox(content_frame, values=opciones_alojamiento)
                alojamiento_selection.pack(pady=5)
            else:
                tk.Label(content_frame, text="No hay alojamientos disponibles para este destino.", bg="white").pack()

        elif section == "Transporte":
            opciones_transporte = [f"{tipo} - ${costo}" for tipo, costo in transporte]
            tk.Label(content_frame, text="Selecciona el transporte:", bg="white").pack(pady=5)
            global transporte_selection
            transporte_selection = ttk.Combobox(content_frame, values=opciones_transporte)
            transporte_selection.pack(pady=5)

        elif section == "Actividades":
            destino = data["Destino"]["Lugar"]
            if destino in actividades:
                tk.Label(content_frame, text=f"Actividades en {destino}:", bg="white").pack(pady=5)
                global actividades_vars
                actividades_vars = {}
                for act, precio in actividades[destino]:
                    var = tk.BooleanVar()
                    chk = ttk.Checkbutton(content_frame, text=f"{act} - ${precio}", variable=var, style="Custom.TCheckbutton")
                    chk.pack(anchor="center")
                    actividades_vars[act] = (var, precio)
            else:
                tk.Label(content_frame, text="No hay actividades disponibles para este destino.", bg="white").pack()

        ttk.Button(content_frame, text="Guardar", command=save_data).pack(pady=10)
        style = ttk.Style()
        style.theme_use("vista")
        style.configure("Custom.TCheckbutton", background="white")

    # Actualizar destinos según selección
    def update_destinos(event):
        tipo = tipo_destino_box.get()
        lugares = destinos.get(tipo, [])
        lugar_box['values'] = lugares
        if lugares:
            lugar_box.current(0)

    # Guardar datos
    def save_data():
        global ida_dt, regreso_dt  # Declarar como globales

        if current_section == "Registro":
            try:
                data["Registro"] = {key: int(entry_vars[key].get()) for key in ["Adultos", "Niños", "Maletas"]}
                message_label.config(text="Registro guardado correctamente", fg="green", bg="white")
            except ValueError:
                message_label.config(text="Error: Ingrese solo números en los campos", fg="red", bg="white")

        elif current_section == "Destino":
            lugar = lugar_box.get()
            ida_str = entry_vars["Ida"].get()
            regreso_str = entry_vars["Regreso"].get()

            if lugar and validate_date(ida_str) and validate_date(regreso_str):
                ida_dt = datetime.strptime(ida_str, "%d/%m/%Y").date()
                regreso_dt = datetime.strptime(regreso_str, "%d/%m/%Y").date()
                tomorrow = date.today() + timedelta(days=1)

                if ida_dt < tomorrow:
                    message_label.config(text="Error: La fecha de ida debe ser a partir de mañana.", fg="red", bg="white")
                    return

                if regreso_dt <= ida_dt:
                    message_label.config(text="Error: La fecha de regreso debe ser posterior a la de ida", fg="red", bg="white")
                    return

                data["Destino"] = {"Lugar": lugar, "Ida": ida_str, "Regreso": regreso_str}
                message_label.config(text="Destino guardado correctamente", fg="green", bg="white")
            else:
                message_label.config(text="Error: Completa todos los campos correctamente", fg="red", bg="white")

        elif current_section == "Alojamiento":
            selected = alojamiento_selection.get()
            if selected:
                data["Alojamiento"] = selected
                message_label.config(text="Alojamiento guardado correctamente", fg="green", bg="white")
            else:
                message_label.config(text="Error: Debes seleccionar un alojamiento", fg="red", bg="white")

        elif current_section == "Transporte":
            selected = transporte_selection.get()
            if selected:
                data["Transporte"] = selected
                message_label.config(text="Transporte guardado correctamente", fg="green", bg="white")
            else:
                message_label.config(text="Error: Debes seleccionar un transporte", fg="red", bg="white")

        elif current_section == "Actividades":
            selected_activities = [act for act, (var, _) in actividades_vars.items() if var.get()]
            if selected_activities:
                data["Actividades"] = selected_activities
                message_label.config(text="Actividades guardadas correctamente", fg="green", bg="white")
            else:
                message_label.config(text="Error: Selecciona al menos una actividad", fg="red", bg="white")

    # Mostrar resumen
    def show_summary():
        for widget in content_frame.winfo_children():
            widget.destroy()

        tk.Label(content_frame, text="Resumen del Viaje", font=("Arial", 10, "bold"), bg="white").pack(pady=5)

        #Extraer datos del diccionarios
        adultos = data['Registro']['Adultos']
        niños = data['Registro']['Niños']
        maletas = data['Registro']['Maletas']
        lugar = data['Destino']['Lugar']
        ida_str = data['Destino']['Ida']
        regreso_str = data['Destino']['Regreso']
        alojamiento_seleccionado = data["Alojamiento"]
        transporte_seleccionado = data["Transporte"]
        actividades_seleccionadas = data["Actividades"]

        def add_summary_section(title, content, color, bold=False, font_size=11):  # Agregado parámetros bold y font_size
            section_frame = tk.Frame(content_frame, bg="white")
            section_frame.pack(pady=3)
            font_style = ("Arial", 10, "bold") if bold else ("Arial", 10)  # Estilo con o sin negrita
            tk.Label(section_frame, text=title, font=font_style, fg=color, bg="white").pack()
            tk.Label(section_frame, text=content, font=("Arial", font_size), bg="white").pack()  # Usar font_size

        add_summary_section("Registro", f"Adultos: {adultos}, Niños: {niños}, Maletas: {maletas}","blue")
        add_summary_section("Destino", f"Lugar: {lugar}\nIda: {ida_str}\nRegreso: {regreso_str}","green")
        add_summary_section("Alojamiento", alojamiento_seleccionado,"blue")
        add_summary_section("Transporte", transporte_seleccionado,"green")
        add_summary_section("Actividades", ", ".join(actividades_seleccionadas),"blue")

        # Calculo de precios
        ida_dt = datetime.strptime(ida_str, "%d/%m/%Y").date()
        regreso_dt = datetime.strptime(regreso_str, "%d/%m/%Y").date()
        dias_estadia = (regreso_dt - ida_dt).days
        
        costo_alojamiento = calcular_costo_alojamiento(dias_estadia, alojamiento_seleccionado)
        costo_transporte = calcular_costo_transporte(transporte_seleccionado)
        costo_actividades = calcular_costo_actividades()
        costo_adultos = adultos * 200  # Ejemplo: $200 por adulto
        costo_niños = niños * 100  # Ejemplo: Mitad del precio de adulto
        
        total = costo_alojamiento + costo_transporte + costo_actividades + costo_adultos + costo_niños

        add_summary_section("Total a pagar", f"${total:.2f}", "red", bold=True, font_size=14)
    
    content_frame = tk.Frame(root, bg="white",  bd=5, relief="solid")
    content_frame.place(relx=0.35, rely=0.32, width=400, height=400) 


    initial_message = tk.Label(content_frame, text="Selecciona una opción", font=("Arial", 14), bg="white")
    initial_message.pack(pady=20)

    entry_vars = {"Adultos": tk.StringVar(), "Niños": tk.StringVar(), "Maletas": tk.StringVar(), "Ida": tk.StringVar(), "Regreso": tk.StringVar()}
    
    style = ttk.Style()
    style.theme_use("vista")
    style.configure("Custom.TButton",font=("Arial", 10,"bold"),padding=5,foreground="black") #, style="Custom.TButton"
    
    #Registro
    frMarcoR = tk.Frame(root, bd=2, relief="solid", bg="white")
    frMarcoR.place(relx=0.2, rely=0.4, anchor="center", width=100, height=40)
    bntRegistro = ttk.Button(root, text="Registro", command=lambda: show_section("Registro"), style="Custom.TButton")
    bntRegistro.place(relx=0.2, rely=0.4, anchor="center")
    
    #Destino
    frMarcoD = tk.Frame(root, bd=2, relief="solid", bg="white")
    frMarcoD.place(relx=0.2,rely=0.48, anchor="center",  width=100, height=40)
    bntRegistro = ttk.Button(root, text="Destino", command=lambda: show_section("Destino"), style="Custom.TButton")
    bntRegistro.place(relx=0.2,rely=0.48, anchor="center")
    
    #Alojamiento
    frMarcoA = tk.Frame(root, bd=2, relief="solid", bg="white")
    frMarcoA.place(relx=0.2,rely=0.56, anchor="center",  width=100, height=40)
    bntRegistro = ttk.Button(root, text="Alojamiento", command=lambda: show_section("Alojamiento"), style="Custom.TButton")
    bntRegistro.place(relx=0.2,rely=0.56, anchor="center")
    
    #Transporte
    frMarcoT = tk.Frame(root, bd=2, relief="solid", bg="white")
    frMarcoT.place(relx=0.2,rely=0.64, anchor="center",  width=100, height=40)
    bntRegistro = ttk.Button(root, text="Transporte", command=lambda: show_section("Transporte"), style="Custom.TButton")
    bntRegistro.place(relx=0.2,rely=0.64, anchor="center")
    
    #Actividades
    frMarcoAc = tk.Frame(root, bd=2, relief="solid", bg="white")
    frMarcoAc.place(relx=0.2,rely=0.72, anchor="center",  width=100, height=40)
    bntRegistro = ttk.Button(root, text="Actividades", command=lambda: show_section("Actividades"), style="Custom.TButton")
    bntRegistro.place(relx=0.2,rely=0.72, anchor="center")
    
    #Finalizar y ver resumen
    frMarcoF = tk.Frame(root, bd=1, relief="solid", bg="red")
    frMarcoF.place(relx=0.5,rely=0.95, anchor="center",  width=178, height=43)
    bntRegistro = ttk.Button(root, text="Finalizar y ver resumen", command=lambda: (show_summary(),reservacion(usuario)), style="Custom.TButton")
    bntRegistro.place(relx=0.5,rely=0.95, anchor="center")
    
    #Mensaje de Reserva guardada
    def reservacion(usuario):
        correo_usuario = usuarios[usuario]["correo"]
        frPago = tk.Frame(root, bd=2, relief="solid", bg="white")
        frPago.place(relx=0.85,rely=0.75, anchor="center", width=350, height=200)
        
        lblReserva =tk.Label(root,text="Su reserva a sido guardada con éxito.",font=("calibri",16,"bold","underline"), bg="white", fg="green")
        lblReserva.place(relx=0.85,rely=0.64, anchor="center")
        
        lblPago = tk.Label(root, text="Para retirar sus boletos y proceder con el pago\nacérquese a nuestras oficinas.",font=("calibri",12), bg="white")
        lblPago.place(relx=0.85,rely=0.71, anchor="center")
        
        lblInfo = tk.Label(root, text="Se le enviara mas informacion al correo registrado\ny el registro de su viaje",font=("calibri",12), bg="white")
        lblInfo.place(relx=0.85,rely=0.78, anchor="center")
        
        lblcorreo = tk.Label(root,text=f"Correo registrado:\n{correo_usuario}",font=("calibri",12), bg="white")
        lblcorreo.place(relx=0.85,rely=0.85, anchor="center")
    
    
    frMarcoS = tk.Frame(root, bd=1, relief="solid", bg="red")
    frMarcoS.place(relx=0.90,rely=0.95, anchor="center",  width=100, height=35)
    ttk.Button(root, text="Salir", command=quit).place(relx=0.90,rely=0.95, anchor="center")

def pantallaInicio():
    limpiar_ventana()
    global Fondo, logo, nuevo_Logo
    root.title("Dreams Journeys")
    root.geometry("800x500+450+75")
    root.config(bg="white")
    
    style = ttk.Style()
    style.theme_use("vista")
    style.configure("Custom.TButton",font=("Arial", 10,"bold"),padding=5,foreground="black")
    
    Fondo = tk.PhotoImage(file="./imgs/FondoPP.png")
    lblFondo = tk.Label(root, image=Fondo)
    lblFondo.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    logo = tk.PhotoImage(file="./imgs/logo_miky.png")
    nuevo_Logo = resize_image(logo)
    lblLogo = tk.Label(root, image=nuevo_Logo, bg="white")
    lblLogo.place(relx=0.5, rely=0.1, anchor="center")

    lblBievenida = tk.Label(root, text="✨Dreams Journeys✨", font=("Arial", 36,"bold"), fg="#1b639e", bg="white")
    lblBievenida.place(relx=0.5, rely=0.3, anchor="center")

    lblIntro = tk.Label(root, text="Tu proximo destino \n     empieza aqui 🛩️ ", font=("Calibri",16), bg="white")
    lblIntro.place(relx=0.5, rely=0.45, anchor="center")

    frame_label = tk.Frame(root, bd=5, relief="solid", bg="black")
    frame_label.place(relx=0.5, rely=0.65, anchor="center", width=600, height=80)

    lblIntro2 = tk.Label(frame_label, text="Dreams Journeys te ayuda a organizar viajes inolvidables con tu familia, \ndesde la elección del destino hasta la planificación del itinerario perfecto. \n¡Prepárate para vivir momentos inolvidables con quienes más quieres! ✈️", bg="white", font=("calibri", 14))
    lblIntro2.place(relx=0.5, rely=0.5, anchor="center")

    btnIniciarsesion = tk.Button(root, text="Iniciar Sesion", command=inicio_sesion ,font=("calibri", 12,"underline","bold"), bg="green", fg="white")
    btnIniciarsesion.place(relx=0.4, rely=0.80, anchor="center", width=100, height=35)

    btnRegistrarse = tk.Button(root, text="Registrarse", command=registro_Usuarios ,font=("calibri", 12,"underline","bold"), bg="green", fg="white")
    btnRegistrarse.place(relx=0.6, rely=0.80, anchor="center", width=100, height=35)

    btnSalir = tk.Button(root, text="Salir", command=quit, font=("calibri", 12,"underline", "bold"), bg="red", fg="white")
    btnSalir.place(relx=0.5, rely=0.90, anchor="center", width=80, height=35)
    
pantallaInicio()

root.mainloop()