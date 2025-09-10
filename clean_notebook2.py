import nbformat

# Chemin vers ton notebook original et le notebook nettoyé
notebook_path = "LangGraph_AppClean.ipynb"
clean_path = "LangGraph_AppClean_GitHub.ipynb"

# Charger le notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Supprimer toute la metadata widgets
for cell in nb.cells:
    if "metadata" in cell and "widgets" in cell.metadata:
        del cell.metadata["widgets"]
    # Supprimer toute metadata d'IPython liée aux widgets
    if "metadata" in cell and "colab" in cell.metadata:
        cell.metadata["colab"].pop("referenced_widgets", None)

# Sauvegarder le notebook nettoyé
with open(clean_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"✅ Notebook prêt pour GitHub : {clean_path}")
