#!/usr/bin/env python
# -*- coding: cp1252 -*-
 
from math import log, exp
 
def titre_general():
    # Titre clin d'oeil à la "Pompe à phynances" d'Alfred JARRY...
    print
    print
    print
    print "                  *******************************************"
    print "                  *             +- PHYNANCE -+              *"
    print "                  *      Logiciel de calculs financiers     *"
    print "                  *******************************************"
    print
   
def titres(titre):
    blancs,etoiles=[15,15,9,7],[50,50,60,65]
    suite=["à remboursement constant  *","à amortissement constant  *",\
    "progressifs à un ou plusieurs taux  *","à remboursements ronds + reliquat final  *"]
    print
    print
    print " "*blancs[titre]+"*"*etoiles[titre]
    print " "*blancs[titre]+"*  Echéancier de prêts "+suite[titre]
    print " "*blancs[titre]+"*"*etoiles[titre]
    print
    print
 
def sortie():
    print
    print
    print "   Au revoir !"
 
def formate(nbr):
    if nbr.find(".")==-1:
        nbr+=".00"
    else:
        if len(nbr)==nbr.find(".")+2:
            nbr+="0"
    return nbr
 
def cout_credit(co):
    print "     Pour un coût total du crédit de %.2f" % co,"€"
    print
 
def incorrect():
    print "           ...Désolé, valeur incorrecte. Veuillez recommencer ..."
 
def pas_nb():
    print "             ... Ce n'est pas un nombre. Veuillez recommencer..."
 
def chx_message(ch):
    ch='       ... Pour retourner au menu,;         ... Pour la suite,'
    return ch
 
def message(mess):
    print
    print "       ",mess,"Presser ENTREE ..."
    raw_input("")
 
def demande_nb_taux(nb):
    while nb==0:
        try:
            nb=int(raw_input("          Nombre de taux (1, 2 ou 3): "))
            if nb <1 or nb >3:
                nb=0
                print "Entrée non comprise entre 1 et 3. Veuillez recommencer..."
        except ValueError:
            pas_nb()
    return nb
 
def demande_tx(ta):
    while ta==0:
        try:
            ta=float(raw_input("? "))
            if ta<0:
                ta=0
                incorrect()
            elif ta==0:
                print "Taux nul... Veuillez recommencer..."
            elif ta >33.33:
                ta=0
                print "Taux supérieur au taux d'usure. Veuillez recommencer..."
        except ValueError:
            pas_nb()
    return ta
 
def demande_duree(dur,periode):
    noms={1:"années",2:"semestres",4:"trimestres",12:"mois"}
    coeff={1:12,2:2,4:4,12:1}
    print "Exprimée en nombre d"+"e ,'".split(",")[periode==1]+noms[periode]+",",
    while dur==0:
        try:
            dur=int(raw_input("durée (de 1 à "+str(360/coeff[periode])+" "+noms[periode]+") ? "))
            if dur >360/coeff[periode]:
                dur = 0
                incorrect()
        except ValueError:
            pas_nb()
    return dur
 
def demande_mensualite_souhaitee(vsmt):
    while vsmt==0:
        try:
            vsmt=int(raw_input("    Mensualité "+chr(34)+"ronde"+chr(34)+\
                               " souhaitée (multiple de 50 €) ? "))
            if vsmt%50 != 0:
                vsmt=0
                incorrect()
        except ValueError:
            pas_nb()
    return vsmt
 
def demande_depot(ca,sod,mode):
    if mode==0:
        while ca==0:
            try:
                print "Quel est le montant du dépôt",
                ca=float(raw_input("initial,régulier".split(",")[mode]+" ? "))
                if ca<0:
                    ca=0
                    incorrect()
            except ValueError:
                pas_nb()
    else:
        while sod==0:
            try:
                sod=float(raw_input("Montant de l'augmentation régulière : "))
                if sod<0:
                    sod=0
                    incorrect()
            except ValueError:
                pas_nb()
    return ca,sod    
                                   
