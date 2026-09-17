# Livello 6 — Shaders & VFX

**Level:** 6
**Phase:** `S-D5`
**Tokens:** `tokens/surfaces.json` → `deferred.refraction`, `deferred.noiseTexture`

Refraction, noise, particle, masking, distorsione liquida. Qui atterrano anche i differiti del livello 1 che richiedono GPU custom.

## Rationale

Il Gaussian blur di Fase 1 è un filtro di compositing, non uno shader di vetro. La rifrazione piega ciò che sta dietro il bordo; il noise evita il blur “plastica”; le particelle e il masking sono effetti di sistema. Senza un livello dedicato, questi effetti invadono i token di Fase 1 e diventano hardcoded.

## Differito — contenuto di S-D5 (grafica)

- Shader di refraction (custom), parametri versionati in un bump di `surfaces.json`.
- Noise texture (micro-grana), asset disegnato o procedurale dichiarato — non inventato senza provenienza.
- Particle effects e masking.
- Distorsione liquida del contenitore (oltre lo squircle statico).

## Limiti

- **Vietato in questo tag** (`a3ui-graphics-v0.1`): refraction, noise, shaders custom, particle, distorsione.
- Vietato “fake refraction” con CSS `filter` extra non tokenizzato.
- I token `deferred.*` non si consumano. Assenza di chiave consumabile = assenza di effetto.
- Nessun secondo renderer in questo repo per prototipare shader.

## Fase

`S-D5`

Tracciato in `docs/roadmap.md` come Fase 5 (insieme ad audio e haptic). Non prima di S-D4.
