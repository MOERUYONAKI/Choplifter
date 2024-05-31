# Choplifter

## I - Vereisten

**Python 3** of een nieuwere versie
> Bibliotheek "**Pygame 2.5.0**"  
> Pakket "**PyInstaller 6.7.0**"  
  
## II - Opdrachten voor CHPrompt

**1 - /clear**  
> Maak de CHPrompt leeg  
  
**2 - /exit**  
> Sluit de CHPrompt  
  
**3 - /help**  
> Toont de lijst met opdrachten 
  
**4 - /play** *[ -f ]* *[ -s ]*  
> Start de Choplifter  
> [ -f ] - Volledig scherm modus *(experimenteel)*  
> [ -s ] - Overlevingsmodus 
  
**5 - /repo**  
> Geeft de repository link terug  
  
## III - Spel  
  
### Inleiding
  
> Het spel *Choplifter* is een gijzelingsreddingssimulatie met een helikopter, waarbij de speler vijanden moet ontwijken en zoveel mogelijk gijzelaars moet redden. Dit spel vereist Python en de Pygame-bibliotheek.
  
### Spellogica
  
> **Initialisatie**: Configuratie van het spelvenster, laden van afbeeldingen en initialisatie van spelvariabelen.  
> **Hoofdlus**: Beheer van spelerinvoer, bijwerken van de spelsituatie en weergeven van grafische elementen.  
> **Collision Management**: Detecteert botsingen tussen de helikopter, vijanden, gijzelaars en projectielen om interacties te beheren.  
> **Gijzelaars Redden**: De helikopter moet landen bij gijzelaars om ze te redden. Gijzelaars bewegen zich naar de helikopter wanneer deze aan de grond staat.  
> **Einde van het Spel**: Het spel eindigt wanneer alle gijzelaars zijn gered of de helikopter is vernietigd.
  
### Spel Elementen
  
> **Helikopter**: Het voertuig van de speler. Kan in alle richtingen bewegen en projectielen afvuren.  
> **Vijanden**: Tanks, straaljagers en buitenaardse wezens die proberen de helikopter te vernietigen.  
> **Gijzelaars**: Burgers die moeten worden gered. Ze bewegen zich naar de helikopter wanneer deze landt.  
> **Basis**: Structuren waar de gijzelaars oorspronkelijk zijn gelokaliseerd.  
> **Projectielen**: Afgevuurd door de helikopter om vijanden te elimineren.
  
### Einde van het Spel
  
> Het spel eindigt wanneer alle gijzelaars zijn gered of de helikopter is vernietigd. De uiteindelijke score, gebaseerd op het aantal geredde gijzelaars en vernietigde vijanden, wordt weergegeven op het scherm.
  
## IV - Ontwikkelaars
  
> [MOERUYONAKI](https://www.github.com/MOERUYONAKI)  
> [Kevin-Sawyer](https://www.github.com/Kevin-Sawyer)  
  