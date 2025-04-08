import gradio as gr
import database as db
import helpers

# Función para mostrar la lista de clientes como DataFrame
def listar_clientes():
    return [[c.dni, c.nombre, c.apellido] for c in db.Clientes.lista]

# Función para buscar cliente
def buscar_cliente(dni):
    cliente = db.Clientes.buscar(dni.upper())
    return f"{cliente}" if cliente else "Cliente no encontrado"

# Función para crear cliente
def crear_cliente(dni, nombre, apellido):
    dni = dni.upper()
    if not helpers.dni_valido(dni, db.Clientes.lista):
        return "DNI inválido o ya existe", listar_clientes()
    if not (2 <= len(nombre) <= 30 and nombre.isalpha()) or not (2 <= len(apellido) <= 30 and apellido.isalpha()):
        return "Nombre o apellido inválidos", listar_clientes()
    db.Clientes.crear(dni, nombre.capitalize(), apellido.capitalize())
    return "Cliente creado correctamente", listar_clientes()

# Función para modificar cliente
def modificar_cliente(dni, nombre, apellido):
    dni = dni.upper()
    cliente = db.Clientes.modificar(dni, nombre.capitalize(), apellido.capitalize())
    return "Cliente modificado" if cliente else "Cliente no encontrado", listar_clientes()

# Función para borrar cliente
def borrar_cliente(dni):
    dni = dni.upper()
    cliente = db.Clientes.borrar(dni)
    return "Cliente borrado" if cliente else "Cliente no encontrado", listar_clientes()

# Interfaz de Gradio
with gr.Blocks(title="Gestor de Clientes") as demo:
    gr.Markdown("# Gestor de Clientes")
    
    # Tabla de clientes
    tabla = gr.Dataframe(headers=["DNI", "Nombre", "Apellido"], value=listar_clientes)
    
    with gr.Row():
        # Buscar
        with gr.Column():
            gr.Markdown("### Buscar Cliente")
            dni_buscar = gr.Textbox(label="DNI (2 nums + 1 letra)")
            buscar_btn = gr.Button("Buscar")
            buscar_output = gr.Textbox(label="Resultado")
            buscar_btn.click(buscar_cliente, inputs=dni_buscar, outputs=buscar_output)
        
        # Crear
        with gr.Column():
            gr.Markdown("### Crear Cliente")
            dni_crear = gr.Textbox(label="DNI")
            nombre_crear = gr.Textbox(label="Nombre")
            apellido_crear = gr.Textbox(label="Apellido")
            crear_btn = gr.Button("Crear")
            crear_output = gr.Textbox(label="Resultado")
            crear_btn.click(crear_cliente, inputs=[dni_crear, nombre_crear, apellido_crear], outputs=[crear_output, tabla])
    
    with gr.Row():
        # Modificar
        with gr.Column():
            gr.Markdown("### Modificar Cliente")
            dni_mod = gr.Textbox(label="DNI")
            nombre_mod = gr.Textbox(label="Nuevo Nombre")
            apellido_mod = gr.Textbox(label="Nuevo Apellido")
            mod_btn = gr.Button("Modificar")
            mod_output = gr.Textbox(label="Resultado")
            mod_btn.click(modificar_cliente, inputs=[dni_mod, nombre_mod, apellido_mod], outputs=[mod_output, tabla])
        
        # Borrar
        with gr.Column():
            gr.Markdown("### Borrar Cliente")
            dni_borrar = gr.Textbox(label="DNI")
            borrar_btn = gr.Button("Borrar")
            borrar_output = gr.Textbox(label="Resultado")
            borrar_btn.click(borrar_cliente, inputs=dni_borrar, outputs=[borrar_output, tabla])

if __name__ == "__main__":
    demo.launch()