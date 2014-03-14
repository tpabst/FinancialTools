# Methodes et formaules de de calculs de finances


# Formaule Calcul de la Mensualité
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


