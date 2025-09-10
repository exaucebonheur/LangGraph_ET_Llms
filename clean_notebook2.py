import nbformat

# Charger le notebook avec encodage UTF-8
with open("LangGraph_App.ipynb", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Supprimer toutes les métadonnées liées aux widgets
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

# Supprimer les métadonnées de chaque cellule
for cell in nb.cells:
    if "metadata" in cell and "widgets" in cell.metadata:
        del cell.metadata["widgets"]

# Sauvegarder dans un nouveau fichier
with open("LangGraph_AppClean.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("Notebook nettoyé et sauvegardé sous LangGraph_App.ipynb")
