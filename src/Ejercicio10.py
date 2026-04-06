
def win_round (round, tabla, numr):
    max = -1
    maxplayer = ""
    for player in round: 
        points = sum(round[player].values())
        if points > max: 
            maxplayer = player 
            max = points
        tabla[player]["p"] += points #actualizo puntaje total
        tabla[player]["pr"] = tabla[player]["p"] / numr
        if points > tabla[player]["mr"]:
            tabla[player]["mr"] = points #actualizo mejor ronda
    tabla[maxplayer]["rg"] += 1
    return (maxplayer, max)

def ordenarTabla (tabla):
    ordenada = sorted(tabla.items(), key=lambda x: x[1]["p"], reverse=True)
    return ordenada

def tabla_final (ordenada):
    print()
    print(f"""   Tabla de posiciones final:
    Cocinero  Puntaje  Rondas ganadas  Mejor Ronda  Promedio
    {"-"*60}
    """)
    for n in range(0,5):
       print (f"    {ordenada[n][0]:<10}  {ordenada[n][1]["p"]}     {ordenada[n][1]["rg"]:^15}      {ordenada[n][1]["mr"]}      {ordenada[n][1]["pr"]}")
    
