# context/ — canonical repo documentation

Stable, ground-truth documentation for PH-units. Distinct from `planning/` (in-flight work) and `docs/` (the public site published by the ph-docs hub).

`CLAUDE.md` at the repo root is the dispatcher; this folder holds the docs it routes to.

## Index

| Doc | Read when you need… |
|-----|---------------------|
| [`PRD.md`](PRD.md) | What PH-units is for and what belongs here |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | How converter / parser / `Unit` / `unit_types` fit together |
| [`TECH_STACK.md`](TECH_STACK.md) | Runtime, packaging, testing, CI, release |
| [`CODING_STANDARDS.md`](CODING_STANDARDS.md) | IPy2.7 rules, how to add a unit type, testing |

## Maintenance rule

When a change alters how conversions/aliases work, fold it into the relevant doc here. Keep it true.