def demande_periodicite(periode):
    chx_per,per,ch=0,[12,4,2,1],[]
    #ch=chx_message(ch)
    print                    
    print "               La périodicité sera-t-elle :"
    print "                  1. Mensuelle"
    print "                  2. Trimestrielle"
    print "                  3. Semestrielle"
    print "                  4. Annuelle"
    print
    while chx_per==0:
        try:
            chx_per=int(raw_input("              ** Votre choix ? ** "))
            if chx_per<1 or chx_per>4:
                chx_per=0
                incorrect()
        except ValueError:
            pas_nb()
    periode=per[chx_per-1]
    print
    return periode
 
def demande_capital_emprunte(cap,cap_min):
    while cap==0:
        try:
            cap=float(raw_input("      Somme empruntée (entre "+str(cap_min)+" et 500000 €) : "))
            if cap <cap_min or cap >500000:
                cap=0
                incorrect()
        except ValueError:
            pas_nb()
    return cap
 
def demande_capital(cap,mot):
    while cap==0:
        try:
            cap=float(raw_input( "Quel est votre capital "+mot+" (entre 1000 et 50000 €) : "))
            if cap <1000 or cap >50000:
                cap=0
                incorrect()
        except ValueError:
            pas_nb()
    return cap
 
def entete_tableau():  
    print "|------|------------|----------|-----------|----------|------------|------------|"
    print "| Vsmt |   Capital  |  Rembsmt |  Intérêt  |  Amortmt |   Amort.   |   Capital  |"
    print "|  n°  |            |          |           |          |   cumulé   | restant dû |"
    print "|------|------------|----------|-----------|----------|------------|------------|"
 
def affiche_corps_tableau(i, v1, v2, v3, v4, v5,v6):
    print "| %3i" % i," |%11s" % v1,"|%9s"% v2,"| %9s" % v3,"| %8s" % v4,
    print "|%11s" % v5,"|%11s" % v6,"|"
 
def pied_tableau():
    print "|------|------------|----------|-----------|----------|------------|------------|"
 
def affichage_fin_tranche(v,ta,periode,ch):
    pied_tableau()                  
    message(ch.split(';')[1])                    
    affiche_cap_taux(v,ta,periode)  
    entete_tableau()
   
def affiche_cap_taux(v,ta,periode):
    print "       Capital emprunté :","%11s" % v,"€          Taux :",ta*100*periode,"%"
 
def remboursement_constant():
    cap,cap_min,am,amcu,vsmt,n,ta,dur,periode,co,ch=0,1000,0,0,0,0,0,0,0,0,''
    titres(0)
    ch=chx_message(ch)
    cap=demande_capital_emprunte(cap,cap_min)
    v=formate(str(cap))
    periode=demande_periodicite(periode)
    n=demande_duree(dur,periode)
    print "A quel taux",
    ta=demande_tx(ta)  
    ta=ta/periode/100.0  
    vsmt=round(cap/(((1+ta)**n-1)/(ta*(1+ta)**n)),2)
    am=cap*ta/((1+ta)**n-1)
    print
    print
    titres(0)
    print "Capital emprunté :","%11s" % v,"€          Taux :",ta*100*periode,"%"
    entete_tableau()
    for i in xrange(1,n+1):
        #if i%12==1 and i >1:                   # <| Supprimer le # devant ces lignes    
            #affichage_fin_tranche(v,ta,12,ch)  # <| pour un affichage par 12 versements
        intr = round(cap*ta,2)
        if i==n:
            am=cap
            intr=vsmt-cap
        else:
            am = round(vsmt-intr,2)
        amcu = round(amcu+am,2)
        co=round(co+intr,2)
        v1=formate(str(cap))
        v2=formate(str(vsmt))
        v3=formate(str(intr))
        v4=formate(str(am))
        v5=formate(str(amcu))
        cap = round(cap-am,2)
        v6=formate(str(cap))
        affiche_corps_tableau(i, v1, v2, v3, v4, v5, v6)
    pied_tableau()  
    cout_credit(co)
    message(ch.split(';')[0])  
    print
    return
 
