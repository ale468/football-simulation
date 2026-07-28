# Gates de qualidade

Um gate comprova que a mudança respeita um contrato. O perfil depende da superfície alterada.

| Perfil | Prova exigida |
|---|---|
| `DOCS` | links, rastreabilidade, estado, fronteira pública e linguagem honesta |
| `KERNEL` | builds, testes, invariantes e separação de instrumentação |
| `DETERMINISM` | seed controlada, replay e hashes aceitos idênticos |
| `ABI` | superfície exportada, ownership, versão e compatibilidade |
| `COLLISION_REALISM` | cenários, ausência de tunneling/contato fantasma e aproximações declaradas |
| `PERFORMANCE` | baseline, distribuição, ambiente e rollback |
| `ML_FUTURE` | lineage, latência, limites, consistência e fallback clássico |
| `PUBLICATION` | direitos, proveniência, scans e independência pública |

Todos os PRs exigem Issue, fase, escopo, DCO, validação, testes aplicáveis, ausência de alegações falsas e aprovação humana.

Na Fase 1, realismo significa coerência autoritativa e física, não fotorealismo. Biomecânica e aparência pertencem a fases futuras.

CI pode rejeitar uma mudança, mas não aceita arquitetura nem promove fase. Copilot é consultivo.
