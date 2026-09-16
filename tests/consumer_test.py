#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Part of the A3 universe. See LICENSE.
"""CS-001..006 — la spec vista da chi la consuma. Stdlib only.

    python3 tests/consumer_test.py

Nota di attribuzione: file proposto da Claude il 15 set 2026, dopo aver
costruito il primo consumatore reale. Non e' il gate della spec — quello resta
`gs_test.py`, che non e' stato toccato. Questo copre
l'altro lato: che la spec resti consumabile senza doverla indovinare.

GS-002 valida i token contro gli schemi. Nessuno verificava che un consumatore
che legge solo `fase-1` ottenga un insieme coerente, ne' che il manifest dica
la verita' sul disco. Il rischio non e' teorico: `gs_test.py` ha l'elenco dei
sette file scritto a mano, quindi un ottavo token aggiunto domani sarebbe
invisibile alla suite; un consumer precedente invece faceva `glob`, quindi lo avrebbe consumato in
silenzio. Due errori opposti, stessa causa: nessun indice.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FASI_NOTE = {"fase-1", "remainder-l2", "S-D2", "S-D3", "S-D4", "S-D5"}


class Fail(Exception):
    pass


def _carica(rel: str):
    p = ROOT / rel
    if not p.is_file():
        raise Fail(f"{rel} manca")
    return json.loads(p.read_text(encoding="utf-8"))


def cs001() -> None:
    """Il manifest esiste e dichiara le fasi consumabili."""
    m = _carica("manifest.json")
    for campo in ("tag", "fasi_consumabili", "file"):
        if not m.get(campo):
            raise Fail(f"manifest senza {campo}")
    if m["fasi_consumabili"] != ["fase-1"]:
        raise Fail(f"fasi consumabili inattese: {m['fasi_consumabili']}")


def cs002() -> None:
    """Il manifest combacia col disco: stessi file, ne' piu' ne' meno."""
    m = _carica("manifest.json")
    dichiarati = {v["token"] for v in m["file"]}
    sul_disco = {f"tokens/{p.name}" for p in (ROOT / "tokens").glob("*.json")}
    if dichiarati != sul_disco:
        mancanti = sorted(sul_disco - dichiarati)
        fantasmi = sorted(dichiarati - sul_disco)
        raise Fail(f"manifest disallineato — non dichiarati: {mancanti}; "
                   f"dichiarati ma assenti: {fantasmi}")


def cs003() -> None:
    """Ogni voce dice il vero su status, fase e schema."""
    m = _carica("manifest.json")
    for v in m["file"]:
        d = _carica(v["token"])
        if v["status"] != d.get("status"):
            raise Fail(f"{v['token']}: manifest dice {v['status']}, il file {d.get('status')}")
        if v["phase"] != d.get("phase"):
            raise Fail(f"{v['token']}: fase incoerente")
        if d.get("phase") not in FASI_NOTE:
            raise Fail(f"{v['token']}: fase sconosciuta {d.get('phase')}")
        if v["consumabile"] != (d.get("status") == "fase-1"):
            raise Fail(f"{v['token']}: 'consumabile' non segue lo status")
        if v["schema"] and not (ROOT / v["schema"]).is_file():
            raise Fail(f"{v['token']}: schema dichiarato ma assente")


def cs004() -> None:
    """Un consumatore che prende solo fase-1 ottiene qualcosa di usabile."""
    m = _carica("manifest.json")
    consumabili = {Path(v["token"]).stem for v in m["file"] if v["consumabile"]}
    if not consumabili:
        raise Fail("nessun token consumabile: la Fase 1 sarebbe vuota")
    # Il minimo per disegnare una superficie: un colore, una profondita', un vetro.
    for atteso in ("colors", "elevation", "surfaces"):
        if atteso not in consumabili:
            raise Fail(f"Fase 1 senza {atteso}: non si puo' disegnare una superficie")


def cs005() -> None:
    """I differiti restano differiti: nessuno e' scivolato dentro."""
    m = _carica("manifest.json")
    for v in m["file"]:
        if Path(v["token"]).stem in ("motion", "typography", "audio", "haptic"):
            if v["consumabile"]:
                raise Fail(f"{v['token']} e' diventato consumabile: "
                           "se e' voluto, va aggiornato CHANGELOG.md e la roadmap")


def cs006() -> None:
    """Il contratto di consumo esiste e nomina la regola."""
    for rel in ("CONSUMING.md", "CHANGELOG.md"):
        p = ROOT / rel
        if not p.is_file():
            raise Fail(f"{rel} manca")
    testo = (ROOT / "CONSUMING.md").read_text(encoding="utf-8")
    if "fase-1" not in testo or "manifest.json" not in testo:
        raise Fail("CONSUMING.md non nomina la regola o il manifest")


CHECKS = [("CS-001", cs001), ("CS-002", cs002), ("CS-003", cs003),
          ("CS-004", cs004), ("CS-005", cs005), ("CS-006", cs006)]


def main() -> int:
    errori = 0
    for nome, fn in CHECKS:
        try:
            fn()
            print(f"{nome} PASS")
        except Fail as e:
            errori += 1
            print(f"{nome} FAIL: {e}")
    print("\nCS-001..006 " + ("PASS" if not errori else f"{errori} FAIL"))
    return 1 if errori else 0


if __name__ == "__main__":
    raise SystemExit(main())
