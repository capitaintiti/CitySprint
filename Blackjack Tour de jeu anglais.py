# -*- coding:utf-8 -*-
from random import *

def tireunecarte(n):
    v = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]
    a = choice(v)
    n.append(a)
    if sommemain(n) > 21 and a == 11:
        print('draw an ace that count for 1')
        n[-1] = 1
        return n
    else:
        print('draw : ', a)
        return n
#fonction renvoyant une hauteur donnée aléatoirement entre 2 et 11 ;
#les as sont rabaissés à 1 si la somme de la main est supérieur strict à 21

def sommemain(n):
    s = 0
    for i in range(len(n)):
        s = s + n[i]
    return s

#prend en argument une suite et renvoie la somme de ses termes

def testa22homme(n):
    while sommemain(n) >= 22 and 11 in n:
        n[n.index(11)] = 1
    if sommemain(n) >= 22:
         print('you lose', sommemain(n))
         return 0
    return()

#détermine si la somme de la main est supérieur strict à 21
#affecte à la hauteur 11 la valeur 1 si la somme d ela main est supérieur strict à 21 et la main possède un 11

def testa22banque(n):
    if sommemain(n) >= 22:
         print('the bank lose', sommemain(n))
         return 1
    return()

#détermine si la somme de la main est supérieur strict à 21

def labanquetire(n):
    while sommemain(n) < 17:
        tireunecarte(n)
        print('the bank got', sommemain(n))
    return ()
    
#fonction faisant tirer des cartes à la banque tant que la main n'a pas une somme supérieur strict a 16    
    
def game(Mise):
    main_joueur = []
    main_banque = []
    print('your first card:')
    main_joueur = tireunecarte(main_joueur)
    print('your second card:')
    main_joueur = tireunecarte(main_joueur)
    print('the card of the bank:')
    main_banque = tireunecarte(main_banque)
    print('you got :',(sommemain(main_joueur)), 'and the bank got :', (sommemain(main_banque)))
    if sommemain(main_joueur) == 21 and sommemain(main_banque) !=11 :
        print('Blackjack!')
        return(5/2*Mise)
    choix_joueur = input('hit, stand, double, split?')
    while choix_joueur == 'hit':
        tireunecarte(main_joueur)
        if testa22homme(main_joueur) == 0:
            return 0
        print('the total of your hand is ', sommemain(main_joueur))
        choix_joueur = input('hit or stand?')
    if choix_joueur == 'double':
        tireunecarte(main_joueur)
        if testa22homme(main_joueur) == 0:
            return (-Mise)
        print('the total of your hand is ', sommemain(main_joueur))
        while sommemain(main_banque) <17 :
            labanquetire(main_banque)
        if testa22banque(main_banque) ==1 :
            return 4*Mise
        if sommemain(main_banque) > sommemain(main_joueur):
            print('you lose')
            return (-Mise)
        if sommemain(main_banque) == sommemain(main_joueur):
            print('equality')
            return(2*Mise)
        else:
            print('you won')
            return(4*Mise)    
    if choix_joueur == 'stand':
        while sommemain(main_banque)<17:
            labanquetire(main_banque)
        if len(main_joueur)==2 and sommemain(main_joueur)==21 and (len(main_banque)!=2 or sommemain(main_banque)!=21):
            print('Blackjack!')
            return(5/2*m)
        if testa22banque(main_banque) == 1:
            return 2*Mise
        if sommemain(main_banque) > sommemain(main_joueur):
            print('you lose')
            return 0
        if sommemain(main_banque) == sommemain(main_joueur):
            print('equality')
            return(Mise)
        else:
            print('you won')
            return(2*Mise)

#http://www.guide-blackjack.com/Statistiques-Probabiltes-blackjack.html
#le croupier s'arrete a un 17 soft ( peut avoir un as en main et ne pas tirer) 
