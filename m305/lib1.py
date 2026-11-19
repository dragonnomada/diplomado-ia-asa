import numpy
import pandas

def quantiles(serie, n=10, u=0.5):
    serie = serie.copy()
    serie.name = "Value"
    
    q = pandas.qcut(serie, q=n)
    q.name = "Quantile"

    median = lambda serie: serie.median()

    cuantiles = pandas.DataFrame([q, serie]).T.groupby("Quantile").agg({
        "Value": (
            "count",
            "sum",
            "mean",
            "std",
            "min",
            median,
            "max",
        )
    }).astype(float).round(2)[("Value", "mean")]

    diferencia_absoluta = cuantiles - cuantiles.rolling(2).first()
    diferencia_absoluta.name = "inc abs"
    diferencia_relativa = diferencia_absoluta / cuantiles.rolling(2).first()
    diferencia_relativa.name = "% inc rel"
    
    cambio_relativo = (diferencia_relativa > diferencia_relativa.quantile(u))
    cambio_relativo.name = "change"
    
    porcentajes_inf = pandas.Series(numpy.linspace(0, 1 - 1/n, n), index=cuantiles.index) * 100
    porcentajes_inf .name = "% inf"
    
    porcentajes_sup = pandas.Series(numpy.linspace(1/n, 1, n), index=cuantiles.index) * 100
    porcentajes_sup .name = "% sup"

    grupo = pandas.Series(numpy.arange(1, n + 1), index=cuantiles.index)
    grupo.name = "clu"
    
    return pandas.DataFrame([grupo, porcentajes_inf, porcentajes_sup, cuantiles, 
                      diferencia_absoluta, diferencia_relativa * 100, cambio_relativo]).T.astype(float).round(2)
    