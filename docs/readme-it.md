# Choplifter

## I - Requisiti

**Python 3** o versioni successive
> Libreria "**Pygame 2.5.0**"  
> Pacchetto "**PyInstaller 6.7.0**"  
  
## II - Comandi per CHPrompt

**1 - /clear**  
> Cancella il CHPrompt  
  
**2 - /exit**  
> Chiude il CHPrompt  
  
**3 - /help**  
> Mostra l'elenco dei comandi 
  
**4 - /play** *[ -f ]* *[ -s ]*  
> Avvia Choplifter  
> [ -f ] - Modalità a schermo intero *(sperimentale)*  
> [ -s ] - Modalità sopravvivenza 
  
**5 - /repo**  
> Restituisce il link del repository  
  
## III - Gioco  
  
### Introduzione
  
> Il gioco *Choplifter* è una simulazione di salvataggio di ostaggi con un elicottero, dove il giocatore deve evitare i nemici e salvare il maggior numero possibile di ostaggi. Questo gioco richiede Python e la libreria Pygame.  
  
### Logica del gioco
  
> **Inizializzazione**: Configurazione della finestra di gioco, caricamento delle immagini e inizializzazione delle variabili di gioco.  
> **Ciclo principale**: Gestione degli input del giocatore, aggiornamento dello stato del gioco e rendering della grafica.  
> **Gestione delle collisioni**: Rileva le collisioni tra l'elicottero, i nemici, gli ostaggi e i proiettili per gestire le interazioni.  
> **Salvataggio degli ostaggi**: L'elicottero deve atterrare vicino agli ostaggi per salvarli. Gli ostaggi si dirigono verso l'elicottero quando è a terra.  
> **Fine del gioco**: Il gioco termina quando tutti gli ostaggi sono salvati o l'elicottero è distrutto.  
  
### Elementi del gioco
  
> **Elicottero**: Il veicolo del giocatore. Può muoversi in tutte le direzioni e sparare proiettili.  
> **Nemici**: Carri armati, jet e alieni che cercano di distruggere l'elicottero.  
> **Ostaggi**: Civili da salvare. Si muovono verso l'elicottero quando atterra.  
> **Base**: Strutture dove inizialmente si trovano gli ostaggi.  
> **Proiettili**: Sparati dall'elicottero per eliminare i nemici.  
  
### Fine del gioco
  
> Il gioco termina quando tutti gli ostaggi sono salvati o l'elicottero è distrutto. Il punteggio finale, basato sul numero di ostaggi salvati e nemici distrutti, viene visualizzato sullo schermo.  
  
## IV - Sviluppatori
  
> [MOERUYONAKI](https://www.github.com/MOERUYONAKI)  
> [Kevin-Sawyer](https://www.github.com/Kevin-Sawyer)  
  