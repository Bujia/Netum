# Netum coding exercise

Data is from https://www.traficom.fi/fi/ajankohtaista/avoin-data?toggle=Ajoneuvojen%20avoin%20data%205.8

Tehtävänäsi on tutkia millä em. saksalaisilla autoilla (saksalaiset.txt) on suurimmat
hiilidioksidipäästöt. Miten voisit visualisoida tätä? Käytä haluamaasi kirjastoa ja esitä
vähintään yksi visualisointi, millä vastaat tehtävänantoon. Perustele lyhyesti valintasi.
Tutkin ajoneuvotiedot dataa, mitkä ovat suosituimmat automerkit, kuinka paljon niillä on ajattu keskimäärin ja niiden keskiverto päästöjä. 
Valitsin nämä, koska minua kiinnosti yleisisti minkälainen data on ja miltä se näyttää
Yritän etsiä saksalaiset.txt tiedosta top 10 päästöisintä automallia. Oletan, että automalleista löytyisi,
joku yhteinen tekijä joka vaikuttaa Co2 päästöihin.
Top 10 listalla oli 4 Sedan ja 3 avoautoa -> Voidaan olettaa että tälläiset automallit ovat keskivertoautoa korkeampi päästöisiä

Kirjoita tekstitiedostoon (co2ka.txt) tarvittavat otsikot sekä keskiarvo BMW, Toyota, Nissan,
Renault, Volkswagen ja Volvo -merkkisten autojen hiilidioksidipäästöistä. Kirjoita jokaisesta
automerkistä 2 eri lukua, vuoden 2017 aikana tai jälkeen rekisteröityjen autojen co2
keskiarvo sekä 2010-2016 rekisteröityjen autojen co2 keskiarvo.
Esimerkiksi: BMW >2017: xxx, 2010-2016: xxx

Kirjoita tekstitiedostoon (saksalaiset.txt) Pandasin dataframea käyttäen BMW, Volkswagen
ja Audi merkkisten autojen seuraavat tiedot: Merkki, malli, kunta, hiilidioksidipäästöt (co2) ja
matkamittarilukema. Huomaa, että kunnan nimi pitää hakea kuntakoodistosta.
Esimerkiksi: BMW, 4D 318I SEDAN-VA51/276, Tampere, 175, 141984
