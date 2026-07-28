# Guia de evidências

Evidência conecta uma alegação a uma observação reproduzível. Não é uma frase manual dizendo que algo “passou”.

O manifest mínimo registra:

- ID, Issue, feature, fase e commit;
- data, responsável, ambiente e hardware;
- comando ou procedimento exato;
- entrada, seed e cenário;
- resultado bruto e hashes de artefatos;
- interpretação, limitações e gate profile.

Exemplos: relatório de teste, replay, hash, log, telemetria, benchmark, ABI, sanitizer, vídeo para alegação visual e manifest de publicação.

Uma screenshot não prova determinismo. Um vídeo não prova contato autoritativo. Um FPS isolado não prova distribuição. Merge não prova capacidade. Uma frase do Copilot não prova execução.

- `IMPLEMENTED`: mudança em `main`;
- `VERIFIED`: critérios e testes aceitos passaram;
- `DEMONSTRATED`: evidência reproduzível sustenta a alegação.
