# IA-trabalho2

## Questão Busca Adversarial

Jogo implementado: Breakthrough 

Arquivos criados:
* breakthrough.py -> implementação do jogo e suas regras
* play_breakthrough_minimax_with_hef -> implementação de um jogo com um agente IA com minimax com função heurística de avaliação
* play_breakthrough_mcts -> implementação de um jogo com um agente IA com mcts com número fixo de avaliações
* play_breakthrough -> implementação de um menu com opções para escolha de modo de jogo

## Questão Aprendizado por Reforço

###  Q-learning Tabular: Replicação de Experimentos

1. Implementação dos novos ambientes
* cliff_walking_environment.py
* frozen_lake_environment

2. Foi preciso adicionar os novos ambientes no dicionário de tq train

3. Treinamento e Teste

* Blackjack
python tql_train.py --env_name Blackjack-v1 --num_episodes 10000
python tql_test.py --env_name Blackjack-v1 --num_episodes 1000

Desempenho ruim, pois o valor de -0.159 indica que perdeu mais do que ganhou
Esse desempenho ruim já era esperado pois esse ambientem tem muitos estados possíveis e resultados incertos (devido ao sorteio das cartas)

* CliffWalking
python tql_train.py --env_name CliffWalking-v0 --num_episodes 10000
python tql_test.py --env_name CliffWalking-v0 --num_episodes 1000

A recompensa média de -13 mostra que o agente aprendeu a chegar no ambiente sem cair, mas não está buscando otimizar o caminho, o que é esperado com configurações padrão e sem ajustes finos 

* Frozen Lake
python tql_train.py --env_name FrozenLake-v1 --num_episodes 10000
python tql_test.py --env_name FrozenLake-v1 --num_episodes 1000

O fozen lake tem uma recompensa média de 0.132, ou seja, chegou ao objetivo em 13% dos casos. E o tamanho médio dos episódios é 14, mostrando que o  agente aprendeu a identificar as ações vantajosas próximas ao objetivo

### Q-learning Tabular: Discretização de Estados

1. Imprementação do ambiente Mountain Car
mountaincair_environment.py