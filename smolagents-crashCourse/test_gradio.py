import gradio as gr

# Función de ejemplo
def greet(name):
    return f"Hello, {name}!"

# Crear la interfaz
interface = gr.Interface(fn=greet, inputs="text", outputs="text")

# Ejecutar la interfaz
interface.launch()

""" 
Running on local URL:  http://127.0.0.1:7860
To create a public link, set `share=True` in launch()
"""