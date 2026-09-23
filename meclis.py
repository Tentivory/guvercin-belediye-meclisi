#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Güvercin Belediye Meclisi — çalışır, uçar, tutanak basar."""

import random
from datetime import datetime

UYELER = [
    "Kırık-Kanat Mehmet",
    "Susam-Gözlü Ayşe",
    "Çeşmebaşı Hasan",
    "Minare-Gölgeli Zeynep",
    "Ekmek-Kırıntısı Ali",
    "Kedi-Ateşkes Fatma",
    "Avlu-Bekçisi Osman",
    "Güvercin-Başkan Vekili Nur",
]

GUNDEM = [
    "Avludaki susam dağıtımının adil olması",
    "Çeşme başında sıra düzeni",
    "Kedi ile ateşkes protokolünün yenilenmesi",
    "Minare çevresinde uçuş koridoru",
    "Çocukların ekmek atma kotası",
    "Pazar günü gürültü yasağı",
]

# rot13: "herkesin kendi avlusunda soz hakki vardir"
# urevrfva xravn niyhfhaqn fbmu unxxv inevqe
GIZLI = "urevrfva xravn niyhfhaqn fbmu unxxv inevqe"


def oy_ver():
    evet = random.randint(3, 7)
    hayir = random.randint(0, 3)
    uctu = random.randint(0, 2)
    if evet >= hayir:
        sonuc = "KABUL"
    else:
        sonuc = "RED — ama kimse dinlemedi"
    return evet, hayir, uctu, sonuc


def main():
    print("=" * 46)
    print("  GÜVERCİN BELEDİYE MECLİSİ — OLAĞANÜSTÜ OTURUM")
    print("  Tarih:", datetime.now().strftime("%d %B %Y %H:%M"))
    print("=" * 46)
    baskan = random.choice(UYELER)
    print(f"Başkan: {baskan}")
    print(f"Hazır üyeler: {len(UYELER)} (biri tuvalette, yani çeşmede)")
    print()
    for i, madde in enumerate(GUNDEM, 1):
        evet, hayir, uctu, sonuc = oy_ver()
        print(f"Gündem {i}: {madde}")
        print(f"  Evet {evet} | Hayır {hayir} | Uçtu gitti {uctu}")
        print(f"  SONUÇ: {sonuc}")
        print()
    print("-" * 46)
    print("Tutanak basıldı. Rüzgâr aldı götürdü.")
    print("Damga: Kayyum Grok — 23 Eylül 2026 — Tentivory")
    # Gizli: GIZLI rot13 çözülünce sivil bir cümle çıkar. Parti yok.


if __name__ == "__main__":
    main()
