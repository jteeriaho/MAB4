#!/usr/bin/env python
# coding: utf-8

# # Koronkorko      
# 
# ## Koronkorkolaskut

# ### Korkolaskuissa käytettävät symbolit

# > k = nykyarvo (investoitu summa, alkupääoma)       
# >
# > K = tuleva arvo (karttunut pääoma)    
# >
# > i = korkokanta (laskuissa desimaalimuodossa: esim. 5% = 0.05)      
# >
# > t = aika, korkojaksojen lukumäärä      
# 
# 
# Em. lisäksi kaavoissa käytetään usein symbolia r, jonka laskukaava on r = 1 + i.       
# Sitä nimitetään *lisäyskertoimeksi* tai *korkotekijäksi*.

# ### Tulevan arvon laskeminen koronkorkomenetelmällä

# > **Koronkorkomenetelmässä** kunkin korkojakson lopussa pääomaan liitetään korko.      
# > Seuraavan korkojakson aikana korkoa kertyy alkuperäisen pääoman ja siihen liitetyn koron yhteissummalle. 

# ```{admonition} **Tulevan arvon laskeminen**
# :class: tip
#  
# Tuleva arvo $K = k\cdot (1+i)^t$     
# 
# k = nykyarvo, i = korkokanta, t = aika (korkojaksojen lukumäärä)
# 
# ```

# ```{admonition} Esim. Irina tallentaa pankin säästötilille 5000 Euroa 5 vuodeksi. Korkoprosentti on 2.5% p.a *(per annum = vuodessa)*. Laske säästötilin saldo 5 vuoden kuluttua Euron tarkkuudella       
# :class: dropdown
# Tehtävässä annettua korkoa vastaava korkotekijä r = 1 + i = 1.025.   
#      
# Loppusaldo $K = k\cdot (1+i)^t = 5000\cdot 1.025^5 = 5657$
# ```

# ### Nykyarvon laskeminen (diskonttaus)

# Kun halutaan tietää esim. jonkin tulevan tuoton arvo nykyhetkellä, tarvitaan **nykyarvon laskemista eli diskonttausta** 

# ```{admonition} **Nykyarvon laskukaava**
# :class: tip
#  
# Nykyarvo $k = \frac{K}{(1+i)^t}\hspace{1cm}$ joka voidaan esittää myös muodossa       
# 
# $k = K {(1+i)}^{-t} $      
# 
# K = tuleva arvo, i = korkokanta, t = aika (korkojaksojen lukumäärä)
# 
# ```

# ```{admonition} Paavo sijoittaa 20000 € kohteeseen, josta arvioi saavansa 24000 € myydessään sen 5 v kuluttua. Paavo tavoittelee 4.0% prosentin voittoa investoinnille. Toteutuuko tavoite?
# :class: dropdown
# 
# Lasketaan myyntihinnan nykyarvo 4 % korkokannalla. $k = K {(1+i)}^{-t} = 24000\hspace{1mm} {1.04}^{-5} = 19726$              
# 
# Myyntihinnan nykyarvo on pienempi kuin investoitu summa 20000, joten Paavon tavoite ei toteudu.
# ```

# ###  Korkokannan i ratkaiseminen koronkorkokaavasta

# ```{admonition} **Korkokannan (eli korkoprosentin) laskeminen**
# :class: tip
#  
# Korkokanta $i = \sqrt[t]{\frac{K}{k}}-1$  
# 
# K = tuleva arvo, k=nykyarvo, t = aika (korkojaksojen lukumäärä)
# 
# ```

# *Kaavan perustelu:*     
# $K = k {(1+i)}^{t} \Rightarrow \frac{K}{k} = (1+i)^t \Rightarrow 1+i=\sqrt[t]{\frac{K}{k}}\Rightarrow i = \sqrt[t]{\frac{K}{k}}-1 $     

# ```{admonition} Paavo sijoittaa 20000 € kohteeseen, josta arvioi saavansa 24000 € myydessään sen 5 v kuluttua. Paavo tavoittelee 4.0% prosentin voittoa investoinnille. Toteutuuko tavoite? Laske Paavon saama todellinen korko?
# :class: dropdown
# 
# Lasketaan Paavon saama todellinen korko. $i = \sqrt[t]{\frac{K}{k}}-1 =\sqrt[t]{\frac{24000}{25000}}-1 = 0.037=3.7\%$              
# 
# Todellinen korko jää alle Paavon tavoitteen.
# ```

# ###  Ajan ratkaiseminen koronkorkokaavasta

# Jos halutaan laskea, missä ajassa alkupääoma k karttuu arvoon K korkokannalla i, pitää ratkaista koronkorkokaava ajan t suhteen

# ```{admonition} **Ajan laskeminen**
# :class: tip
#  
# Aika (=korkojaksojen määrä)  $t = \frac {log(\frac{K}{k})}{log(1+i)}$  
# 
# K = tuleva arvo, k=nykyarvo, t = aika (korkojaksojen lukumäärä)
# 
# ```

