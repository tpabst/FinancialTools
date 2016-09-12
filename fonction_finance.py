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

def calculTauxPeriodiqueProportionnel(txAn, echAn):
    return float(txAn)/float(echAn)

def calculTauxPeriodiqueActuarielle(txAn, echAn):
    return 


# Formule calcul des intêrets

def calculInteret(capitalRestant, tauxAnnuel, echParAn):
    proportionnel = True
    if proportionnel == True:
        tauxPeriodique = calculTauxPeriodiqueProportionnel(tauxAnnuel, echParAn)
    else:
        tauxPeriodique = calculTauxPeriodiqueActuarielle(tauxAnnuel, echParAn)

    return tauxPeriodique * capitalRestant



# tableau amortissement par récurence

def amortissement(capital, tauxAnnuel, nbrEch, echParAn):
    if nbrEch > 0:
        mensualite = calculMensualite(capital, nbrEch, tauxAnnuel)
        interet = calculInteret(capital, tauxAnnuel, echParAn)
        capitalRbst = mensualite - interet
        newCapital = capital - capitalRbst
        print("%5.2f" % capital, "%.2f" % mensualite, "%.2f" % interet, "%.2f" % capitalRbst, nbrEch)
        amortissement(newCapital, tauxAnnuel, nbrEch -1, echParAn)

# tableau amortissement

def amortissement2(capital, tauxAnnuel, nbrEch, echParAn):
    try:
        assert nbrEch > 0
        i = nbrEch
        TotalInterets = 0
        newCapital = capital
        mensualite = calculMensualite(newCapital, i, tauxAnnuel)
        capitalRbst = 0

        while i != 0:
            interet = calculInteret(newCapital, tauxAnnuel, echParAn)
            TotalInterets += interet
            capitalRbst = mensualite - interet
            print("%5.2f" % newCapital, "%.2f" % mensualite, "%.2f" % interet, "%.2f" % capitalRbst, i)
            newCapital -= capitalRbst
            i-=1
            if i < 41-10 :
                break

        print("")
        print("TotalInterets: %f" % TotalInterets)

    except AssertionError:
        print("Une échéance inférieur à 1 ! Vraiement !")



# tableau amortissement

def amortissement3(capital, tauxAnnuel, nbrEch,  tauxAnnuelAssurance):
    echParAn = 12
    try:
        assert nbrEch > 0
        i = nbrEch
        TotalInterets = 0
        TotalInteretsAssurance = 0
        newCapital = capital
        mensualite = calculMensualite(newCapital, i, tauxAnnuel)
        print("mensualite : %f" % mensualite)
        mensualiteAssurance = calculMensualite(newCapital, i, tauxAnnuelAssurance)
        capitalRbst = 0

        while i != 0:
            interet = calculInteret(newCapital, tauxAnnuel, echParAn)
            interetAssurance = calculInteret(newCapital, tauxAnnuelAssurance, echParAn)
            TotalInterets += interet
            TotalInteretsAssurance += interetAssurance
            capitalRbst = mensualite - interet
            TotalMensualite = mensualite #+ interetAssurance
            print("%5.2f" % newCapital, "%.2f" % mensualite, "%.2f" % interet,
                  "%.2f" % capitalRbst, "%.2f" % interetAssurance, 
                  "%.2f" % TotalMensualite, i)
            newCapital -= capitalRbst
            i-=1

        print("")
        print("TotalInterets: %f" % TotalInterets)
        print("TotalInteretsAssurance: %f" % TotalInteretsAssurance)
        CoutTotal = TotalInterets + TotalInteretsAssurance
        print("CoutTotal: %f" % CoutTotal)

        print("")
        print("mensualite theorique: %f" % TotalMensualite)
        TotalInteretsPlusCapital = CoutTotal + capital
        print("TotalInteretsPlusCapital: %f" % TotalInteretsPlusCapital)

    except AssertionError:
        print("Une échéance inférieur à 1 ! Vraiement !")


# tableau amortissement

def amortissement4(capital, tauxAnnuelCapital, nbrEch,  tauxAnnuelAssurance):
    echParAn = 12
    try:
        assert nbrEch > 0
        i = nbrEch
        TotalInteretsCapital = 0
        TotalInteretsAssurance = 0
        TotalInterets = TotalInteretsCapital + TotalInteretsAssurance
        newCapital = capital
        mensualite = calculMensualite(newCapital, i, tauxAnnuelCapital)
        capitalRbst = 0

        interetAssurance = round(capital * tauxAnnuelAssurance / echParAn, 2)

        while i != 0:
            interet = round(calculInteret(newCapital, tauxAnnuelCapital, echParAn), 2)
            TotalInteretsCapital += interet
            TotalInteretsAssurance += interetAssurance
            capitalRbst = mensualite - interet
            MensualiteTotal = mensualite + interetAssurance
            print("%5.2f" % newCapital,
                  "%.2f" % interetAssurance,
                  "%.2f" % interet,
                  "%.2f" % capitalRbst,
                  "%.2f" % mensualite,
                  "%.2f" % MensualiteTotal,
                  i)
            newCapital -= capitalRbst
            i-=1
            #if i < 41-5 :
            #    break

        print("")
        print("TotalInteretsCapital: %.2f" % TotalInteretsCapital)
        print("TotalInteretsAssurance: %.2f" % TotalInteretsAssurance)
        CoutTotal = TotalInteretsCapital + TotalInteretsAssurance
        print("CoutTotal: %f" % CoutTotal)
        TotalInteretsCapitalPlusCapital = CoutTotal + capital
        print("TotalInteretsCapitalPlusCapital: %.2f" % TotalInteretsCapitalPlusCapital)

    except AssertionError:
        print("Une échéance inférieur à 1 ! Vraiement !")
