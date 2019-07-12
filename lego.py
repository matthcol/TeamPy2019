# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:19:45 2019

@author: Matthias
"""
from datetime import date
from PIL import Image
import re
import json
import csv



class Boite:
    """classe représentant une boîte de Lego"""
    #__slots__ = ['_numero', '_nom', 'nombrePiece', 'annee', 'image']
    
    # constructeur
    def __init__(self, numero, nom, nombrePiece=None, annee = None, image = None):
        self._numero = numero
        self._nom = nom
        self.nombrePiece = nombrePiece
        self.annee = annee
        self.image = image
        
    # properties
    @property
    def numero(self):
        return self._numero
    
    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, nom):
        if not (3 <= len(nom) <= 255):
            raise ValueError('nom de boite doit avoir entre 3 et 255 caracteres')
        self._nom = nom

    
    def __repr__(self):
        return f'BoiteLego<{self.numero} - {self.nom}>'
    
    # si on souhaite conversion en str différente de la représentation
    def __str__(self):
        nombrePieceStr = str(self.nombrePiece) if self.nombrePiece is not None else 'NC'
        anneeStr = str(self.annee) if self.annee is not None else 'NC'
        return f'{self.numero} - {self.nom} ({nombrePieceStr} p, {anneeStr})'
    
    # redéfinition de l'égalité basée sur les numéros de boîtes
    # ( opérateurs == et != )
    def __eq__(self, other):
        if not isinstance(other, Boite):
            return NotImplemented
        else:
            return self.numero == other.numero
    
    def estNouvelle(self):
        """renvoie le status nouveauté de la boîte de Lego:
        - True si l'année de la boîte est l'année courante
        - False sinon"""
        aujourdhui = date.today()
        return self.annee == aujourdhui.year
        
def pathToBoite(imagePath):
    nom = imagePath.name
    m = re.search(r'^[0-9]+', nom)
    numeroBoite = int(m.group())
    _, pos = m.span()
    fin = nom[pos+1:]
    nomTiret = re.sub(r'\.[a-z]+$','', fin, flags=re.I)
    nomBoite = re.sub(r'-', ' ', nomTiret)
    image = Image.open(imagePath)
    boite = Boite(numeroBoite, nomBoite, image=image)
    return boite

# SAUVER LA LISTE DANS UN FICHIER JSON
def toJson(listeBoite, filename):    
    liste_boite_dict = [ 
            { 'numero': boite.numero, 
              'nom' : boite.nom,
              'nombrePiece': boite.nombrePiece, 
              'annee': boite.annee } 
                        for boite in listeBoite ]
    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(liste_boite_dict, f, ensure_ascii=False)

# SAUVER LA LISTE DANS UN FICHIER CSV
def toCsv(listeBoite, filename):
    with open(filename, 'w', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(('numero','nom','nombrePiece','annee'))
        for boite in listeBoite:
            writer.writerow((boite.numero, boite.nom, boite.nombrePiece,boite.annee))
        
        
        
        
        
        
        
   