# *Kaavan perustelu:*     
# $K = k {(1+i)}^{t} \Rightarrow \frac{K}{k} = (1+i)^t \Rightarrow log(\frac{K}{k})= log((1+i)^t)= t\hspace{1mm} log(1+i)\Rightarrow t = \frac {ln(\frac{K}{k})}{ln(1+i)} $

# ```{admonition} Annen auton arvo on nyt 5000 €. Monenko vuoden kuluttua arvo on enää 1000 € olettaen, että ko. automallin arvo putoaa 15% vuodessa?
# :class: dropdown
# Korko on tässä tapauksessa negatiivinen luku -0.015, joten korkotekijä 1 + i = 0.85        
# 
# $t = \frac {log(\frac{K}{k})}{log(1+i)} =  \frac {log(\frac{1000}{5000})}{log(0.85)} = 9.9 $       
# 
# Vastaus:  9.9 vuoden kuluttua.
# 
# 
# ```

# ## Annuiteettilaina eli tasaerälaina

# Nykyisin yleisin lainamuoto asunto- ja kulutusluotoissa on **tasaerälaina**, jossa laina maksetaan takaisin koko laina-ajan samansuuruisina pysyvinä suorituksina, jotka sisältävät sekä lyhennyksen että koron.    
# 
# Alla on kaava maksuerän suuruuden laskemiseen.  Kaava voidaan johtaa käyttämällä geometrisen sarjan summan kaavaa, joka löytyy kaavakirjoista. 

# ```{admonition} **Tasaerälainan maksuerän laskukaava**
# :class: tip  
# 
# $p=\frac{k\hspace{1mm}i}{1-(1+i)^{-n}}$      
# 
# k = lainamäärä, i = korkojakson korkoprosentti, n = erien määrä    
# 
# Huom! Kaavaa vastaava Excel funktio on MAKSU (engl. Excelissä PMT)
# ```

# ```{admonition} Esim. Maija ostaa tietokoneen luotolla, jonka maksuaika on 18 kk. Luottosumma on 800 Euroa, korko 6% vuodessa eli 0.5% kk:ssa. Mikä on kuukausierän suuruus?
# :class: dropdown
# 
# Periaate:  Maksuerien nykyarvojen summan on oltava yhtäsuuri kuin ostohinta.     
# 
# Kuukausierä p on yhtälön $800 = \frac {p}{1.005}+ \frac {p}{1.005^2} + ... + \frac {p}{1.005^18}$ ratkaisu. 
# 
# Yhtälö on liian pitkä laskimella ratkaistavaksi. Käytetään **tasaerän laskukaavaa**   
# 
# $p=\frac{k\hspace{1mm}i}{1-(1+i)^{-n}}$, missä k = lainattu summa, i = lyhennyskauden korko,     
# n = lyhennysten lukumäärä     
# 
# Sijoitusten jälkeen saadaan tasaeräksi $p= \frac{800\hspace{1mm}\cdot \hspace{1mm}0.005}{1-1.005^{-18}} = 46.59 $     
# 
# Excel-ratkaisu: $\color{blue}{\text{=MAKSU(0,5%;18;800)}}$
# 
# ```

# ```{admonition} **Tasaerälaina, jossa viimeiseen erään on lisätty lainan jäännösarvo**
# :class: tip  
# 
# $p=\frac{k\hspace{1mm}i-K\hspace{1mm}i (1+i)^{-n}}{1-(1+i)^{-n}}$      
# 
# k = lainamäärä, i = korkojakson korkoprosentti, n = erien määrä, K = jäännösarvo    
# 
# Huom! Kaavaa vastaava Excel funktio on MAKSU (engl. Excelissä PMT)   
#    
# ```

# ```{admonition} Esim. Eero ostaa vaihtoauton osamaksulla, jonka maksuaika on 36 kk. Luottosumma on 6000 euroa, korko 6% vuodessa eli 0.5% kk:ssa. Mikä on kuukausierän suuruus, kun viimeiseen erään on lisätty jäännösarvo 2000 euroa?
# :class: dropdown
# 
# Periaate:  Maksuerien nykyarvojen summan on oltava yhtäsuuri kuin ostohinta.     
# 
# Käytetään **laskukaavaa**   
# 
# $p=\frac{k\hspace{1mm}i-K\hspace{1mm}i (1+i)^{-n}}{1-(1+i)^{-n}}$, missä k = lainattu summa, i = lyhennyskauden korko,       
# n = lyhennysten lukumäärä (laina-aika) ja K on viimeiseen erään lisätty ns. jäännösarvo     
# 
# Sijoitusten jälkeen saadaan tasaeräksi 
# $p=\frac{6000\hspace{1mm}0.05-2000\hspace{1mm}0.005\cdot 1.005^{-36}}{1-1.005^{-36}} = 131.69 $      
# 
# Excel-ratkaisu: $\color{blue}{\text{=MAKSU(0,5%;36;5000,-2000)}}$
# 
# ```
