# Choplifter

## I - Krav

**Python 3** eller en nyere version
> Bibliotek "**Pygame 2.5.0**"  
> Pakke "**PyInstaller 6.7.0**"  
  
## II - Kommandoer til CHPrompt

**1 - /clear**  
> Ryd CHPrompt  
  
**2 - /exit**  
> Luk CHPrompt  
  
**3 - /help**  
> Viser kommandooversigten
  
**4 - /play** *[ -f ]* *[ -s ]*  
> Start Choplifter  
> [ -f ] - Fuldskærmstilstand *(eksperimentel)*  
> [ -s ] - Overlevelsestilstand
  
**5 - /repo**  
> Returnerer linket til repository'et  
  
## III - Spil  
  
### Introduktion
  
> Spillet *Choplifter* er en gidselredningssimulation ved hjælp af en helikopter, hvor spilleren skal undgå fjender og redde så mange gidsler som muligt. Dette spil kræver Python og Pygame-biblioteket.
  
### Spil Logik
  
> **Initialisering**: Opsætning af spilvinduet, indlæsning af billeder og initialisering af spilvariabler.  
> **Hovedloop**: Håndtering af spillerens input, opdatering af spiltilstand og rendering af grafik.  
> **Kollisionshåndtering**: Registrerer kollisioner mellem helikopteren, fjender, gidsler og projektiler for at håndtere interaktioner.  
> **Gidselredning**: Helikopteren skal lande nær gidslerne for at redde dem. Gidslerne bevæger sig mod helikopteren, når den er på jorden.  
> **Spil Slut**: Spillet slutter, når alle gidsler er reddet, eller helikopteren er ødelagt.
  
### Spilelementer
  
> **Helikopter**: Spillerens køretøj. Kan bevæge sig i alle retninger og skyde projektiler.  
> **Fjender**: Tanke, jetfly og rumvæsner, der forsøger at ødelægge helikopteren.  
> **Gidsler**: Civile, der skal reddes. De bevæger sig mod helikopteren, når den lander.  
> **Base**: Strukturer, hvor gidslerne oprindeligt er placeret.  
> **Projektiler**: Affyres af helikopteren for at eliminere fjender.
  
### Spil Slut
  
> Spillet slutter, når alle gidsler er reddet, eller helikopteren er ødelagt. Den endelige score, baseret på antallet af reddede gidsler og ødelagte fjender, vises på skærmen.
  
## IV - Udviklere
  
> [MOERUYONAKI](https://www.github.com/MOERUYONAKI)  
> [Kevin-Sawyer](https://www.github.com/Kevin-Sawyer) 
  