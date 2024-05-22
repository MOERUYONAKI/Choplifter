# Choplifter

## I - Requirements

**Python 3** or later
> "**Pygame 2.5.0**" lib  
  
## II - Commands for CHPrompt

**1 - /clear**  
> Clear the CHPrompt  
  
**2 - /exit**  
> Close the CHPrompt  
  
**3 - /help**  
> Give the commands list  
  
**4 - /play** *[ -f ]* *[ -s ]*  
> Start the Choplifter game  
> [ -f ] - Fullscreen mode *(experimental)*  
> [ -s ] - Survival mode  
  
**5 - /repo**  
> Return the repository link  
  
## III - Game  
  
### Introduction
  
> *Choplifter* is a hostage rescue simulation game using a helicopter, where the player must evade enemies and save as many hostages as possible. This game requires Python and the Pygame library.  
  
### Game Logic
  
> **Initialization**: Setting up the game window, loading images, and initializing game variables.  
> **Main Loop**: Managing player inputs, updating game state, and rendering graphics.  
> **Collision Management**: Detects collisions between the helicopter, enemies, hostages, and projectiles to manage interactions.  
> **Hostage Rescue**: The helicopter must land near hostages to save them. Hostages move towards the helicopter when it is on the ground.  
> **End of Game**: The game ends when all hostages are rescued or the helicopter is destroyed.  
  
### Game Elements
  
> **Helicopter**: The player's vehicle. Can move in all directions and fire projectiles.  
> **Enemies**: Tanks, jets, and aliens trying to destroy the helicopter.  
> **Hostages**: Civilians to be rescued. They move towards the helicopter when it lands.  
> **Base**: Structures where hostages are initially located.  
> **Projectiles**: Fired by the helicopter to eliminate enemies.  
  
### End of Game
  
> The game ends when all hostages are rescued or the helicopter is destroyed. The final score, based on the number of hostages saved and enemies destroyed, is displayed on the screen.  
  
## IV - Developers
  
> [MOERUYONAKI](https://www.github.com/MOERUYONAKI)  
> [Kevin-Sawyer](https://www.github.com/Kevin-Sawyer)  
  