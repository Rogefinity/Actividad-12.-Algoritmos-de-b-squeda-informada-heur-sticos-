import time

def greedy_best_first_search(grafo: dict, origen: str, destino: str, limite: int):
    inicio_tiempo = time.time()
    
    visitados = []
    ruta = []
    nodo_actual = origen
    nodos_totales = len(grafo)
    limite_nodos = int(nodos_totales * limite)
    
    #costo base inicial de memoria variables
    costo_memoria = len(grafo.keys()) 
    
    while nodo_actual != destino and len(visitados) < limite_nodos:
        if nodo_actual not in visitados:
            visitados.append(nodo_actual)
            ruta.append(nodo_actual)
            
        vecinos = grafo.get(nodo_actual, [])
        if not vecinos:
            break
            
        #criterio de evaluación greddy: Tomar siempre el vecino con menor costo inmediato 
        vecino_optimo = min(vecinos, key=lambda x: x[1])
        
        #si el vecino óptimo ya se visito, buscar la segunda mejor opción para evitar ciclos 
        opciones_validas = [v for v in vecinos if v[0] not in visitados]
        if not opciones_validas:
            break
            
        vecino_optimo = min(opciones_validas, key=lambda x: x[1])
        nodo_actual = vecino_optimo[0]

    #agregar el ultimo nodo si se alcanzo el destino
    if nodo_actual == destino:
        ruta.append(destino)
        visitados.append(destino)
        solucion = True
    else:
        solucion = False
        
    tiempo_fin = time.time()
    T_n = tiempo_fin - inicio_tiempo
    S_n = costo_memoria + len(visitados) + len(ruta)

    return {
        "nodos_visitados": len(visitados),
        "solucion": solucion,
        "ruta": ruta,
        "T_n": f"{T_n:.6f} segundos",
        "S_n": f"O({S_n}) unidades espaciales estimadas"
    }
