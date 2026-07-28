# Visão geral do projeto

## North Star

O Football Simulation pretende se tornar uma simulação autoritativa de futebol 11 contra 11 capaz de, futuramente, sustentar realismo visual de transmissão sem permitir que renderização, animação ou ML decidam a verdade competitiva.

## Capacidade atual

A Fase 1 está ativa. O repositório contém a fundação pública, regras de contribuição e validação. Ainda não contém implementação de jogo ou simulação.

Primeiro objetivo:

```text
dois proxies corporais simplificados
+ uma bola esférica
+ estado autoritativo explícito
+ execução determinística por passo fixo
+ replay e hash de estado
+ testes e baseline reproduzível
```

A primeira unidade pronta é a [FNS-CORE-001](https://github.com/ale468/football-simulation/issues/3).

## Limites da Fase 1

Permitido:

- C++20, CMake e Ninja;
- biblioteca headless e testes;
- mundo, dois corpos e bola com estado explícito;
- tick fixo, seed, replay e hash;
- contato rígido mínimo e colisão da bola;
- C ABI pequena;
- telemetria e benchmark reproduzível.

Ainda proibido:

- gráficos, animação, áudio, UI ou engine;
- IA tática, rede, arbitragem completa ou 22 jogadores;
- ML, renderização neural, atletas reais, assets e datasets;
- orçamento absoluto arbitrário antes do primeiro baseline.

Consulte o [roadmap](PUBLIC-ROADMAP.md) e a [jornada](DEVELOPER-JOURNEY.md).
