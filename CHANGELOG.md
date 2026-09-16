# CHANGELOG — a3ui-graphics

> **Nota di attribuzione.** File proposto da Claude il 15 set 2026. Serve perché
> i token portano `version: "0.1"` ma niente dice cosa cambierà nella 0.2, e un
> consumatore che si aggiorna deve sapere cosa gli si rompe.

Il formato: una voce per tag. Ogni voce dice **cosa è cambiato per chi consuma**,
non cosa è cambiato nel repo.

---

## `a3ui-graphics-v0.1` — 11 set 2026

Primo tag. Spec chiusa per la Fase 1.

**Consumabile:** `colors`, `elevation`, `surfaces` (liquid glass base + curvature).

**Differito:** `motion` (S-D2), `typography` (remainder-l2), `audio` e `haptic` (S-D5).

**Per chi consuma:** niente da migrare, è il primo tag.

---

## Non ancora rilasciato

Nessuna modifica ai token dal tag v0.1.

**Licenza (15 set 2026):** la spec passa sotto **CC BY 4.0** (`LICENSE`).
Per chi consuma: l'uso resta libero, va citato il tag di provenienza —
per esempio `a3ui-graphics-v0.1`.

Aggiunti solo file di infrastruttura, che non toccano la spec né il catalogo
(`stack row list item action field text`, invariato):

- `manifest.json` — indice macchina-leggibile di file, fase e schema
- `CONSUMING.md` — il contratto di consumo
- `CHANGELOG.md` — questo file
- `tests/consumer_test.py` — la verifica dal lato di chi consuma
