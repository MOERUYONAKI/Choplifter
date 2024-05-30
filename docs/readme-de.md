# Choplifter

## I - Anforderungen

**Python 3** oder höher
> "**Pygame 2.5.0**" Bibliothek  

## II - Befehle für CHPrompt

**1 - /clear**  
> Löscht den CHPrompt  
  
**2 - /exit**  
> Schließt den CHPrompt  
  
**3 - /help**  
> Gibt die Befehlsliste aus  
  
**4 - /play** *[ -f ]* *[ -s ]*  
> Startet das Choplifter-Spiel  
> [ -f ] - Vollbildmodus *(experimentell)*  
> [ -s ] - Überlebensmodus  
  
**5 - /repo**  
> Gibt den Repository-Link zurück  
  
## III - Spiel  

### Einführung
  
> *Choplifter* ist ein Simulationsspiel zur Geiselrettung mit einem Hubschrauber, bei dem der Spieler Feinden ausweichen und so viele Geiseln wie möglich retten muss. Dieses Spiel erfordert Python und die Pygame-Bibliothek.  
  
### Spiel-Logik
  
> **Initialisierung**: Einrichtung des Spiel-Fensters, Laden von Bildern und Initialisierung der Spielvariablen.  
> **Hauptschleife**: Verwaltung der Spielereingaben, Aktualisierung des Spielzustands und Rendern der Grafiken.  
> **Kollisionsmanagement**: Erkennt Kollisionen zwischen dem Hubschrauber, Feinden, Geiseln und Projektilen, um Interaktionen zu verwalten.  
> **Geiselrettung**: Der Hubschrauber muss in der Nähe der Geiseln landen, um sie zu retten. Geiseln bewegen sich zum Hubschrauber, wenn er am Boden ist.  
> **Spielende**: Das Spiel endet, wenn alle Geiseln gerettet oder der Hubschrauber zerstört ist.  
  
### Spielelemente
  
> **Hubschrauber**: Das Fahrzeug des Spielers. Kann sich in alle Richtungen bewegen und Projektile abfeuern.  
> **Feinde**: Panzer, Jets und Aliens, die versuchen, den Hubschrauber zu zerstören.  
> **Geiseln**: Zivilisten, die gerettet werden müssen. Sie bewegen sich zum Hubschrauber, wenn er landet.  
> **Basis**: Strukturen, in denen sich die Geiseln ursprünglich befinden.  
> **Projektilen**: Vom Hubschrauber abgefeuert, um Feinde zu eliminieren.  
  
### Spielende
  
> Das Spiel endet, wenn alle Geiseln gerettet oder der Hubschrauber zerstört ist. Die Endpunktzahl, basierend auf der Anzahl der geretteten Geiseln und der zerstörten Feinde, wird auf dem Bildschirm angezeigt.  
  
## IV - Entwickler
  
> [MOERUYONAKI](https://www.github.com/MOERUYONAKI)  
> [Kevin-Sawyer](https://www.github.com/Kevin-Sawyer)  
  