# Livello 4 — Micro-interactions (feedback tattile-visivo)

**Level:** 4
**Phase:** `S-D3`
**Tokens:** `tokens/motion.json` (estensione in S-D3), `tokens/haptic.json` (consumo pieno in S-D5; qui solo il *legame* visivo)

Ripple, rubber-banding, parallasse. Sono reazioni del *corpo* della superficie, non nuovi eventi epistemici.

## Rationale

Il dito (o il puntatore) deforma il vetro e lo spazio. Senza questo livello il vetro è un blur statico. Con questo livello resta comunque grammar: l'interazione non inventa stato. A3 continua a dire se un `confirm` è vero; il ripple non autorizza.

## Differito — contenuto di S-D3

- Ripples legati al target del gesto già nel `GestureMap` A3 (niente ripple su nodi senza binding).
- Rubber-banding sui contenitori scrollabili (`list`), non sui campi.
- Parallasse tra strati di `elevation.zIndex` (content sotto glass, chrome sopra). Ampiezza da token, non da gusto.

Nessun token v0.1 extra per ripple/rubber/parallax: inventarli ora violerebbe GR-003 (token non documentati come consumabili). S-D3 *estende* `motion.json` con chiavi nuove, version bump, e aggiorna questo file.

## Limiti

- Vietato in Fase 1 e in S-D2.
- Vietato ripple come decorazione su ogni tap.
- Parallasse non sostituisce l'asse epistemico.
- Rubber-banding non è bounce di marketing: è overscroll con massa, quindi dipende da S-D2 springs.

## Fase

`S-D3`

Tracciato in `docs/roadmap.md` come Fase 3. Non saltare S-D2.
