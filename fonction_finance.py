# Methodes et formules de de calculs de finances
# -*-coding:Utf-8 -*

# Formule Calcul de la Mensualité
#
# C : montant emprunté en euros
# m : mensualité en euros
# n : durée d'emprunt en mois
# t : taux effectif Global annuel ( attention, pas en %)
#
#
#                             t
#                        C x ----
#                             12
# Formule :  m = ---------------------------
#                       /       t  \ -42
#                  1 - | 1 + ----  |
#                       \      12  /
#

def calculMensualite(C, n, t):
    return (float(C) * float(t) / 12) / (1 - (1 + float(t) / 12)**(float(-n)))


# Formule calcul du taux périodique
#
# TxPer : Taux périodique
# TxAn  : Taux annuel
# EchAn : nombre d'échéances par an (i.e. 12 mois)
#
#                      TxAn
# Formule :  TxPer = ---------
#                      EchAn
#

def calculTauxPeriodique(txAn, echAn):
    return float(txAn)/float(echAn)



# Formule calcul des intêrets

def calculInteret(capitalRestant, tauxAnnuel, echParAn):
    tauxPeriodique = calculTauxPeriodique(tauxAnnuel, echParAn)
    return tauxPeriodique * capitalRestant



# tableau amortissement

def amortissement(capital, tauxAnnuel, nbrEch, echParAn):
    if nbrEch > 0:
        mensualite = calculMensualite(capital, nbrEch, tauxAnnuel)
        interet = calculInteret(capital, tauxAnnuel, echParAn)
        capitalRbst = mensualite - interet
        newCapital = capital - capitalRbst
        print("%5.2f" % capital, "%.2f" % mensualite, "%.2f" % interet, "%.2f" % capitalRbst, nbrEch)
        amortissement(newCapital, tauxAnnuel, nbrEch -1, echParAn)



# tableau amortissement epargne
def epargne(a,b):
    x=0
    while x < 6:
        y = a * x + b
        print x+7
        print y
        x=x+1
