from pydantic import BaseModel, Field
from typing import Dict, List, Tuple

class GrafoEntrada(BaseModel):
    # laa lista de adyacencia es un diccionario donde la clave es el nodo 
    grafo: Dict[str, List[Tuple[str, int]]] = Field(
        ..., 
        description="Lista de adyacencia del grafo con sus pesos."
    )
    origen: str = Field(..., description="Nodo de partida de la búsqueda.")
    destino: str = Field(..., description="Nodo objetivo de la búsqueda.")
    limite_nodos: float = Field(
        0.8, 
        description="Límite de nodos a visitar por defecto (80% del total de nodos)."
    )
