from flask import Flask, render_template, request, jsonify
from pycolors import *
import webview

app = Flask(__name__)
window = webview.create_window("Mes couleurs", app)


@app.route("/")
def hello_world():
    return render_template("index.html")


# Selectionner couleur
@app.route("/selectColors", methods=["POST"])
def executer_fonction():
    file_path = select_image()
    if not file_path:
        print("Aucune image selectionnée.")
        return
    colors = extract_colors_from_image(file_path)
    colorRgb = convert_to_css_rgb(colors)
    colorsCode = colors_to_copie(colorRgb)
    return jsonify({"result": colorRgb, "colorscode": colorsCode})


if __name__ == "__main__":
    # app.run(debug=True)
    webview.start()
