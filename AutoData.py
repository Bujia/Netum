# -*- coding: utf-8 -*-
"""
Bujia Guo


Kirjoita tekstitiedostoon (saksalaiset.txt) Pandasin dataframea käyttäen BMW, Volkswagen
ja Audi merkkisten autojen seuraavat tiedot: Merkki, malli, kunta, hiilidioksidipäästöt (co2) ja
matkamittarilukema. Huomaa, että kunnan nimi pitää hakea kuntakoodistosta.
Esimerkiksi: BMW, 4D 318I SEDAN-VA51/276, Tampere, 175, 141984

"""
import pandas as pd
#Read csv file, selecting specific columns
file = pd.read_csv("TieliikenneAvoinData_5_8.csv", low_memory=False, delimiter=";", sep=";",encoding ="latin", 
                  usecols=["merkkiSelvakielinen", "mallimerkinta", "kunta", "Co2", "matkamittarilukema"])
#Choosing specific only german car manufacturers
cars = file.loc[file.merkkiSelvakielinen.isin(["Audi", "BMW", "Volkswagen"])]
#Read kunta page from the xlsl file
kaupungit = pd.read_excel("AjoneuvotiedotMuuttujaluettelo_31_3_2019.xlsx", sheetname="kunta", skiprows=3, usecols=range(0,2))
#Dropping NaN values
cars = cars.dropna()
#Order by manufacturers
cars = cars.sort_values(by = ["merkkiSelvakielinen"])
#looping city dataframe and matching the cars dataframe
for x in kaupungit["KOODINTUNNUS"]:
    a = 0
    a=kaupungit[kaupungit["KOODINTUNNUS"] == x].index.values
    try:
        a = int(a)
        b = kaupungit["PITKASELITE_fi"].values[a]
        #swapping the num city value to real city name
        cars.loc[(cars.kunta == x),"kunta"]= b
    except:
        pass
#writing the dataframe to txt file       
cars.to_csv("saksalaiset.txt", sep=",", header=False, index=False)