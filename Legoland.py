#!/usr/bin/env python
# coding: utf-8

# # Première(s) classe(s) en python
# ## Boîte de Lego


# librairie(s) utilisées par ce notebook
# LIRE LES IMAGES  DES BOITES DE LEGO
from pathlib import Path
import lego as lg

dirImage = Path('images')
dirImageBoite = dirImage.joinpath('boites')
dirImageTheme = dirImage.joinpath('themes')

# fabriquer la liste des objets Boite (numero, nom, image) 
# correspondant au images du répertoire dirImageBoite

listeBoite = [ lg.pathToBoite(imagePath) 
                      for imagePath in dirImageBoite.glob('*.jpg') ]

lg.toCsv(listeBoite, 'boites.csv')
lg.toJson(listeBoite, 'boites.json')

     
print("Ecriture de la liste de boite de Lego en JSON et CSV done !")
print(len(listeBoite), "boites")        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
