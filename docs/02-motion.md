# Livello 3 — Motion (spring physics)

**Level:** 3
**Phase:** `S-D2`
**Tokens:** `tokens/motion.json`

Animazione come fisica dichiarata: massa, stiffness, damping, easing. In A3 il *verbo* resta epistemico (HELD, UNKNOWN, CONTRADICTED, STALE, COMPENSATED). Questo livello versiona *come* un verbo occupa il tempo.

## Rationale

Il manifesto A3: ogni animazione è emessa da uno stato verificato, non da una scelta drammatica. I numeri oggi sono hardcoded in `Theme` (renderer A3). Questo file è la fonte di verità per quando A3 smetterà di hardcodarli (GR-001, GR-003). Finché `status` è `deferred`, A3 non thaw-a per consumarli.

Spring e morphing/inertia appartengono a questo livello. I cinque verbi epistemici sono già veri nel renderer; qui si registrano le durate perché non restino letterali eterne.

## Differito — contenuto di S-D2

- Spring physics: `springs.*` (`mass`, `stiffness`, `damping`) per density compact / comfortable / spacious, allineati a `TemporalBuilder` A3.
- Morphing e inertia: non tokenizzati oltre `springs` + `easings` in v0.1. Arrivano in S-D2 come estensione di questo file, non come livello saltato.
- Easings nominati (`standard`, `emphasized`).

`reducedMotion.zeroAllDurations` è invariante già vero in A3: ON azzera le durate e lascia la cromia. Resta dichiarato qui così non si reintroduce motion in accessibilità.

## Limiti

- Nessuna spring, morph, inertia in questo tag spec come *implementazione*. I JSON esistono per GR-003; il consumo è `S-D2`.
- Nessun verbo nuovo. Pulse / shimmer / crack / fade restano i cinque di A3.
- Niente duration inventata fuori da `epistemicVerbs` e `springs`.
- Reduced motion: vietato aggirare lo zero.

## Fase

`S-D2`

Tracciato in `docs/roadmap.md` come Fase 2. Non prima di Fase 1 e di `remainder-l2`.
