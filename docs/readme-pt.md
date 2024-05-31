# Choplifter

## I - Requisitos

**Python 3** ou uma versão mais recente
> Biblioteca "**Pygame 2.5.0**"  
> Pacote "**PyInstaller 6.7.0**"  
  
## II - Comandos do CHPrompt

**1 - /clear**  
> Limpa o CHPrompt  
  
**2 - /exit**  
> Fecha o CHPrompt  
  
**3 - /help**  
> Exibe a lista de comandos
  
**4 - /play** *[ -f ]* *[ -s ]*  
> Inicia o Choplifter  
> [ -f ] - Modo tela cheia *(experimental)*  
> [ -s ] - Modo sobrevivência
  
**5 - /repo**  
> Retorna o link do repositório  
  
## III - Jogo  
  
### Introdução
  
> O jogo *Choplifter* é uma simulação de resgate de reféns usando um helicóptero, onde o jogador deve evitar inimigos e salvar o máximo de reféns possível. Este jogo requer Python e a biblioteca Pygame.
  
### Lógica do jogo
  
> **Inicialização**: Configuração da janela do jogo, carregamento das imagens e inicialização das variáveis do jogo.  
> **Loop principal**: Gerenciamento das entradas do jogador, atualização do estado do jogo e renderização dos gráficos.  
> **Gerenciamento de colisões**: Detecta colisões entre o helicóptero, inimigos, reféns e projéteis para gerenciar interações.  
> **Resgate de reféns**: O helicóptero deve pousar perto dos reféns para salvá-los. Os reféns se dirigem ao helicóptero quando ele está no chão.  
> **Fim do jogo**: O jogo termina quando todos os reféns são resgatados ou o helicóptero é destruído.
  
### Elementos do jogo
  
> **Helicóptero**: O veículo do jogador. Pode se mover em todas as direções e disparar projéteis.  
> **Inimigos**: Tanques, jatos e alienígenas tentando destruir o helicóptero.  
> **Reféns**: Civis a serem resgatados. Eles se movem em direção ao helicóptero quando ele pousa.  
> **Base**: Estruturas onde os reféns estão inicialmente localizados.  
> **Projéteis**: Disparados pelo helicóptero para eliminar os inimigos.
  
### Fim do jogo
  
> O jogo termina quando todos os reféns são resgatados ou o helicóptero é destruído. A pontuação final, baseada no número de reféns salvos e inimigos destruídos, é exibida na tela.
  
## IV - Desenvolvedores
  
> [MOERUYONAKI](https://www.github.com/MOERUYONAKI)  
> [Kevin-Sawyer](https://www.github.com/Kevin-Sawyer)  
  