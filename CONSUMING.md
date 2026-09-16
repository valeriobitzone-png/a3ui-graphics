# Consumare a3ui-graphics

> **Nota di provenienza.** Questo file documenta una regola dedotta dal primo
> consumer test. Non è una decisione di prodotto: descrive il contratto necessario
> perché il ponte resti nella spec, non nel consumatore.

`a3ui-graphics` è una spec, non una libreria. GR-001: *la spec è la fonte di
verità, l'implementazione consuma i token.* Questo file dice come.

## 1. La regola unica

**Si consuma solo ciò che dichiara `"status": "fase-1"`.**

Ogni file in `tokens/` porta il proprio `status` e la propria `phase`. Oggi:

| File | status | consumabile |
|---|---|---|
| `colors.json` | `fase-1` | sì |
| `elevation.json` | `fase-1` | sì |
| `surfaces.json` | `fase-1` | sì |
| `motion.json` | `deferred` (S-D2) | no |
| `typography.json` | `deferred` (remainder-l2) | no |
| `audio.json` | `deferred` (S-D5) | no |
| `haptic.json` | `deferred` (S-D5) | no |

`manifest.json` è la stessa tabella in forma macchina-leggibile: **leggere quello**,
non fare `glob` sulla cartella. Un `glob` consuma in silenzio qualunque file
compaia domani, ed è esattamente il modo in cui una fase si salta senza che
nessuno se ne accorga (GR-004).

## 2. Cosa deve fare un consumatore

1. leggere `manifest.json`;
2. prendere i file con `consumabile: true`;
3. **rifiutare** gli altri, e dire quali ha rifiutato — un rifiuto silenzioso e
   un'assenza sono indistinguibili;
4. registrare la provenienza: tag, versione, data, percorso del repo;
5. non rimandare mai niente verso la spec. Il ponte va in una direzione sola.

## 3. Cosa NON deve fare

- Non copiare un valore di vetro, ombra o molla nel proprio codice (GR-003).
  Se il valore serve, viene dal token; se il token non c'è ancora, la funzione
  aspetta la fase.
- Non "adattare" un token differito perché servirebbe adesso. Una fase saltata
  non si vede in un test: si vede sei mesi dopo, quando due superfici si muovono
  in due modi diversi e nessuno sa perché.
- Non trattare l'assenza di un token come zero. Assente ≠ zero.

## 4. Quando una fase avanza

Quando un file passa da `deferred` a `fase-1`:

1. cambia il suo `status` **nel file**, non nel consumatore;
2. `manifest.json` va rigenerato;
3. i consumatori lo vedono al giro successivo senza modifiche;
4. il consumatore deve dire cosa ha cominciato a consumare, non assorbirlo in
   silenzio.

## 5. Consumatori noti

| Consumatore | Come | Cosa prende |
|---|---|---|
| Consumer privato | ponte di token dichiarato dal consumer | colors, elevation, surfaces |

Un secondo consumatore indipendente è ciò che tiene onesta la spec:
finché ce n'è uno solo, ogni decisione rischia di essere presa per far contento
quello.

## 6. Cosa questo file NON risolve

- **Licenza**: il README dice «Non fa: LICENSE pubblica». Finché resta così, chi
  consuma lo fa senza termini scritti. È una decisione di governance, non una
  dimenticanza da riempire.
- **Versioning**: tutti i token sono `0.1`. `CHANGELOG.md` è il posto dove
  scrivere cosa cambia; oggi è vuoto perché niente è ancora cambiato.