def amortissement_constant():
    cap,cap_min,am,amcu,vsmt,n,ta,dur,periode,co,mess,ch=0,1000,0,0,0,0,0,0,0,0,[],''
    titres(1)
    ch=chx_message(ch)
    cap=demande_capital_emprunte(cap,cap_min)
    v=formate(str(cap))
    periode=demande_periodicite(periode)
    n=demande_duree(dur,periode)
    print "A quel taux",
    ta=demande_tx(ta)  
    ta=ta/periode/100.0
    am = round(cap/n,2)
    print
    print
    titres(1)
    affiche_cap_taux(v,ta,periode)
    entete_tableau()
    for i in xrange(1,n+1):
        #if i%12==1 and i >1:                   # <| Supprimer le # devant ces lignes    
            #affichage_fin_tranche(v,ta,12,ch)  # <| pour un affichage par 12 versements
        intr = round(cap*ta,2)
        vsmt=round(am+intr,2)
        co=round(co+intr,2)
        amcu=round(am*i,2)
        v1=formate(str(cap))
        v4=formate(str(am))
        cap = round(cap-am,2)
        v6=formate(str(cap))        
        if i==n:
            correctif=round(amcu-float(v),2)
            cap=0
            if correctif<0:
                intr=round(intr+correctif,2)
                vsmt=round(vsmt+correctif,2)
                co=round(co+intr+correctif,2)
            elif correctif>0:
                intr=round(intr-correctif,2)
                vsmt=round(vsmt-correctif,2)
                co=round(co+intr-correctif,2)
        v2=formate(str(vsmt))
        v3=formate(str(intr))
        v5=formate(str(amcu))
        v6=formate(str(cap))
        affiche_corps_tableau(i, v1, v2, v3, v4, v5,v6)
    pied_tableau()  
    cout_credit(co)
    message(ch.split(';')[0])  
    print
    return
                         
def remboursements_progressifs():
    am,amcu,co,n,nb,cap,periode,ch=0,0,0,0,0,0,0,''
    x2,x3,cap_min,tx,dur_tx=0,0,100000,[0,0,0],[0,0,0]
    ch=chx_message(ch)
    titres(2)
    cap=demande_capital_emprunte(cap,cap_min)
    periode=demande_periodicite(periode)
    nb=demande_nb_taux(nb)
    for i in xrange(nb):
        ta,dur=0,0
        print "Taux",
        if nb>1:
            print "no "+str(i+1)+" :",
        else:
            print ":",
        ta=demande_tx(ta)
        tx[i]=ta/periode/100.0
        dur_tx[i]=demande_duree(dur,1)
        n+=dur_tx[i]
        print"    ---------------"
    n*=periode
    diff_am=-1
    while diff_am<0:
        try:
            diff_am=int(raw_input("Durée du différé d'amortissement (de 1 à 4 ans): ** ? ** "))
            if diff_am<1 or diff_am>4:
                print
                diff_am=-1
                incorrect()
                print
        except ValueError:
            pas_nb()
            print
    diff_am*=periode
    print"           ---------------"
    prg=-1
    while prg<0:
        try:
            prg=int(raw_input("Progressivité annuelle (en %)) : ** ? ** "))
            if prg<0:
                print
                prg=0
                incorrect()
                print
        except ValueError:
            pas_nb()
            print
    x1,x2,x3=0,0,0
    prg=prg/100.0
    ai1=1/(1+tx[0])
    ai2=1/(1+tx[1])
    ai3=1/(1+tx[2])
    n1=float(dur_tx[0]-diff_am/periode)
    a1=(1+prg)/(1+tx[0])
    a2=(ai1**periode-1)/(ai1-1)
    a3=((1+prg)**n1*ai1**(n1*periode)-1)/((1+prg)*ai1**periode-1)
    x1=a1*a2*a3
    if nb > 1:
        a1=((1+prg)/(1+tx[0])**periode)**n1
        a2=(1+prg)/(1+tx[1])
        a3=(ai2**periode-1)/(ai2-1)
        a4=((1+prg)**dur_tx[1]*ai2**(dur_tx[1]*periode)-1)/((1+prg)*ai2**periode-1)
        x2=a1*a2*a3*a4
    if nb > 2:
        a1=((1+prg)/(1+tx[0])**periode)**n1
        a2=((1+prg)/(1+tx[1])**periode)**dur_tx[1]
        a3=(1+prg)/(1+tx[2])
        a4=(ai3**periode-1)/(ai3-1)
        a5=((1+prg)**dur_tx[2]*ai3**(dur_tx[2]*periode)-1)/((1+prg)*ai3**periode-1)
        x3=a1*a2*a3*a4*a5
    vsmt=cap/(x1+x2+x3)
    vo=vsmt
    print
    print
    titres(2)
    v=formate(str(cap))
    print "Capital emprunté :","%11s" % v,"€"
    for i in xrange(nb):
        print "                Taux n° "+str(i+1)+" : "+formate(str(round(tx[i]*100*periode,2))).rjust(5)+" %      ",
        print "Durée : "+str(dur_tx[i]).rjust(2)+" ans"
    print
    entete_tableau()
    a=tx[0]
    dur1,dur2=dur_tx[0]*periode+1,(dur_tx[0]+dur_tx[1])*periode+1  
    for i in xrange(1,n+1):
        #if i%12==1 and i>1:            # <| Supprimer le # devant ces lignes
            #pied_tableau()             # <|          pour un
            #message(ch.split(';')[1])  # <| affichage de l'échéancier      
            #entete_tableau()           # <|       per 12 versements
        if i<=diff_am:
            am=0
            intr=round(cap*a,2)
            vsmt=intr
            v2=formate(str(vsmt))
        elif i<n:
            if i==dur1:
                a=tx[1]
            elif i==dur2:
                a=tx[2]                                
            vsmt=round(vo*(1+prg)**(1+(i-diff_am-1)/periode),2)            
            intr=round(cap*a,2)
            am=round(vsmt-intr,2)
        else:
            am=cap
            intr=round(vsmt-am,2)
        amcu+=am
        co+=intr
        v1=formate(str(cap))
        v2=formate(str(vsmt))
        v3=formate(str(intr))
        v4=formate(str(am))
        v5=formate(str(amcu))
        cap=round(cap-am,2)
        v6=formate(str(cap))
        affiche_corps_tableau(i, v1, v2, v3, v4, v5, v6)
    pied_tableau()  
    cout_credit(co)
    message(ch.split(';')[0])  
    print
    return
 
