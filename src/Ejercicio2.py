def time_tot (playlist):
    minuts = 0
    seconds = 0
    for elem in playlist:
        minuts += int(elem["duration"][0])
        seconds += int(elem["duration"][2:4]) 
    minuts += seconds // 60
    seconds = seconds % 60
    return(f"Duracion total: {minuts}m {seconds}s")

def cancion_larga (playlist):
    maxmin = -9999
    maxseg = -9999
    nommax = ""
    for dic in playlist:
        if int(dic["duration"][0]) > maxmin:
            maxmin = int(dic["duration"][0])
            maxseg = int(dic["duration"][2:4])      #se podria usar minutos,segundos = dic["duration"].split[":"]
            nommax = dic["title"]
        elif int(dic["duration"][0]) == maxmin:
            if int(dic["duration"][2:4]) > maxseg:
                maxmin = int(dic["duration"][0])
                maxseg = int(dic["duration"][2:4])
                nommax = dic["title"]
    return (f"{nommax} ({maxmin}:{maxseg})")

def cancion_corta (playlist):
    minmin = 9999
    minseg = 9999
    nommin = ""
    for dic in playlist:
        if int(dic["duration"][0]) < minmin:
            minmin = int(dic["duration"][0])
            minseg = int(dic["duration"][2:4])      
            nommin = dic["title"]
        elif int(dic["duration"][0]) == minmin:
            if int(dic["duration"][2:4]) < minseg:
                minmin = int(dic["duration"][0])
                minseg = int(dic["duration"][2:4])
                nommin = dic["title"]
    return (f"{nommin} ({minmin}:{minseg})")