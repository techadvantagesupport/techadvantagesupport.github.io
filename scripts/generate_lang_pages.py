#!/usr/bin/env python3
"""
Generates real, self-canonical static homepage files (es/, de/, fr/) from the
English index.html so Google can index each language independently instead of
collapsing everything to the canonical-tagged root.

The body/CSS/JS are byte-identical to root (same DICTS-driven client-side
i18n) -- only the <head> block (title, description, canonical, og/twitter,
html lang attribute) is swapped per language, plus the boot IIFE (already
patched in index.html itself) picks the right default language from the URL
path. Re-run this any time index.html's copy changes, to keep the three
mirrors in sync.
"""
import re
import pathlib

REPO = pathlib.Path("/storage/emulated/0/Download/Tech Advantage Pages")
SRC = REPO / "index.html"

HEAD = {
    "es": {
        "title": "BudgeTrak — App de Presupuesto para Parejas y Familias | Gasto Seguro Diario",
        "description": "Una app de presupuesto diario para parejas y familias: convierte tus ingresos y facturas reales en un número seguro para gastar, compartido entre teléfonos con cifrado de extremo a extremo — sin credenciales bancarias, sin hojas de cálculo. Gratis en Google Play.",
        "og_title": "BudgeTrak — App de Presupuesto para Parejas y Familias",
        "og_description": "Un número seguro para gastar, calculado a partir de tus ingresos y facturas reales — compartido entre los teléfonos de tu hogar con cifrado de extremo a extremo. Sin credenciales bancarias.",
        "twitter_title": "BudgeTrak — App de Presupuesto para Parejas y Familias",
        "twitter_description": "Sabe cuánto puede gastar tu hogar hoy con seguridad — un número calculado a partir de tus ingresos y facturas reales, compartido entre teléfonos con cifrado de extremo a extremo. Gratis en Google Play.",
    },
    "de": {
        "title": "BudgeTrak — Budget-App für Paare & Familien | Täglich sicher ausgeben",
        "description": "Eine tägliche Budget-App für Paare und Familien: verwandle deine echten Einnahmen und Rechnungen in eine sichere Ausgaben-Zahl, geräteübergreifend geteilt mit Ende-zu-Ende-Verschlüsselung — kein Bank-Login, keine Tabellen. Kostenlos bei Google Play.",
        "og_title": "BudgeTrak — Budget-App für Paare & Familien",
        "og_description": "Eine sichere Ausgaben-Zahl, berechnet aus deinen echten Einnahmen und Rechnungen — geteilt zwischen den Telefonen deines Haushalts mit Ende-zu-Ende-Verschlüsselung. Kein Bank-Login nötig.",
        "twitter_title": "BudgeTrak — Budget-App für Paare & Familien",
        "twitter_description": "Wisse, was dein Haushalt heute sicher ausgeben kann — eine Zahl aus deinen echten Einnahmen und Rechnungen, geteilt zwischen Telefonen mit Ende-zu-Ende-Verschlüsselung. Kostenlos bei Google Play.",
    },
    "fr": {
        "title": "BudgeTrak — App de Budget pour Couples et Familles | Dépense Sûre au Quotidien",
        "description": "Une appli de budget quotidien pour couples et familles : transforme tes revenus et factures réels en un montant sûr à dépenser, partagé entre téléphones avec un chiffrement de bout en bout — pas d'identifiants bancaires, pas de tableurs. Gratuite sur Google Play.",
        "og_title": "BudgeTrak — App de Budget pour Couples et Familles",
        "og_description": "Un montant sûr à dépenser, calculé à partir de tes revenus et factures réels — partagé entre les téléphones de ton foyer avec un chiffrement de bout en bout. Aucun identifiant bancaire requis.",
        "twitter_title": "BudgeTrak — App de Budget pour Couples et Familles",
        "twitter_description": "Sache ce que ton foyer peut dépenser sans risque aujourd'hui — un montant calculé à partir de tes revenus et factures réels, partagé entre téléphones avec un chiffrement de bout en bout. Gratuite sur Google Play.",
    },
}


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace('"', "&quot;")


def generate(lang: str, src_text: str) -> str:
    h = HEAD[lang]
    out = src_text

    def replace_one(pattern, replacement, text):
        new_text, n = re.subn(pattern, replacement, text, count=1)
        if n != 1:
            raise RuntimeError(f"expected exactly 1 match for pattern: {pattern!r} (got {n})")
        return new_text

    out = replace_one(r'<html lang="en">', f'<html lang="{lang}">', out)
    out = replace_one(
        r"<title>.*?</title>",
        f"<title>{esc(h['title'])}</title>",
        out,
    )
    out = replace_one(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{esc(h["description"])}">',
        out,
    )
    out = replace_one(
        r'<link rel="canonical" href="https://techadvantageapps\.com/">',
        f'<link rel="canonical" href="https://techadvantageapps.com/{lang}/">',
        out,
    )
    out = replace_one(
        r'<meta property="og:title" content="[^"]*">',
        f'<meta property="og:title" content="{esc(h["og_title"])}">',
        out,
    )
    out = replace_one(
        r'<meta property="og:description" content="[^"]*">',
        f'<meta property="og:description" content="{esc(h["og_description"])}">',
        out,
    )
    out = replace_one(
        r'<meta property="og:url" content="https://techadvantageapps\.com/">',
        f'<meta property="og:url" content="https://techadvantageapps.com/{lang}/">',
        out,
    )
    out = replace_one(
        r'<meta name="twitter:title" content="[^"]*">',
        f'<meta name="twitter:title" content="{esc(h["twitter_title"])}">',
        out,
    )
    out = replace_one(
        r'<meta name="twitter:description" content="[^"]*">',
        f'<meta name="twitter:description" content="{esc(h["twitter_description"])}">',
        out,
    )
    # MobileApplication JSON-LD "url" field -- self-reference like the canonical.
    out = replace_one(
        r'"url": "https://techadvantageapps\.com/",\n  "description"',
        f'"url": "https://techadvantageapps.com/{lang}/",\n  "description"',
        out,
    )
    return out


def main():
    src_text = SRC.read_text(encoding="utf-8")
    for lang in ("es", "de", "fr"):
        out = generate(lang, src_text)
        dest = REPO / lang / "index.html"
        dest.write_text(out, encoding="utf-8")
        print(f"wrote {dest} ({len(out)} bytes)")


if __name__ == "__main__":
    main()
