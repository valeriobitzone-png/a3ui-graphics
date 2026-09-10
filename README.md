# a3ui-graphics

Corpo visivo / sensoriale di A3UI. **Non è A3.** Spec OS-level: vetro, geometria, motion, chrome, shader, audio, haptic. Tag **`a3ui-graphics-v0.1`**: spec. L'implementazione nel renderer sta nel repo A3 e consumerà `tokens/*.json` — non in questo tag.

A3 (`valeriobitzone-png/a3`) resta freeze. Nessun `*Spec`, nessun thaw di `a3ui/`. Catalogo invariato: `stack row list item action field text`.

Repo **private** (`git@github.com:valeriobitzone-png/a3ui-graphics.git`). Nessun push finché non deciso.

## Invarianti

| ID | Regola |
|---|---|
| GR-001 | Spec = fonte di verità. Implementazione consuma token. |
| GR-002 | Ogni livello: rationale + limiti + fase. |
| GR-003 | Token JSON versionati. Niente vetro/ombra/spring hardcoded quando A3 consumerà. |
| GR-004 | Roadmap pubblica; fasi non saltate. |

## Albero

```
docs/
  00-foundations.md        livello 1 — Fase 1
  01-micro-geometry.md     livello 2 — Fase 1 (curvature); type/icone = remainder-l2
  02-motion.md             livello 3 — S-D2
  03-micro-interactions.md livello 4 — S-D3
  04-system-chrome.md      livello 5 — S-D4
  05-shaders-vfx.md       livello 6 — S-D5
  06-audio.md              suoni — S-D5
  07-haptic.md             haptic — S-D5
  roadmap.md               fasi 1–5
tokens/                   colors elevation surfaces motion audio haptic typography
schemas/                  JSON Schema per GS-002
tests/gs_test.py
```

## Fase 1 (unica implementabile dopo questo tag, in A3)

Liquid glass base + curvature:

- Gaussian blur, vibrancy, inner/outer highlight 1px, ambient + key shadow
- Squircles, nested radius

**Vietato in v0.1 e in Fase 1 A3:** refraction, noise, shaders custom, particle, distorsione liquida, Monet, contrasto real-time, luminanza adattiva, variable fonts, icone animate, spring/morph/inertia, ripple/rubber/parallax, island/modal chrome, audio/haptic nuovi.

## Test

```
python3 tests/gs_test.py
```

GS-001 struttura · GS-002 schema JSON · GS-003 rationale/limiti/fase · GS-004 roadmap ↔ docs.

## Non fa

Secondo renderer, KMP, LICENSE pubblica, disclosure. Niente glyph inventati dall'AI.
