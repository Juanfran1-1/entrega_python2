#FUNCIONES PARA MAIN

def calcular_puntos(kills,assists,deaths):
    puntaje = {'kill' : 3 , 'assist': 1 , 'death': -1}
    return (kills * puntaje['kill']) + (assists * puntaje['assist']) + (puntaje['death'] if deaths else 0)

def mostrar_ronda(stats_ronda,mvps,i,rm):
    ordenados= sorted(stats_ronda.items(), key= lambda x: x[1]['points'], reverse=True)
    print(f"\nRanking ronda {i}") if i < rm else print('\nRanking final')
    print(f"{'jugador':<10} {'kills':<5} {'asistencias':<5} {'muertes':<5} {' mvps':<5} {'puntos':<6}")
    print('-'*60)
    for jugador,stats in ordenados:
        print(f"{jugador:<10} {stats['kills']:>5} {stats['assists']:>11} {stats['deaths']:>7} {mvps[jugador]:>5} {stats['points']:>6}")
    print("-" * 60)

def procesar_rondas(rounds):
    mvps = {}
    stats_ronda= {}
    i= 0
    rm = len(rounds)
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
        mostrar_ronda(stats_ronda,mvps,i,rm)