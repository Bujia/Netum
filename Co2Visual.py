# -*- coding: utf-8 -*-
"""
Bujia Guo

Tehtävänäsi on tutkia millä em. saksalaisilla autoilla (saksalaiset.txt) on suurimmat
hiilidioksidipäästöt. Miten voisit visualisoida tätä? Käytä haluamaasi kirjastoa ja esitä
vähintään yksi visualisointi, millä vastaat tehtävänantoon. Perustele lyhyesti valintasi.

Tutkin ajoneuvotiedot dataa, mitkä ovat suosituimmat automerkit, kuinka paljon niillä on ajattu keskimäärin ja niiden keskiverto päästöjä. 
Valitsin nämä, koska minua kiinnosti yleisisti minkälainen data on ja miltä se näyttää

Yritän etsiä saksalaiset.txt tiedosta top 10 päästöisintä automallia. Oletan, että automalleista löytyisi,
joku yhteinen tekijä joka vaikuttaa Co2 päästöihin.
Top 10 listalla oli 4 Sedan ja 3 avoautoa -> Voidaan olettaa että tälläiset automallit ovat keskivertoautoa korkeampi päästöisiä


"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file1 = pd.read_csv("TieliikenneAvoinData_5_8.csv", low_memory=False, delimiter=";", sep=";",encoding ="latin", 
                  usecols=["merkkiSelvakielinen", "Co2", "ensirekisterointipvm", "matkamittarilukema"])
#Dropping NaN values
file1 = file1.dropna()
#Choosing car brand only from the file
file2 = file1["merkkiSelvakielinen"]
#Getting the top 5 values
top5 = file2.value_counts().head(5)
#getting rest of the cars count
sumtop5 = top5.sum()
totalcar = len(file1.index)
other = totalcar-sumtop5
#creating the car brand dataframe
otherB = pd.DataFrame([other], index =["Other"])
brand = top5.append(otherB)
label1 = brand.index
size1 = brand.values

km = file1["matkamittarilukema"].dropna()
label2 = ["0-50000 km", "50001-100000 km", "100001-150000 km", "150001-200000 km",
        "200001-250000 km", "250001-300000 km", "> 300000 km"]
size2 = [km[(km > 0) & (km < 50000)].count(),km[(km > 50000) & (km < 100000)].count(),
            km[(km > 100000) & (km < 150000)].count(), km[(km > 150000) & (km < 200000)].count(),
            km[(km > 200000) & (km < 250000)].count(), km[(km > 250000) & (km < 300000)].count(), km[km > 300000].count()]
#Choosing Co2 from the file
co2=file1.Co2.dropna()
label3=["<=100 g/km",">100 but <=125 g/km",">125 but <=150 g/km",">150 but <=175 g/km",
       ">175 but <=200 g/km",">200 but <=225 g/km",">225 but <=250 g/km",">250 g/km"]
size3=[co2[co2<=100].count(),
      co2[(co2>100) & (co2<=125)].count(),
      co2[(co2>125) & (co2<=150)].count(),
      co2[(co2>150) & (co2<=175)].count(),
      co2[(co2>175) & (co2<=200)].count(),
      co2[(co2>200) & (co2<=225)].count(),
      co2[(co2>225) & (co2<=250)].count(),
      co2[co2>250].count()]

#Creating plots for the dataframes
plt.figure(figsize = (10,10))
plt.subplots_adjust(wspace= 0.5, hspace=0.5)
p1=plt.subplot(2,2,1)
p1.pie(size1, labels = label1, autopct= "%1.1f%%", textprops={"fontsize": 12})
p1.set_title("Car Brands", fontsize = 15)

p2=plt.subplot(2,2,2)
p2.pie(size2, labels = label2, autopct= "%1.1f%%", textprops={"fontsize": 12})
p2.set_title("Driven kilometers", fontsize = 15)

p3=plt.subplot(2,2,3)
p3.pie(size3, labels = label3, autopct= "%1.1f%%", textprops={"fontsize": 12})
p3.set_title("Co2", fontsize = 15)

#Read the txt file and naming the columns
file = pd.read_csv("saksalaiset.txt", delimiter=",", encoding ="latin", 
                   names = ["merkkiSelvakielinen", "mallimerkinta", "kunta", "Co2", "matkamittarilukema"])

#Dropping duplicates from dataframe column[mallimerkinta], so top 10 values will be unique
top10 = file.drop_duplicates(subset="mallimerkinta", keep="last")
#Finding the top 10 cars with the highest Co2 emission
cars = top10.nlargest(10, "Co2")
#setting up fig size
plt.figure(figsize=(10,5))
#fitting the Co2Max values to plot
sns.barplot(x="mallimerkinta", y='Co2', data=cars, alpha=0.8)
plt.xticks(rotation=90)
#setting up the plot
plt.title("Top 10 cars with the biggest Co2 emission")
plt.ylabel("Co2 emission value", fontsize=14)
plt.xlabel("Car model", fontsize=14)
plt.show()