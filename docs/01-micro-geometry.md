# Livello 2 — Micro-geometry (layout & forms)

**Level:** 2
**Phase:** `fase-1` (solo curvature)
**Tokens:** `tokens/surfaces.json` (`container`), `tokens/typography.json` (differito)

Gli angoli e i raggi annidati. Non il catalogo: A3 continua a decidere *cosa* è `list` o `action`. Questo livello decide *come* il contenitore chiude lo spazio.

## Rationale

Un rettangolo a raggio circolare (CSS `border-radius`) gonfia gli angoli e stringe i lati. La superellisse (squircle) tiene la curvatura sugli angoli e i lati più lunghi. È la geometria di un OS, non di una card Material.

Il nested radius evita squircle-in-squircle che “mangia” il padding: il raggio interno è funzione dell'esterno e del padding, con un minimo.

## In Fase 1

- Squircles (superellisse) per gli angoli dei container: `container.corner.kind = squircle`, `superellipseN`, `radiusPx`.
- Nested radius: `inner = max(minPx, outerRadiusPx - paddingPx)`.

## Differito (non Fase 1)

| Capacità | Phase | Perché |
|---|---|---|
| Tipografia variable + optical sizing | `remainder-l2` | L2 remainder. `typography.json` è versionato ma `status: deferred`. A3 oggi usa 18sp / weight 400 / ink. |
| Icone animate / glifi stratificati | `remainder-l2` | Niente glyph inventati dall'AI. Asset disegnati, o niente. |

Non saltare `remainder-l2` per andare a `S-D2` (GR-004).

## Limiti

- Nessun nuovo ruolo. Lo squircle è corner treatment di superfici esistenti.
- `superellipseN` e `radiusPx` solo da token. Niente `14.dp` nel renderer A3 quando consumerà questo file.
- Nested radius non è un inset visivo extra: è geometria. Il padding resta lo spacing A3 (`16`) finché A3 non consumerà un token di space da questo repo (non in Fase 1: space resta in Theme A3).
- Variable fonts e icone: file presenti, consumo vietato in Fase 1.

## Fase

`fase-1`

Remainder L2 (type + icone): `remainder-l2`, dopo Fase 1, prima di `S-D2`. Vedi `docs/roadmap.md`.
