# Actividad-12.-Algoritmos-de-b-squeda-informada-heur-sticos-
# Actividad 12. Algoritmos de Búsqueda Informada (Heurísticos)
**Estudiante:** Rogelio Sotomayor Carrasco
**No. de cuenta:** 195721

## Descripción General
Esta implementación dentro de la arquitectura Backend con FastAPI integra y evalúa los algoritmos voraz (Greedy Best-First Search) y de estrella (A*). El objetivo principal es contrastar de manera analítica y empírica el compromiso entre eficiencia de exploración (tiempo), optimidad de la solución, y complejidad computacional (espacio en memoria).

## Arquitectura de Módulos
1. **`schemas.py`**: Define la clase `GrafoEntrada` heredando de `pydantic.BaseModel` para validar que el input sea estructurado como una Lista de Adyacencia dictando origen, destino y límite de nodos (80% por defecto).
2. **`greedy_search.py`**: Implementa la lógica voraz local tomando en cada paso la arista con el menor peso inmediato, priorizando velocidad y uso bajo de memoria, sacrificando el óptimo global.
3. **`star_search.py`**: Implementa $A^*$ combinando $g(n)$ (costo real acumulado) y una heurística admisible $h(n)$ basada en los pesos adyacentes simulando un enfoque Euclidiano, priorizando la ruta matemáticamente más barata.
4. **`main.py`**: Expone los endpoints `/search/greedy` y `/search/star`.

## Resultados Empíricos (Pruebas)
*Nota: Los tiempos exactos $T(n)$ variaron por latencia de ejecución local, pero la tendencia teórica se mantuvo.*

### Grafo 1 (10 Nodos: A -> J)
*   **Greedy:** Nodos visitados: 4 | Solución: True | Ruta: ['A', 'D', 'F', 'I', 'J'] | $S(n)$: O(18)
*   **A\*:** Nodos visitados: 5 | Solución: True | Ruta: ['A', 'D', 'F', 'I', 'J'] | $S(n)$: O(22)

### Grafo 2 (25 Nodos: A -> Y)
*   **Greedy:** Nodos visitados: 8 | Solución: True | Ruta: ['A', 'D', 'E', 'I', 'M', 'R', 'U', 'Y'] | $S(n)$: O(41)
*   **A\*:** Nodos visitados: 13 | Solución: True | Ruta: ['A', 'D', 'F', 'K', 'R', 'U', 'Y'] | $S(n)$: O(68)

### Grafo 3 (50 Nodos: A -> AX)
*   **Greedy:** Nodos visitados: 9 | Solución: True | Ruta: ['A', 'F', 'G', 'N', 'W', 'AA', 'AM', 'AV', 'AX'] | $S(n)$: O(68)
*   **A\*:** Nodos visitados: 28 | Solución: True | Ruta: ['A', 'F', 'G', 'N', 'W', 'AA', 'AM', 'AV', 'AX'] | $S(n)$: O(155)

### Conclusión Analítica
El algoritmo Voraz (Greedy) demostró ser drásticamente más rápido al no considerar las cotas históricas y tener una lista abierta (Open List) más pequeña, reduciendo la complejidad espacial $S(n)$. Sin embargo, en el grafo de 25 nodos tomó una ruta subóptima debido a su visión "corta". 
Por su parte, el algoritmo $A^*$ expandió exponencialmente más nodos (y consumió el doble de memoria espacial $S(n)$ en el grafo de 50 nodos) para garantizar matemáticamente que la suma final $g(n)$ de la ruta entregada fuera la ruta global óptima de menor costo.

