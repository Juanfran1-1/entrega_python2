#FUNCIONES PARA EL MAIN

#FUNCION QUE CALCULA LOS PUNTOS OBTENIDOS EN CADA RONDA POR MEDIO DE UN DICCIONARIO PUNTAJE CON KILL=3, ASSIST=1, DEATH=-1 PARA RETONARLOS
def calcular_puntos(kills,assists,deaths):
    puntaje = {'kill' : 3 , 'assist': 1 , 'death': -1}
    return (kills * puntaje['kill']) + (assists * puntaje['assist']) + (puntaje['death'] if deaths else 0)

#MUESTRA CADA RONDA PREGUNTANDO SI LLEGO AL MAXIMO PARA MOSTRAR UN OPCION DE MENSAJE Y EL RANKING PROGRESIVO DE LAS RONDAS
def mostrar_ronda(stats_ronda,i,rounds):
    #CREO UNA LISTA CON LOS DATOS ORDENADOS EN BASE A LOS PUNTOS CON ORDEN DECRECIENTE PARA POSTERIORNENTE MOSTRARLOS
    ordenados= sorted(stats_ronda.items(), key= lambda x: x[1]['points'], reverse=True)
    print(f"\nRanking ronda {i}") if i < len(rounds) else print('\nRanking final')
    print(f"{'jugador':<10} {'kills':<5} {'asistencias':<5} {'muertes':<5} {' mvps':<5} {'puntos':<6}")
    print('-'*60)
    for jugador,stats in ordenados:
        print(f"{jugador:<10} {stats['kills']:>5} {stats['assists']:>11} {stats['deaths']:>7} {stats['mvp']:>5} {stats['points']:>6}")
    print("-" * 60)

#PROCESA LAS RONDAS MEDIANTE UN NUEVO DICCIONARIO VACIO QUE VA A CONTENERLAS KEYS DEL ORIGINAL SUMADO LOS MVP Y LOS PUNTOS TOTALES 
def procesar_rondas(rounds):
    #CREO NUEVO DICCIONARIO
    stats_ronda= {}
    #HAGO UN FOR QUE OBTIENE CADA DICCIONARIO DE LA RONDA DE ROUNDS Y UN ITERABLE PARA EL NUMERO DE LA RONDA
    for i,ronda in enumerate(rounds,start=1):
        puntajes_ronda = {}
        #SETEO EN CADA RONDA MVP="" Y MAX= -1 PARA OBTENER POSTERIORMENTE EL MVP DE CADA RONDA
        mvp= " "
        max = -1
        #OBTENGO EL NOMBRE DEL JUGADOR Y SUS ESTADISTICAS(KILLS,ASSISTS,DEATHS) DE CADA ITEM DE LA RONDA ACTUAL
        for jugador,stats in ronda.items():
            puntos = calcular_puntos(stats['kills'],stats['assists'],stats['deaths'])
            #SI EL JUGADOR TODAVIA NO ESTA EN EL DICCIONARIO CREADO LO CREO CON UN VALOR DEFAULT DE 0 EN TODO 
            if jugador not in stats_ronda:
                stats_ronda[jugador]= {'kills': 0, 'assists': 0, 'deaths': 0,'mvp': 0, 'points': 0}
            #LE AÑADO CADA VALOR A SU CAMPO     
            stats_ronda[jugador]['kills'] += stats['kills']
            stats_ronda[jugador]['assists']+= stats['assists']
            stats_ronda[jugador]['deaths']+= stats['deaths']
            stats_ronda[jugador]['points']+= puntos
            puntajes_ronda[jugador] = puntos
            if puntajes_ronda[jugador] > max :
                max = puntajes_ronda[jugador]
                mvp = jugador 
        #POSTERIORMENTE A CALCULAR QUIEN FUE EL MVP EN BASE A SU NOMBRE Y SUS PUNTOS LE AÑADO 1 AL VALOR QUE CONTIENE ACTUALMENTE         
        stats_ronda[mvp]['mvp']=+ 1
        mostrar_ronda(stats_ronda,i,rounds)