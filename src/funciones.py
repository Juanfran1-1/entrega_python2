#FUNCIONES PARA MAIN

def calcular_puntos(kills,assists,deaths):
    puntaje = {'kill' : 3 , 'assist': 1 , 'death': -1}
    return (kills * puntaje['kill']) + (assists * puntaje['assist']) + (puntaje['death'] if deaths else 0)