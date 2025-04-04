#FUNCIONES PARA MAIN

def calcular_puntos(kills,assists,deaths):
    puntaje = {'kill' : 3 , 'assist': 1 , 'death': -1}
    return (kills * puntaje['kill']) + (assists * puntaje['assist']) + (puntaje['death'] if deaths else 0)

def procesar_rondas(rounds):
    mvps = {}
    stats_ronda= {}
    i= 0
    for ronda in rounds:
        i+=1
        puntajes_ronda = {}
        mvp= " "
        max = -1
        for jugador,stats in ronda.items():
            puntos = calcular_puntos(stats['kills'],stats['assists'],stats['deaths'])
            
            if jugador not in stats_ronda:
                stats_ronda[jugador]= {'kills': 0, 'assists': 0, 'deaths': 0, 'points': 0}
            if jugador not in mvps:
                mvps[jugador]=0
            stats_ronda[jugador]['kills'] += stats['kills']
            stats_ronda[jugador]['assists']+= stats['assists']
            stats_ronda[jugador]['deaths']+= stats['deaths']
            stats_ronda[jugador]['points']+= puntos
            puntajes_ronda[jugador] = puntos
            if puntajes_ronda[jugador] > max :
                max = puntajes_ronda[jugador]
                mvp = jugador 
        mvps[mvp]=+ 1