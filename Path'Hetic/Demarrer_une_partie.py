from ecran_aventure import *

# Hub principal, ici on initialise les valeurs de départ du jeu.
def lejeu():
    save = []
    currentIndex = [1, 7]
    m =[["╔","═","═","═","╗","═","╗","═","╔","═","═","═","═","╗","═","═","═","╗","═","═","═","╗","═","═","═","═","═","╔","═","═","═","═","═","╔","═","═","═","═","═","═","╔","╗","","","","","",""],
        ["║","-","-","-","║","-","║","-","║","-","-","-","-","║","x","x","x","║","-","-","-","║","-","-","-","-","K","║","-","-","-","-","-","-","-","-","-","-","-","-","║","║","╔","═","╗","",""],
        ["║","-","║","F","║","-","-","-","╠","═","╔","╗","-","║","x","x","x","║","-","-","-","-","-","-","╔","═","═","╠","-","╗","-","-","-","╚","═","═","═","═","╗","-","║","║","║","?","║","",""],
        ["║","-","╠","═","╣","-","║","-","║","-","║","║","-","║","x","x","x","║","-","╔","═","═","═","╔","╣","x","x","║","-","║","-","-","-","-","-","-","-","-","║","-","║","║","║","-","║","",""],
        ["║","-","║","-","-","-","║","-","-","-","║","║","-","╚","═","═","═","╣","-","║","x","x","x","║","╠","═","═","╝","-","╠","═","╗","═","╔","═","╗","-","-","║","-","╚","╣","╠","═","╣","",""],
        ["║","-","-","-","╔","═","╣","═","═","═","╣","║","-","-","-","-","-","-","-","║","x","x","x","║","║","-","-","-","-","║","x","║","-","-","R","║","-","-","║","-","-","║","║","B","║","",""],
        ["║","═","═","-","╠","-","║","-","-","-","║","║","═","╗","═","═","═","╣","-","╚","═","╗","x","║","║","-","═","═","═","╣","x","║","-","╔","═","╣","-","-","╚","═","╔","╣","╚","═","╝","",""],
        ["║","-","-","-","║","-","║","-","═","═","║","║","-","║","-","-","-","║","-","-","-","║","x","║","║","-","-","-","-","║","x","║","-","║","x","║","-","-","-","-","║","║","","","","","",""],
        ["║","-","═","═","╣","-","-","-","-","-","║","║","-","║","-","║","-","║","-","║","-","╚","═","╣","╠","═","═","═","-","║","x","║","-","╚","═","╝","═","═","╗","-","║","║","","","","","",""],
        ["║","-","-","-","║","-","-","-","║","-","║","║","-","-","-","║","-","-","-","║","-","-","-","║","║","-","-","-","-","║","x","║","-","-","-","-","-","-","-","-","║","║","","","","","",""],
        ["╚","═","═","═","╝","═","═","═","╝","═","═","╚","═","═","═","═","═","═","═","═","═","═","═","╚","╝","═","═","═","═","╝","═","╝","═","═","═","═","═","═","╝","═","╚","╝","","","","","",""],
        ["","", "","", "", "","", "", "","", "", "","", "", "","", "", "","", "", "","", "", "","", "", "","", "", "","", "", "","", "", "","", "", "","", "", "","", "", "","", "", "","", "", ""],
        ["", "", "","", "", "Cour du batiment","", "", "","", "", "","", "", "","", "", "Coeur de l'établissement","", "", "","", "", "","", "", "","", "", "","", "", "Amphithéatre",  "", "", ""]]
    menu(save, m, currentIndex, Player)
    
    

lejeu()