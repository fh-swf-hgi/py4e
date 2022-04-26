def chop(liste):
    if len(liste) > 0:
        del liste[0]
    if len(liste) > 1:
        del liste[len(liste) - 1]
    return None


l = ["a", "b", "c"]
chop(l)
