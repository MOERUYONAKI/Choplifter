# Choplifter

## I - Requisitos

**Python 3** o posterior  
> Librería "**Pygame 2.5.0**"  
> Paquete "**PyInstaller 6.7.0**"  

## II - Comandos para CHPrompt

**1 - /clear**  
> Limpia el CHPrompt  

**2 - /exit**  
> Cierra el CHPrompt  

**3 - /help**  
> Muestra la lista de comandos  

**4 - /play** *[ -f ]* *[ -s ]*  
> Inicia el juego de Choplifter  
> [ -f ] - Modo pantalla completa *(experimental)*  
> [ -s ] - Modo supervivencia  

**5 - /repo**  
> Devuelve el enlace del repositorio  

## III - Juego  

### Introducción  

> *Choplifter* es un juego de simulación de rescate de rehenes usando un helicóptero, donde el jugador debe evadir enemigos y salvar la mayor cantidad posible de rehenes. Este juego requiere Python y la librería Pygame.  

### Lógica del Juego  

> **Inicialización**: Configuración de la ventana del juego, carga de imágenes e inicialización de variables del juego.  
> **Bucle Principal**: Manejo de entradas del jugador, actualización del estado del juego y renderizado de gráficos.  
> **Gestión de Colisiones**: Detecta colisiones entre el helicóptero, enemigos, rehenes y proyectiles para gestionar las interacciones.  
> **Rescate de Rehenes**: El helicóptero debe aterrizar cerca de los rehenes para rescatarlos. Los rehenes se mueven hacia el helicóptero cuando está en el suelo.  
> **Fin del Juego**: El juego termina cuando todos los rehenes son rescatados o el helicóptero es destruido.  

### Elementos del Juego  

> **Helicóptero**: El vehículo del jugador. Puede moverse en todas las direcciones y disparar proyectiles.  
> **Enemigos**: Tanques, jets y alienígenas que intentan destruir el helicóptero.  
> **Rehenes**: Civiles que deben ser rescatados. Se mueven hacia el helicóptero cuando aterriza.  
> **Base**: Estructuras donde se encuentran inicialmente los rehenes.  
> **Proyectiles**: Disparados por el helicóptero para eliminar enemigos.  

### Fin del Juego  

> El juego termina cuando todos los rehenes son rescatados o el helicóptero es destruido. La puntuación final, basada en el número de rehenes salvados y enemigos eliminados, se muestra en la pantalla.  

## IV - Desarrolladores  

> [MOERUYONAKI](https://www.github.com/MOERUYONAKI)  
> [Kevin-Sawyer](https://www.github.com/Kevin-Sawyer)  
  