# Gates de performance

Performance é requisito arquitetural, mas um número sem ambiente reproduzível não é gate confiável.

O primeiro benchmark da Fase 1 cria o baseline. O computador do proprietário é a referência inicial. Runners compartilhados do GitHub provam build e correção e podem detectar regressão grosseira, mas não definem orçamento absoluto.

Todo resultado registra:

- commit, compilador, flags e build;
- sistema operacional e hardware;
- cenário, tick, seed e entrada;
- aquecimento, repetições e duração;
- mediana, p95, p99 e throughput;
- memória, alocações e dispersão;
- resultado bruto, limitações e rollback.

Uma mudança de performance declara gargalo observado, baseline, mecanismo causal, invariantes de autoridade/realismo/determinismo, impactos esperados e critério derivado de evidência.

Uma otimização mais rápida que falsifique o estado autoritativo, a física aceita ou o replay determinístico falha no gate.
