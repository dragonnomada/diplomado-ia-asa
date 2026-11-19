import pandas

from matplotlib import pyplot
import seaborn

def reporte_discreto_simple(X, a, b, plot=True):
    x = X[a]
    y = X[b]

    M = pandas.DataFrame([x, y]).T.groupby([a, b]).size().unstack()
    R1 = M.divide(M.sum(axis=1), axis=0)
    R2 = M.divide(M.sum(axis=0), axis=1)

    if plot:
        figure, axis = pyplot.subplots(1, 3, figsize=(20, 5))
        axis[0].set_title("Soporte")
        seaborn.heatmap(M, cmap="Greens", annot=True, fmt=".0f", ax=axis[0])
        axis[1].set_title("% Horizontales")
        seaborn.heatmap(100 * R1, cmap="Blues", annot=True, fmt=".1f", ax=axis[1])
        axis[2].set_title("% Verticales")
        seaborn.heatmap(100 * R2, cmap="Reds", annot=True, fmt=".1f", ax=axis[2])

    return pandas.concat([M, 100 * R1, 100 * R2], axis=1, 
                         keys=["Soporte", "% Horizontales", "% Verticales"],).round(1)

def reporte_discreto_multiple(X, clases, respuesta, plot=True, nombre="reporte.png"):
    x = X[clases]
    y = X[respuesta]

    M = X[clases].join(X[respuesta]).groupby(clases + [respuesta]).size().unstack()
    R1 = M.divide(M.sum(axis=1), axis=0)
    R2 = M.divide(M.sum(axis=0), axis=1)

    if plot:
        figure, axis = pyplot.subplots(1, 3, figsize=(40, 20))
        axis[0].set_title("Soporte")
        seaborn.heatmap(M, cmap="Greens", annot=True, fmt=".0f", ax=axis[0])
        axis[1].set_title("% Horizontales")
        seaborn.heatmap(100 * R1, cmap="Blues", annot=True, fmt=".1f", ax=axis[1])
        axis[2].set_title("% Verticales")
        seaborn.heatmap(100 * R2, cmap="Reds", annot=True, fmt=".1f", ax=axis[2])
        figure.savefig(nombre, dpi=300)
        pyplot.show()

    return pandas.concat([M, 100 * R1, 100 * R2], axis=1, 
                         keys=["Soporte", "% Horizontales", "% Verticales"],).round(1)