# Livello 7b — Haptic (localizzati, pressione)

**Level:** 7 (haptic)
**Phase:** `S-D5`
**Tokens:** `tokens/haptic.json`

Feedback di pressione e texture. A3 ha già haptic *semantico* (`HapticMap`: `tap` / `double-tap`, `light` / `medium`, gap 40ms). Questo livello versiona intensità / texture / duration e differisce localizzazione e pressione analogica.

## Rationale

Il renderer decide COME un evento semantico diventa motore; non inventa l'evento. I token chiudono i letterali (`hapticGapMs`, intensità). Localizzato = il punto di contatto, non il telefono intero. Pressione = ampiezza continua, non due bucket.

S-D5 perché haptic localizzato e pressione chiedono device API oltre `performHapticFeedback` e vanno dopo chrome/motion (l'utente sente *dove* il vetro cede).

## Differito — contenuto di S-D5 (haptic)

- Intensità e duration per `light` e `medium`.
- Texture nominata (`tick`, `tap`).
- `gapMs` (40) tra i due battiti di `double-tap`.
- Localizzato: `deferred.localized`.
- Pressione analogica: `deferred.pressure`.

A3 può continuare a mappare `light`/`medium` come oggi finché non consuma questo file. Consumo = S-D5, non Fase 1.

## Limiti

- Nessuna API device in questo repo. Nessun vibrator sample.
- Vietato haptic senza causa nel `HapticMap`.
- Localized / pressure: chiavi `deferred`, non consumabili.
- Intensità fuori da `light`/`medium` = nuova chiave versionata, non un magico terzo valore nel renderer.

## Fase

`S-D5`

Tracciato in `docs/roadmap.md` come Fase 5.