def remboursements_ronds_reliquat():
    cap,cap_min,am,amcu,vsmt,n,ta,dur,periode,co,mens,ch=0,1000,0,0,0,0,0,0,0,0,0,''
    ch=chx_message(ch)
    titres(3)
    cap=demande_capital_emprunte(cap,cap_min)
    print "A quel taux",
    ta=demande_tx(ta)
    print
    print "           - Notez bien : l'amortissement est mensuel ! -"
    print
    vsmt=demande_mensualite_souhaitee(vsmt)
    ta = ta/1200.0
    q = 1 + ta
    n = int(cap/vsmt)+1
    mens = q*(q**(n-1)*cap-vsmt*(q**(n-1)-1)/ta)
    while mens>vsmt:
        n+=1
        mens = q*(q**(n-1)*cap-vsmt*(q**(n-1)-1)/ta)
    print
    print "      La durée de remboursement sera obligatoirement de", n/12, "ans",n%12,"mois."
    message(ch.split(';')[1])
    am = round(float(cap/n),2)
    v1=formate(str(cap))
    v=v1
    print
    print
    titres(3)
    v2 = formate(str(vsmt))
    affiche_cap_taux(v,ta,12)
    entete_tableau()
    for i in xrange(1,n+1):
        #if i%12==1 and i >1:                   # <| Supprimer le # devant ces lignes    
            #affichage_fin_tranche(v,ta,12,ch)  # <| pour un affichage par 12 versements
        v1=formate(str(cap))
        intr = round(cap*ta,2)
        if i==n:
            am=cap
            vsmt=round(am+intr,2)
            cap=0
        else:
            am = round(vsmt - intr,2)
            cap = round(cap - am,2)
        amcu = round(amcu + am,2)
        co= round(co + intr,2)      
        v2 = formate(str(vsmt))
        v3=formate(str(intr))  
        v4 = formate(str(am))
        v5=formate(str(amcu))
        v6=formate(str(cap))
        affiche_corps_tableau(i,v1,v2,v3,v4,v5,v6)
    pied_tableau()  
    cout_credit(co)
    message(ch.split(';')[0])
    print
    return    
 
