# -*- coding: utf-8 -*-
"""
Bujia Guo

Kirjoita tekstitiedostoon (co2ka.txt) tarvittavat otsikot sekä keskiarvo BMW, Toyota, Nissan,
Renault, Volkswagen ja Volvo -merkkisten autojen hiilidioksidipäästöistä. Kirjoita jokaisesta
automerkistä 2 eri lukua, vuoden 2017 aikana tai jälkeen rekisteröityjen autojen co2
keskiarvo sekä 2010-2016 rekisteröityjen autojen co2 keskiarvo.
Esimerkiksi: BMW >2017: xxx, 2010-2016: xxx

"""
import pandas as pd
import numpy as np
#Read csv and selecting the specific columns
file = pd.read_csv("TieliikenneAvoinData_5_8.csv", low_memory=False, delimiter=";", sep=";",encoding ="latin", 
                  usecols=["merkkiSelvakielinen", "ensirekisterointipvm", "Co2"])
#Dropping NaN values
file = file.dropna()
#Selecting the values that are between 2010-2017
start_date = "2010-1-1"
end_date = "2017-12-31"
after_start_date = file["ensirekisterointipvm"] >= start_date
before_end_date = file["ensirekisterointipvm"] <= end_date
between_two_dates = after_start_date & before_end_date
filtered_dates = file.loc[between_two_dates]
print("step1")
#Selecing specific cars manufacturers from dataframe
cars = filtered_dates.loc[file.merkkiSelvakielinen.isin(["Renault", "BMW", "Volkswagen", "Toyota", "Nissan", "Volvo"])]
#parsing the date to year specific
cars["ensirekisterointipvm"] = pd.DatetimeIndex(cars["ensirekisterointipvm"]).year
# Calcuting the counts of the cars manufacturer in 2017 and 2010-2016 (not optimal way to solve Co2 emissions answer)
BMW = cars.loc[file.merkkiSelvakielinen.isin(["BMW"])]
Renault = cars.loc[file.merkkiSelvakielinen.isin(["Renault"])]
Volkswagen = cars.loc[file.merkkiSelvakielinen.isin(["Volkswagen"])]
Toyota = cars.loc[file.merkkiSelvakielinen.isin(["Toyota"])]
Nissan = cars.loc[file.merkkiSelvakielinen.isin(["Nissan"])]
Volvo = cars.loc[file.merkkiSelvakielinen.isin(["Volvo"])]
#Cars count in 2010-2016 and 2017
BMW2017 = np.sum(BMW["ensirekisterointipvm"] == 2017)
BMW2010 = np.sum(BMW["ensirekisterointipvm"] < 2017)
Renault2017 = np.sum(Renault["ensirekisterointipvm"] == 2017)
Renault2010 = np.sum(Renault["ensirekisterointipvm"] < 2017)
Volkswagen2017 = np.sum(Volkswagen["ensirekisterointipvm"] == 2017)
Volkswagen2010 = np.sum(Volkswagen["ensirekisterointipvm"] < 2017)
Toyota2017 = np.sum(Toyota["ensirekisterointipvm"] == 2017)
Toyota2010 = np.sum(Toyota["ensirekisterointipvm"] < 2017)
Nissan2017 = np.sum(Nissan["ensirekisterointipvm"] == 2017)
Nissan2010 = np.sum(Nissan["ensirekisterointipvm"] < 2017)
Volvo2017 = np.sum(Volvo["ensirekisterointipvm"] == 2017)
Volvo2010 = np.sum(Volvo["ensirekisterointipvm"] < 2017)
#Specific cars Co2 emissions mean during 2010-2016 and 2017
Co2BMW2017 = (BMW.loc[BMW["ensirekisterointipvm"] == 2017, "Co2"].sum())/BMW2017
Co2BMW2010 = (BMW.loc[BMW["ensirekisterointipvm"] < 2017, "Co2"].sum())/BMW2010
Co2Renault2017 = (Renault.loc[Renault["ensirekisterointipvm"] == 2017, "Co2"].sum())/Renault2017
Co2Renault2010 = (Renault.loc[Renault["ensirekisterointipvm"] < 2017, "Co2"].sum())/Renault2010
Co2Volkswagen2017 = (Volkswagen.loc[Volkswagen["ensirekisterointipvm"] == 2017, "Co2"].sum())/Volkswagen2017
Co2Volkswagen2010 = (Volkswagen.loc[Volkswagen["ensirekisterointipvm"] < 2017, "Co2"].sum())/Volkswagen2010
Co2Toyota2017 = (Toyota.loc[Toyota["ensirekisterointipvm"] == 2017, "Co2"].sum())/Toyota2017
Co2Toyota2010 = (Toyota.loc[Toyota["ensirekisterointipvm"] < 2017, "Co2"].sum())/Toyota2010
Co2Nissan2017 = (Nissan.loc[Nissan["ensirekisterointipvm"] == 2017, "Co2"].sum())/Nissan2017
Co2Nissan2010 = (Nissan.loc[Nissan["ensirekisterointipvm"] < 2017, "Co2"].sum())/Nissan2010
Co2Volvo2017 = (Volvo.loc[Volvo["ensirekisterointipvm"] == 2017, "Co2"].sum())/Volvo2017
Co2Volvo2010 = (Volvo.loc[Volvo["ensirekisterointipvm"] < 2017, "Co2"].sum())/Volvo2010
#Creating dataframe
d = {"Automerkit": ["Renault", "BMW", "Volkswagen", "Toyota", "Nissan", "Volvo"], 
     "Co2 mean in 2010-2016": [int(Co2Renault2010), int(Co2BMW2010), int(Co2Volkswagen2010), int(Co2Toyota2010), int(Co2Nissan2010), int(Co2Volvo2010)],
     "Co2 mean in 2017": [int(Co2Renault2017), int(Co2BMW2017), int(Co2Volkswagen2017), int(Co2Toyota2017), int(Co2Nissan2017), int(Co2Volvo2017)]}
df = pd.DataFrame(data=d)
#writing the dataframe to txt file  
df.to_csv("co2ka.txt", sep=",", index = False)