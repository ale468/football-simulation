# Jornada do desenvolvedor

## 1. Descobrir

Leia a [visão geral](PROJECT-OVERVIEW.md), o [roadmap](PUBLIC-ROADMAP.md), licença e governança. Confirme a fase ativa e a capacidade real.

## 2. Encontrar trabalho pronto

Abra o [Project público](https://github.com/users/ale468/projects/2). Escolha somente uma Issue `READY` com problema, escopo, critérios, gate profile, impactos e evidência esperada.

## 3. Preparar

Confirme que não há decisão arquitetural pendente. Use uma branch curta por Issue e uma PR principal.

## 4. Implementar

Siga a Issue e os contratos públicos. Preserve a separação entre estado autoritativo e apresentação. Não antecipe dependências de fases futuras.

O Copilot pode receber uma Issue pronta e delimitada. Sua PR passa pelo mesmo CI e revisão humana de qualquer outra contribuição.

## 5. Validar

Execute os comandos exigidos. Antes do primeiro código:

```bash
python -B tools/repository-validation/test_validate.py
python -B tools/repository-validation/validate.py
git diff --check
```

Não declare teste ou benchmark que não foi executado.

## 6. Abrir a PR

Assine cada commit pelo DCO:

```bash
git commit --signoff -m "type: descrição concisa"
```

Complete o template, vincule a Issue, declare os gates e anexe evidência.

## 7. Revisar e integrar

CI verifica requisitos executáveis. Revisão do Copilot é consultiva; uma pessoa aprova. O método normal é squash merge.

Merge significa `IMPLEMENTED`, não automaticamente `VERIFIED` ou `DEMONSTRATED`.

## 8. Demonstrar

Verifique o estado integrado e publique evidência reproduzível antes de declarar a capacidade demonstrada.

```text
PLANNED → READY → IN PROGRESS → IN REVIEW
→ IMPLEMENTED → VERIFIED → DEMONSTRATED
```
