# Choplifter

## I - Wymagania

**Python 3** lub nowszy
> Biblioteka "**Pygame 2.5.0**"  
> Pakiet "**PyInstaller 6.7.0**"  
  
## II - Komendy dla CHPrompt

**1 - /clear**  
> Czyści CHPrompt  
  
**2 - /exit**  
> Zamyka CHPrompt  
  
**3 - /help**  
> Wyświetla listę komend 
  
**4 - /play** *[ -f ]* *[ -s ]*  
> Uruchamia grę Choplifter  
> [ -f ] - Tryb pełnoekranowy *(eksperymentalny)*  
> [ -s ] - Tryb przetrwania 
  
**5 - /repo**  
> Zwraca link do repozytorium  
  
## III - Gra  
  
### Wstęp
  
> Gra *Choplifter* to symulacja ratowania zakładników za pomocą helikoptera, gdzie gracz musi unikać wrogów i ratować jak najwięcej zakładników. Do gry potrzebny jest Python i biblioteka Pygame.
  
### Logika gry
  
> **Inicjalizacja**: Konfiguracja okna gry, wczytywanie obrazów i inicjalizacja zmiennych gry.  
> **Główna pętla**: Zarządzanie wejściami gracza, aktualizacja stanu gry i renderowanie grafiki.  
> **Zarządzanie kolizjami**: Wykrywa kolizje między helikopterem, wrogami, zakładnikami i pociskami, aby zarządzać interakcjami.  
> **Ratowanie zakładników**: Helikopter musi wylądować blisko zakładników, aby ich uratować. Zakładnicy kierują się w stronę helikoptera, gdy ten jest na ziemi.  
> **Koniec gry**: Gra kończy się, gdy wszyscy zakładnicy zostaną uratowani lub helikopter zostanie zniszczony.
  
### Elementy gry
  
> **Helikopter**: Pojazd gracza. Może poruszać się we wszystkich kierunkach i strzelać pociskami.  
> **Wrogowie**: Czołgi, odrzutowce i obce istoty próbujące zniszczyć helikopter.  
> **Zakładnicy**: Cywile do uratowania. Poruszają się w kierunku helikoptera, gdy ten ląduje.  
> **Baza**: Struktury, w których początkowo znajdują się zakładnicy.  
> **Pociski**: Strzelane przez helikopter, aby eliminować wrogów.
  
### Koniec gry
  
> Gra kończy się, gdy wszyscy zakładnicy zostaną uratowani lub helikopter zostanie zniszczony. Ostateczny wynik, oparty na liczbie uratowanych zakładników i zniszczonych wrogów, jest wyświetlany na ekranie.
  
## IV - Programiści
  
> [MOERUYONAKI](https://www.github.com/MOERUYONAKI)  
> [Kevin-Sawyer](https://www.github.com/Kevin-Sawyer)  
  