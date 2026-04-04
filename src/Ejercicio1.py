def calc_lines (text):
    return(len(text.split("."))) #Se podria usar splitlines()

def tot_words (text):
    return(len(text.split()))

def prom_words (text):
    prom = tot_words(text) / calc_lines(text)
    return (prom)

def lines_prom (text):
    lines = text.split(".")
    listprom = [n for n in lines if tot_words(n) > prom_words(text)]
    return(listprom)