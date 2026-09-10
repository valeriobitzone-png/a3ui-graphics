# Livello 1 — Physicality & surfaces

**Level:** 1
**Phase:** `fase-1`
**Tokens:** `tokens/colors.json`, `tokens/elevation.json`, `tokens/surfaces.json`

Questo livello definisce come una superficie occupa lo spazio: vetro liquido, profondità, luce. Non è un ruolo di catalogo. I ruoli restano quelli di A3 (`stack`, `row`, `list`, `item`, `action`, `field`, `text`). Il renderer A3 consumerà questi token; questo repo non è un secondo renderer.

## Rationale

Un OS agent non poggia su Material Design. La materialità è **fisica dichiarata**: blur dello sfondo, saturazione (vibrancy), due bordi di luce da 1px, due ombre. I numeri vivono nei JSON. L'implementazione (A3) non hardcoda blur, opacità, saturazione, highlight o shadow.

La vibrancy alza la saturazione dello sfondo visto attraverso il vetro. Senza di essa il Gaussian blur produce un grigio cupo. Il boost è un coefficiente (`vibrancySaturation`), non un tint arbitrario.

## In Fase 1

- Gaussian blur real-time sul contenuto sottostante (`glass.blurRadiusPx`).
- Vibrancy: saturation boost (`vibrancySaturation`), mai desaturazione verso il fango.
- Inner highlight 1px, gradiente luce (`glass.innerHighlight`).
- Outer highlight 1px, gradiente scuro (`glass.outerHighlight`).
- Soft ambient shadow + key shadow; la direzione della key è `keyShadow.azimuthDeg` (il renderer può ricalcolarla dalla luce, il nome del token no).
- Palette statica, luminance relativa, contrasto minimo / high-contrast (`colors.json`).
- Acrylic: stessa famiglia del vetro, più opaco e più blur, per chrome denso. Non è un materiale nuovo.

## Differito (non Fase 1)

| Capacità | Phase | Perché |
|---|---|---|
| Refraction (shader custom) | `S-D5` | Livello 6. Vietato in questo tag. |
| Noise texture (micro-grana) | `S-D5` | Livello 6. Vietato in questo tag. |
| Luminanza ambientale adattiva | `S-D5` | Richiede campionamento continuo dello sfondo. |
| Color extraction (Material You / Monet) | `S-D5` | A3 non è Material. Eventuale estrazione è un adapter, non un thaw. |
| Contrasto adattivo real-time | `S-D5` | Il contrasto *minimo* di Fase 1 è statico. |

Chiavi `deferred.*` in `colors.json`, `elevation.json`, `surfaces.json` tracciano questi limiti. Non sono token da consumare.

## Limiti

- Nessun shader, refraction, noise, particle, distorsione liquida.
- Nessun colore o ombra inventato fuori da questi token.
- Glass non introduce ruoli, meanings, o un asse epistemico. LOW/UNKNOWN/CONTRADICTED restano paint del renderer A3.
- `fillOpacity` è sul fill del vetro, non sul contenuto. Il testo usa `palette.ink` su `palette.paper` (o high-contrast).
- Adaptive luminance / Monet / contrasto real-time assenti: il renderer non deve simularli.

## Fase

`fase-1`

Tracciato in `docs/roadmap.md`. Implementazione renderer: repo A3, dopo questo tag spec.
