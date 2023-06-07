#!/usr/bin/env python
# coding: utf-8

# # Verotus

# ## Verokortti

# ```{admonition} Prosentin määritelmä
# :class: tip
# Verokortti on ohje palkansaajan ansiotulojen verotukselle.  Se sisältää kaksi veroprosenttia: perusprosentin ja 
# lisäprosentin, sekä tulorajan, jonka ylimenevälle osalle käytetään lisäprosenttia.
# 
# 1% = $\frac {1}{100} = 0.01$ 
# ```

# ## Tuloveron laskeminen verokirjan tiedoista

# ```{admonition} Maijan verokirjan perusprosentti on 28 ja lisäprosentti on 40. Tuloraja on 3600 eur/kk.  Maija ansaitsee maaliskuussa 4100 euroa.  Kuinka suuri on siitä pidätettävä vero? 
# :class: dropdown    
# Koska tulot ylittävät tulorajan, tulorajan summasta pidätetään 28% ja ylimenevästä osasta 40%     
# 
# $vero = 0.28*3600 + 0.40*(4100-3600) = 0.28*3600 + 0.40*500 = 1208 $   
# 
# Vastaus: Vero on 1208 euroa
# ```

# ## Valtionvero on progressiivinen

# Vuoden 2019 valtionverotaulukko näytti seuraavalta:
# 
# | verotettava ansiotulo | vero alarajan kohdalla | veroprosentti alarajan ylittävältä osalta |
# |-----------------------|------------------------|-------------------------------------------|
# | 17600-26400           | 8                      | 6                                         |
# | 26400-43500           | 536                    | 17.25                                     |
# | 43500-76100           | 3486                   | 21.25                                     |
# | 76100...              | 10413                  | 31.25                                     |

# ```{admonition} Pekan verotettava tulo oli vuonna 2019 41000 euroa. Laske taulukon perusteella Pekan valtiolle maksama vero kyseisenä vuonna.     
# 
# :class: dropdown      
# Pekan tulot ovat luokassa 26400 - 43500. Luokan alarajan suuruisesta osasta veroa menee 536 euroa, ja
# alarajan ylittävästä osasta 17.25 prosentin mukaan:    
# 
# Vero on siten $ 536 + 0.175*(41000 - 26400) = 3091$      
# Pekan valtionvero on siten 3091 euroa vuodessa.
# ```

# ### Montako prosenttia a on suurempi kuin b? 

# Tässä vertailuarvona on lukujen erotus ja perusarvona luku b. Ratkaisu: $\frac {a-b}{b}\cdot100\%$

# ```{admonition} Ruotsalaisten keskipalkka on 3680 Eur/kk ja suomalaisten 3570 Eur/kk. Kuinka monta prosenttia ruotsalaisten keskipalkka on suurempi kuin suomalaisten?
# :class: dropdown
# $\frac {3680-3570}{3570}\cdot100\% = 3.1\%$   
# 
# Vastaus:  3.1%
# ```

# ## Pääomatuloista maksetaan lähes tasaveroa ( jossa on tosin yksi porras)

# **Pääomatuloja ovat mm. vuokratulot, osingot ja korkotuotot**      
# 
# Pääomaveroprosentti on 30,  kun tulot ovat enintään 30000 vuodessa.      
# Rajan ylimenevältä osalta prosentti on 34.

# ```{admonition} Maijalla oli vuonna 2022 pääomatuloja 45200 euroa. Laske veron suuruus.
# :class: dropdown
# $ 0.30*30000 + 0.34*(45200-30000) = 14168 $   
# 
# Vastaus:  14168 Euroa
# ```

# ## Nettokorko pankkitalletuksesta  / sijoituksesta

# ```{admonition} Nettokorko
# :class: tip
# 30 prosentin pääomaveroa sovelletaan talletuskorkoihin.      
# 
# nettokorko = 0.7 * nimellinen korko   
# 
# Esim. jos talletuskorko olisi 3.0 %, nettokorko olisi 
# $ 0.7*3.0\% = 2.1\%$  $ 
# ```

# ## Arvonlisävero eli ALV

# ```{admonition} Maijan palkkaa korotettiin sopimuskaudella kolme kertaa. Korotukset olivat 3.0%, 2.5% ja 1.5%. Kuinka paljon Maijan palkka nousi yhteensä sopimuskaudella?
# :class: dropdown
# Koko sopimuskauden lisäyskerroin on korotuksia vastaavien lisäyskertoimien tulo. 
# $1.03\cdot1.025\cdot1.015 = 1.0716$  
# Tämä vastaan n. 7.2% palkankorotusta   
# 
# Vastaus:  7.2%
# ```

# ```{admonition} Kiinteistön arvo v.2010 oli 125000 euroa. Mikä oli kiinteistön arvo v.2018, jos oletetaan että arvo nousi tuolla aikavälillä 2.5% vuodessa? 
# :class: dropdown
# Vuotuinen lisäyskerroin on 1.025. Arvo 8 vuotta vertailuvuoden 2010 jälkeen on    
# 
# $125000\cdot1.025^8 = 152300$   
# 
# Vastaus:  152300 euroa
# ```

# ## Lahja- ja perintövero