def cherche_taux():
    cap,cap_fin,ta,dur,periode,ch=0,0,0,0,0,''
    ch=chx_message(ch)
    print
    print
    print "                    ************************************************"
    print "                    *  Recherche du taux de placement d'un capital *"
    print "                    ************************************************"
    print
    print
    mot="de départ"
    cap=demande_capital(cap,mot)
    mot="final"
    cap_fin=demande_capital(cap_fin,mot)
    dur=demande_duree(dur,12)
    ta = 100*(exp(log(cap_fin/cap)/(dur/12.0))-1)
    print
    print "              +++++++++++++++++++++++++++++++++++++++++++++++++"
    print "     Le taux nécessaire à un capital de", cap,"€ pour devenir",cap_fin,"€ après", dur/12,"ans",dur%12,"mois est :"
    print "                                    %.2f" % ta,"%"
    print "              +++++++++++++++++++++++++++++++++++++++++++++++++"
    print
    print "N-B : Pour une même durée, ce résultat ne dépend que du rapport entre les capitaux d'arrivée et de départ ..."
    print
    message(ch.split(';')[0])
    return
 
def cherche_capital_depart():
    cap,ta,dur,mot,ch=0,0,0,"final",''
    ch=chx_message(ch)
    print
    print
    print "                           ************************************"
    print "                           *  Recherche du capital de départ  *"
    print "                           ************************************"
    print
    print
    cap=demande_capital(cap,mot)
    print "Taux du placement (en %)",
    ta=demande_tx(ta)
    ta=ta/100.0
    dur=demande_duree(dur,12)
    print
    print "              +++++++++++++++++++++++++++++++++++++++++++++++++"
    print "Le capital à placer pour obtenir",cap,"€ à", ta*100,"% pendant",dur/12,"ans",dur%12,"mois est :"
    v=formate(str(round(cap*(1+ta)**(-dur/12.0),2)))
    print "                                ","%11s" % v,"€"
    print "              +++++++++++++++++++++++++++++++++++++++++++++++++"
    print
    message(ch.split(';')[0])
    return
 
def cherche_capital_final():
    cap,ta,dur,mot,ch=0,0,0,"de départ",''
    ch=chx_message(ch)
    print
    print
    print "                            *******************************"
    print "                            *  Recherche du capital final  *"
    print "                            *******************************"
    print
    print
    cap=demande_capital(cap,mot)
    print "Taux du placement (en %)",
    ta=demande_tx(ta)
    ta=ta/100.0                  
    dur=demande_duree(dur,12)
    print
    print "              +++++++++++++++++++++++++++++++++++++++++++++++++"
    print "Le capital obtenu après placement de",cap,"€ à", ta*100,"% pendant",dur/12,"ans",dur%12,"mois sera :"
    v=formate(str(round(cap*(1+ta)**(dur/12.0),2)))
    print "                                ","%11s" % v,"€"
    print "              +++++++++++++++++++++++++++++++++++++++++++++++++"
    print
    message(ch.split(';')[0])
 
def cherche_duree_placement():
    cap,cap_fin,ta,dur,nbf,ch=0,0,0,0,0,''
    ch=chx_message(ch)
    print
    print
    print "                        ****************************************************"
    print "                        *  Recherche de la durée de placement d'un capital *"
    print "                        ****************************************************"
    print
    print
    mot="de départ"
    cap=demande_capital(cap,mot)
    mot="final"
    cap_fin=demande_capital(cap_fin,mot)
    print "Taux du placement (en %) ",
    ta=demande_tx(ta)
    ta=ta/100.0
    nbf=float(cap_fin/cap)
    tp= log(nbf)/log(1+ta)
    dur = int(360*tp)
    print
    print "              +++++++++++++++++++++++++++++++++++++++++++++++++"
    print "      La durée de placement à",ta*100,"% pour passer de",cap,"€ à",round(cap*(1+ta)**tp,2),"€ est :"
    print
    print "                                ",round(tp,2),"années"
    print
    print "                        Soit encore ",int(dur/360.0),"ans",int((dur%360.0)/30),"mois"
    print "              +++++++++++++++++++++++++++++++++++++++++++++++++"
    print
    print "N-B : Pour un même taux, ce résultat ne dépend que du rapport entre les capitaux d'arrivée et de départ ..."
    print
    message(ch.split(';')[0])
    return
 
