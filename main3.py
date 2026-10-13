from fastapi import FastAPI
from schemas import GrafoEntrada
from greedy_search import greedy_best_first_search
from star_search import a_star_search

app = FastAPI(title="Actividad 12: Búsquedas Informadas (Greedy y A*)")

@app.post("/search/greedy")
def endpoint_greedy(datos: GrafoEntrada):
    resultado = greedy_best_first_search(
        grafo=datos.grafo, 
        origen=datos.origen, 
        destino=datos.destino, 
        limite=datos.limite_nodos
    )
    return resultado

@app.post("/search/star")
def endpoint_star(datos: GrafoEntrada):
    resultado = a_star_search(
        grafo=datos.grafo, 
        origen=datos.origen, 
        destino=datos.destino, 
        limite=datos.limite_nodos
    )
    return resultado
