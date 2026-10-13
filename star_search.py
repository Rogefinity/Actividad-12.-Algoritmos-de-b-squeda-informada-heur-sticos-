import time

def heuristica_simulada_euclidiana(nodo: str, destino: str, grafo: dict) -> int:
    """
    Como no se proporcionan coordenadas XY (x, y) de cada nodo en los esquemas, 
    simulamos una heurística relajada. Asignamos a h(n) un costo base. 
    Si el nodo no tiene vecinos, h(n) es muy alto.
    """
    if nodo == destino:
        return 0
    vecinos = grafo.get(nodo, [])
    if not vecinos:
        return 9999
    #heuristica minima admisible: El menor peso para salir del nodo actual
    return min(vecinos, key=lambda x: x[1])[1]

def a_star_search(grafo: dict, origen: str, destino: str, limite: int):
    inicio_tiempo = time.time()
    
    nodos_totales = len(grafo)
    limite_nodos = int(nodos_totales * limite)
    
    #estructura - (f(n), g(n), nodo_actual, camino_recorrido)
    open_list = [(0 + heuristica_simulada_euclidiana(origen, destino, grafo), 0, origen, [origen])]
    closed_list = set()
    nodos_visitados = 0
    costo_memoria = len(grafo.keys())
    
    solucion_encontrada = False
    ruta_final = []
    
    while open_list and nodos_visitados < limite_nodos:
        #ordenar para simular una PriorityQueue y tomar el menor f(n)
        open_list.sort(key=lambda x: x[0])
        f_actual, g_actual, nodo_actual, camino = open_list.pop(0)
        
        if nodo_actual in closed_list:
            continue
            
        closed_list.add(nodo_actual)
        nodos_visitados += 1
        
        if nodo_actual == destino:
            solucion_encontrada = True
            ruta_final = camino
            break
            
        vecinos = grafo.get(nodo_actual, [])
        for vecino, peso_arista in vecinos:
            if vecino not in closed_list:
                g_vecino = g_actual + peso_arista
                h_vecino = heuristica_simulada_euclidiana(vecino, destino, grafo)
                f_vecino = g_vecino + h_vecino
                open_list.append((f_vecino, g_vecino, vecino, camino + [vecino]))

    tiempo_fin = time.time()
    T_n = tiempo_fin - inicio_tiempo
    S_n = costo_memoria + len(closed_list) + len(open_list)
    
    return {
        "nodos_visitados": nodos_visitados,
        "solucion": solucion_encontrada,
        "ruta": ruta_final if solucion_encontrada else [],
        "T_n": f"{T_n:.6f} segundos",
        "S_n": f"O({S_n}) unidades espaciales estimadas"
    }
