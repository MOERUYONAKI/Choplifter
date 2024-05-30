# Choplifter

## I - Vaatimukset

**Python 3** tai uudempi versio
> Kirjasto "**Pygame 2.5.0**"  
> Paketti "**PyInstaller 6.7.0**"  
  
## II - CHPrompt-komennot

**1 - /clear**  
> Tyhjentää CHPromptin  
  
**2 - /exit**  
> Sulkee CHPromptin  
  
**3 - /help**  
> Näyttää komentolistan
  
**4 - /play** *[ -f ]* *[ -s ]*  
> Käynnistää Choplifter-pelin  
> [ -f ] - Koko näytön tila *(kokeellinen)*  
> [ -s ] - Selviytymismoodi
  
**5 - /repo**  
> Palauttaa arkiston linkin  
  
## III - Peli  
  
### Johdanto
  
> *Choplifter* on panttivankien pelastussimulaatiopeli, jossa käytetään helikopteria. Pelaajan täytyy väistää vihollisia ja pelastaa mahdollisimman monta panttivankia. Tämä peli vaatii Pythonin ja Pygame-kirjaston.
  
### Pelilogiikka
  
> **Alustus**: Pelin ikkunan määritys, kuvien lataaminen ja pelimuuttujien alustaminen.  
> **Pääsilmukka**: Pelaajan syötteiden hallinta, pelin tilan päivittäminen ja grafiikan renderöinti.  
> **Törmäyksen hallinta**: Havaitsee törmäykset helikopterin, vihollisten, panttivankien ja ammuksien välillä hallitakseen vuorovaikutuksia.  
> **Panttivankien pelastus**: Helikopterin täytyy laskeutua panttivankien lähelle pelastaakseen heidät. Panttivangit liikkuvat kohti helikopteria, kun se on maassa.  
> **Pelin loppu**: Peli päättyy, kun kaikki panttivangit on pelastettu tai helikopteri on tuhottu.
  
### Pelin elementit
  
> **Helikopteri**: Pelaajan ajoneuvo. Voi liikkua kaikkiin suuntiin ja ampua ammuksia.  
> **Viholliset**: Tankit, suihkukoneet ja alienit, jotka yrittävät tuhota helikopterin.  
> **Panttivangit**: Pelastettavia siviilejä. He liikkuvat kohti helikopteria, kun se laskeutuu.  
> **Base**: Rakennelmat, joissa panttivangit alun perin sijaitsevat.  
> **Ammukset**: Helikopterin ampumat vihollisten eliminoimiseksi.
  
### Pelin loppu
  
> Peli päättyy, kun kaikki panttivangit on pelastettu tai helikopteri on tuhottu. Lopullinen pistemäärä, joka perustuu pelastettujen panttivankien ja tuhottujen vihollisten määrään, näytetään ruudulla.
  
## IV - Kehittäjät
  
> [MOERUYONAKI](https://www.github.com/MOERUYONAKI)  
> [Kevin-Sawyer](https://www.github.com/Kevin-Sawyer)  
  