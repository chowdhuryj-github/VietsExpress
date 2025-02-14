import nbformat
from nbconvert import PythonExporter

# loading the notebook
with open("ExpressTest.ipynb", "r", encoding="utf-8") as f:
    notebook = nbformat.read(f, as_version=4)

# converting to a python script
python_exporter = PythonExporter()
script, _ = python_exporter.from_notebook_node(notebook)

# saving the script
with open("dataset.py", "w", encoding='utf-8') as f:
    f.write(script)

# confirmation message
print("Operation Successful!")