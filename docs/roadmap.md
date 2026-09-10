# Roadmap — a3ui-graphics

Le fasi non si saltano (GR-004). Questo file è la traccia pubblica dei sei livelli grafici più audio e haptic.

Tag corrente: **`a3ui-graphics-v0.1`** — spec. Implementazione renderer: repo A3, non questo albero.

## Invarianti

| ID | Regola |
|---|---|
| GR-001 | Spec = fonte di verità. L'implementazione (A3 Theme / renderer) consuma `tokens/*.json`. |
| GR-002 | Ogni livello ha rationale + limiti + fase (`docs/00`–`07`). |
| GR-003 | Token JSON versionati (`version: 0.1`). Niente numeri di vetro/ombra/spring hardcoded quando A3 consumerà. |
| GR-004 | Roadmap pubblica; fasi in ordine. |

## Fasi 1–5

| Fase | Alias | Livelli | Docs | Token | Stato in v0.1 |
|---|---|---|---|---|---|
| 1 | `fase-1` | L1 fondamenti liquid glass; L2 curvature | `00-foundations.md`, `01-micro-geometry.md` | `colors`, `elevation`, `surfaces` (chiavi non-deferred) | **Spec chiusa.** Renderer A3: non in questo tag. |
| 2 | `S-D2` | L3 spring, morphing, inertia | `02-motion.md` | `motion.json` | Differito. File presente, `status: deferred`. |
| 3 | `S-D3` | L4 ripples, rubber-banding, parallasse | `03-micro-interactions.md` | estensione `motion.json` (bump futuro) | Differito. Nessun token extra in v0.1. |
| 4 | `S-D4` | L5 pannelli, island, modal, notification chrome | `04-system-chrome.md` | `surfaces` + `elevation` (z chrome/overlay già nominati) | Differito. |
| 5 | `S-D5` | L6 shaders/VFX; L7 audio; L7 haptic | `05-shaders-vfx.md`, `06-audio.md`, `07-haptic.md` | `audio.json`, `haptic.json`; `deferred.*` su surfaces/colors/elevation | Differito. Vietato refraction/noise/shaders ora. |

## Remainder L2 (non è un salto)

Dopo Fase 1 e **prima** di `S-D2` (`remainder-l2`):

- Variable fonts + optical sizing (`typography.json`, `phase: remainder-l2`, `status: deferred`)
- Icone animate / glifi stratificati (niente glyph AI)

`docs/01-micro-geometry.md` e `tokens/typography.json` tracciano questo blocco. Non è Fase 2: S-D2 è motion.

## Copertura livelli ↔ docs

| Livello | Doc | Phase dichiarata |
|---|---|---|
| 1 physicality | `docs/00-foundations.md` | `fase-1` |
| 2 micro-geometry | `docs/01-micro-geometry.md` | `fase-1` |
| 3 motion | `docs/02-motion.md` | `S-D2` |
| 4 micro-interactions | `docs/03-micro-interactions.md` | `S-D3` |
| 5 system chrome | `docs/04-system-chrome.md` | `S-D4` |
| 6 shaders/vfx | `docs/05-shaders-vfx.md` | `S-D5` |
| 7 audio | `docs/06-audio.md` | `S-D5` |
| 7 haptic | `docs/07-haptic.md` | `S-D5` |

## Differiti espliciti (non Fase 1)

Da L1: refraction, noise, luminanza ambientale adattiva, Monet/color extraction, contrasto adattivo real-time.

Da L2: variable type, optical sizing, icone animate.

Da L3–L7: tutto il contenuto dei docs `02`–`07`.

## Gate v0.1

`python3 tests/gs_test.py`

- GS-001 struttura (`docs/` + `tokens/` + `docs/roadmap.md`)
- GS-002 JSON validi contro `schemas/`
- GS-003 ogni livello: rationale + limiti + fase
- GS-004 roadmap coerente con i docs (tutti i livelli tracciati)

PASS → tag locale `a3ui-graphics-v0.1`. Nessun push finché non deciso.
