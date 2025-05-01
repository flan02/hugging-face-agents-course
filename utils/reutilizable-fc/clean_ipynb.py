# pip install nbformat

import nbformat

def clean_notebook(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    for cell in nb.cells:
        if "outputs" in cell:
            cell["outputs"] = []
        if "execution_count" in cell:
            cell["execution_count"] = None

    with open(file_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

clean_notebook("ruta/a/tu_archivo.ipynb")

# | Run the script
# python clean_ipynb.py


