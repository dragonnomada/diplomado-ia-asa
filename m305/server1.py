from flask import Flask
from flask import request
from flask import send_file

import pandas

import matplotlib

matplotlib.use("Agg")

from matplotlib import pyplot
import seaborn

import io

# --- DATOS ---

titanic = pandas.read_csv("./conjuntos/titanic.csv")

# --- SERVIDOR ---

app = Flask(__name__)

@app.get("/") # text/plain
def main():
    return send_file("ui/index.html")

@app.get("/datos/titanic") # application/json
def datos_titanic():
    columns = request.args.get("columns", default=None, type=str)
    survived = request.args.get("survived", default=None, type=int)
    age_min = request.args.get("age_min", default=None, type=int)
    age_max = request.args.get("age_max", default=None, type=int)
    pclass = request.args.get("pclass", default=None, type=int)
    fare_min = request.args.get("fare_min", default=None, type=float)
    fare_max = request.args.get("fare_max", default=None, type=float)
    cabin = request.args.get("cabin", default=None, type=bool)
    embarked = request.args.get("embarked", default=None, type=str)
    sibsp_min = request.args.get("sibsp_min", default=None, type=int)
    sibsp_max = request.args.get("sibsp_max", default=None, type=int)
    parch_min = request.args.get("parch_min", default=None, type=int)
    parch_max = request.args.get("parch_max", default=None, type=int)

    tabla = titanic.copy()

    if not survived is None:
        tabla = tabla[tabla["Survived"] == survived]
    
    if not age_min is None:
        tabla = tabla[tabla["Age"] >= age_min]
    if not age_max is None:
        tabla = tabla[tabla["Age"] <= age_max]
    
    if not pclass is None:
        tabla = tabla[tabla["Pclass"] == pclass]
    
    if not fare_min is None:
        tabla = tabla[tabla["Fare"] >= fare_min]
    if not fare_max is None:
        tabla = tabla[tabla["Fare"] <= fare_max]
    
    if not cabin is None:
        tabla = tabla[(~(tabla["Cabin"].isna())) == cabin]
    
    if not embarked is None:
        tabla = tabla[tabla["Embarked"] == embarked]

    if not sibsp_min is None:
        tabla = tabla[tabla["SibSp"] >= sibsp_min]
    if not sibsp_max is None:
        tabla = tabla[tabla["SibSp"] <= sibsp_max]
    if not parch_min is None:
        tabla = tabla[tabla["Parch"] >= parch_min]
    if not parch_max is None:
        tabla = tabla[tabla["Parch"] <= parch_max]

    if not columns is None:
        columns = columns.split(",")
        tabla = tabla[columns]
        
    return tabla.to_json(orient="records")

@app.get("/graficas/titanic/sexo_vs_supervivencia") # application/json
def graficas_titanic_sexo_vs_supervivencia():
    M = titanic[["Sex", "Survived"]].groupby(["Sex", "Survived"]).size().unstack()
    R1 = M.divide(M.sum(axis=1), axis=0)
    R2 = M.divide(M.sum(axis=0), axis=1)

    figure, axis = pyplot.subplots(1, 3, figsize=(40, 10))

    seaborn.heatmap(M, cmap="Greens", annot=True, fmt=".0f", ax=axis[0])
    seaborn.heatmap(R1, cmap="Blues", annot=True, fmt=".1f", ax=axis[1])
    seaborn.heatmap(R2, cmap="Reds", annot=True, fmt=".1f", ax=axis[2])

    # 1. Guardar la gráfica en un buffer de memoria
    buffer = io.BytesIO()
    figure.savefig(buffer, format="png", bbox_inches="tight")
    
    # 2. Liberar la memoria de la figura de Matplotlib
    pyplot.close(figure)
    
    # 3. Regresar el puntero al inicio del archivo en memoria
    buffer.seek(0)

    # 4. Devolver la imagen con el mimetype adecuado
    return send_file(buffer, mimetype="image/png")

# curl --output sexo_vs_supervivencia.png localhost:3000/graficas/titanic/sexo_vs_supervivencia
app.run(host="0.0.0.0", port=3000)