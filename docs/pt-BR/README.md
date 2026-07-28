# Football Simulation — documentação em português

Este é o ponto de entrada público em português.

## Estado atual

A **Fase 1 — Deterministic Contact Lab** está ativa. A fundação open source, a governança e a validação documental existem. Ainda não existe jogo, kernel, física, renderer, animação, ML, atleta real, asset ou dataset publicado.

O primeiro objetivo executável é um kernel headless determinístico com dois proxies corporais simplificados e uma bola. Ele criará replay, hash de estado, evidência de colisão e o primeiro baseline reproduzível de desempenho antes de gráficos, animação ou ML.

## Navegação

- [Visão geral do projeto](PROJECT-OVERVIEW.md)
- [Jornada do desenvolvedor](DEVELOPER-JOURNEY.md)
- [Gates de qualidade](QUALITY-GATES.md)
- [Gates de performance](PERFORMANCE-GATES.md)
- [Guia de evidências](EVIDENCE-GUIDE.md)
- [Roadmap público](PUBLIC-ROADMAP.md)
- [GitHub Project público](https://github.com/users/ale468/projects/2)
- [Primeira Issue pronta](https://github.com/ale468/football-simulation/issues/3)

## Regra central

O kernel autoritativo decide o que aconteceu. Apresentação, animação e ML podem representar ou auxiliar o estado, mas não decidem contato, posse, trajetória da bola, regras ou resultado competitivo.

Realismo e desempenho guiam as decisões. Ambos exigem evidência reproduzível.