def calcul_depot_constant():
    sod,sof,ta,dur,periode,mode,ca,ch=0,0,0,0,0,0,0,''
    ch=chx_message(ch)
    print
    print
    print "                       *******************************************"
    print "                       *  Placement à dépôt régulier et constant *"
    print "                       *******************************************"
    print
    periode=demande_periodicite(periode)
    dico_per={12:'mois',4:'trimestre)',2:'semestre)',1:'année'}
    dur=demande_duree(dur,periode)
    ca,sod=demande_depot(ca,sod,mode)
    print "Taux annuel du placement (en %)",
    ta=demande_tx(ta)
    q=1+ta/100.0/periode
    sof = ca*q*(q**dur-1)/(q-1)
    print
    print "              +++++++++++++++++++++++++++++++++++++++++++++++++"
    print "     Après "+str(dur)+" versements chaque "+dico_per[periode]+" de "+str(ca)+" € au taux annuel \
de "+str(ta)+" %"
    print "                     vous serez à la tête de %.2f" % sof, "€"
    print "              +++++++++++++++++++++++++++++++++++++++++++++++++"
    message(ch.split(';')[0])
    return
 
def calcul_depot_progressif():
    n,ta,sod,vsmt,q,periode,dur,ca,ch=0,0,0,0,0,0,0,0,''
    ch=chx_message(ch)
    dico_per={12:'mois',4:'trimestre',2:'semestre',1:'année'}
    print
    print
    print "                *****************************************************"
    print "                *  Placement à dépôt régulier régulier et croissant *"
    print "                           - toujours de la même somme -            *"
    print "                *****************************************************"
    print
    periode=demande_periodicite(periode)
    print "Taux annuel du placement :",
    ta=demande_tx(ta)
    print "---------------------"
    q=1+ta/100.0/periode
    n=demande_duree(dur,periode)
    mode = 0
    ca,sod=demande_depot(ca,sod,mode)
    mode=1
    ca,sod=demande_depot(ca,sod,mode)
    sof = q*((ca+sod/(q-1))*(q**n-1)/(q-1)-n*sod/(q-1))
    print
    print "              +++++++++++++++++++++++++++++++++++++++++++++++++"
    print "    Après "+str(n)+" versements de "+str(ca),str(ca+sod),str(ca+2*sod)+"..."+str(ca+(n-1)*sod)\
          +" € au taux annuel de "+str(ta)+" %"
    print "                     vous serez à la tête de %.2f" % sof, "€"
    print "              +++++++++++++++++++++++++++++++++++++++++++++++++"
    message(ch.split(';')[0])
    return
   
fin=100
while fin>0:
    titre_general()
    print " 1. Echéancier de prêt à remboursement constant"
    print " 2. Echéancier de prêt à amortissement constant"
    print " 3. Echéancier de prêt à remboursements progressifs"
    print " 4. Echéancier de prêt à remboursements \"ronds\" + reliquat"  
    print " 5. Somme obtenue après placement d'un Capital donné"
    print " 6. Somme à placer pour obtenir un Capital donné"
    print " 7. Durée nécessaire pour obtenir un Capital donné à partir d'une somme fixée"
    print " 8. Taux nécessaire pour obtenir un Capital donné à partir d'une somme fixée"
    print " 9. Capital obtenu par dépôt périodique d'une somme toujours identique"
    print "10. Capital obtenu par dépôt périodique d'une somme -également- croissante"
    print
    print "                                 0. Sortie du programme"
    chx_menu='100'
    while chx_menu=='100':
        try:
            chx_menu=raw_input("            Votre choix : ")      
            fin = int(chx_menu)
            choix2 = {'1': remboursement_constant,
                      '2': amortissement_constant,
                      '3': remboursements_progressifs,
                      '4': remboursements_ronds_reliquat,
                      '5': cherche_capital_final,
                      '6': cherche_capital_depart,
                      '7': cherche_duree_placement,
                      '8': cherche_taux,
                      '9': calcul_depot_constant,
                      '10': calcul_depot_progressif,
                      '0': sortie}
            if fin <0 or fin>10:
                chx_menu='100'
                incorrect()
        except ValueError:
            pas_nb()
    choix2[chx_menu]()
