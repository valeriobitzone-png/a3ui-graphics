# Livello 7a — Audio (suoni armoniosi, transizioni uditive)

**Level:** 7 (audio)
**Phase:** `S-D5`
**Tokens:** `tokens/audio.json`

Foley di sistema: un suono, una causa visibile. Silenzio è materiale. Sintesi real-time, mai file. Volume sotto la voce.

## Rationale

Il manifesto A3: non un UI sound pack. `Theme.voiceCeiling` (0.08) e `morphSemitones` (−1) e `airBedMs` (160) sono già veri nel renderer. Questo file li versiona e aggiunge frequenza / envelope per quando la sintesi uscirà dai letterali.

Armonioso = intervalli e envelope dichiarati, non “suono premium”. Transizione uditiva = attacco/rilascio dell'envelope, non un jingle.

## Differito — contenuto di S-D5 (audio)

- Frequenze (`frequencyHz`) e spostamento in semitoni già usato da A3.
- Durata (`durationMs`) allineata ad `airBedMs`.
- Envelope ADSR (`attackMs`, `decayMs`, `sustain`, `releaseMs`).
- `voiceCeiling`, divieto file (`files: false`), sintesi `realtime`.

## Limiti

- Vietato `.wav` / `.ogg` / `res/raw` come fonte di verità.
- Volume ≤ `voiceCeiling` rispetto alla voce.
- Un suono senza causa visibile (stage, crack, morph, haptic gap) è un bug, non un easter egg.
- Questo tag non implementa sintesi. A3 non thaw-a per audio in v0.1 graphics.

## Fase

`S-D5`

Tracciato in `docs/roadmap.md` come Fase 5.
