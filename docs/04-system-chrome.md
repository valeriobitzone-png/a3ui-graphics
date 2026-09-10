# Livello 5 — System chrome (pannelli, island, modal)

**Level:** 5
**Phase:** `S-D4`
**Tokens:** `tokens/surfaces.json`, `tokens/elevation.json` (consumo chrome: `zIndex.chrome`, `zIndex.overlay`)

Pannelli di sistema, compact status (dynamic island come *trattamento*, non come prodotto Apple), modal backdrop, notification chrome. Overlay A3 (`approve` / `return`) esiste già: questo livello ne specifica il vetro, non la semantica.

## Rationale

Il chrome è OS-level: sta sopra il catalogo, non *è* catalogo. `zIndex.chrome` e `zIndex.overlay` esistono in Fase 1 così la stratificazione è dichiarata; il morphing a island, il backdrop modale e il notification chrome aspettano S-D4 perché richiedono motion (S-D2) e micro-interazioni (S-D3).

## Differito — contenuto di S-D4

- Compact status / dynamic island: collasso di chrome in una capsula squircle, non un nuovo ruolo.
- Modal backdrop: vetro + blur sui token Fase 1, più scrim da `elevation` / opacità dichiarata in S-D4.
- Notification chrome: stessa famiglia glass, `zIndex.chrome`.

## Limiti

- Nessun ruolo `island`, `modal`, `toast` nel catalogo A3.
- Overlay `approve` / `return` restano fallback semantici A3; S-D4 cambia solo materializzazione.
- Vietato copiare UI kit iOS/Android come dipendenza. I token restano di questo repo.
- Backdrop non è un dim arbitrario: quando arriverà, sarà un token, non `Color.Black.copy(0.4)` nel renderer.

## Fase

`S-D4`

Tracciato in `docs/roadmap.md` come Fase 4.
