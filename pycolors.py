from tkinter import Tk, filedialog
from PIL import Image
from collections import Counter
from sklearn.cluster import KMeans
import numpy as np


def extract_colors_from_image(image_path, num_colors=20):
    try:
        # Importation de l'image et convertion en matrice RGB de pixels
        image = Image.open(image_path)
        image = image.convert("RGB")
        pixels = list(image.getdata())
        pixel_array = np.array(pixels)
        # Clustering (groupage) des couleurs en num_colors groupe avec l'algorithme
        # du plus proche voisin de Scikit-learn (KMeans)
        kmeans = KMeans(n_clusters=num_colors, random_state=0, n_init=1).fit(
            pixel_array
        )
        # Extraction des centroïdes des clusters.
        # Les centroïdes des clusters sont les couleurs les plus éloignées les unes des autres
        unique_colors = [tuple(map(int, color)) for color in kmeans.cluster_centers_]
        return unique_colors
    except Exception as e:
        return str(e)


def convert_to_css_rgb(colors):
    css_colors = []
    for color in colors:
        css_color = f"rgb({color[0]}, {color[1]}, {color[2]})"
        css_colors.append(css_color)
    return css_colors


def select_image():
    file_path = filedialog.askopenfilename(title="Selectionner une image")
    return file_path


def colors_to_copie(colors):
    tag = ""
    for x in range(len(colors)):
        tag += f'<pre data-prefix="{x+1}"><code style="color:{colors[x]}">{colors[x]}</code></pre>'
    return tag
