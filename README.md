# a3ui-graphics

Corpo visivo di A3UI. Non è A3.

A3 (`valeriobitzone-png/a3`, `c17a136`) è il runtime chiuso: epistemica, catalogo, renderer. Questo repo produce i token e gli asset (palette, tipo, spacing, elevation, glyph, texture) che il Theme di `android-compose` può consumare.

## Invarianti

- A3 resta freeze. Nessun nuovo `*Spec`, nessun thaw di `a3ui/`.
- Integrazione = file di Theme / drawable, non architettura.
- Niente glyph o texture inventati dall'AI. Asset disegnati, o niente.
- Repo **private** finché Valerio non apre.

## Consuma

`schemas/a3uisurface.schema.json` v0.2 (in A3). 7 ruoli: stack row list item action field text.

## Non fa

Secondo renderer, KMP, LICENSE, disclosure.
