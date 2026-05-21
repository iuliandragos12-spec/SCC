"""
Biblioteca masini - elementul ales: Citroen C5 (generatia C5 X, 2022+).

Contine functii care intorc informatii despre:
    - descrierea tehnica scurta (descriere_c5)
    - optiunile de culoare (culoare_c5)
    - optiunile de motorizare (motor_c5)
    - pachetele de echipare (pachete_c5)

Functiile intorc string-uri formatate, pregatite pentru a fi afisate
in pagini HTML <pre> sau prelucrate in template-uri.

Autor: Iorga Iulian Dragos
Tema:  Masini (grupa 441D)
"""


def descriere_c5():
    """
    Descriere tehnica scurta a modelului Citroen C5 X.

    parametrii: -

    return:     descriere multi-linie a masinii
    """

    descriere = (
        "Citroen C5 X (generatia 2022+)\n"
        "------------------------------\n"
        "Citroen C5 X este modelul de top al marcii, un crossover-fastback\n"
        "care combina trei elemente: confortul unei berline, dinamismul\n"
        "unui break si garda la sol crescuta a unui SUV.\n"
        "\n"
        "Caracteristici tehnice principale:\n"
        " - Lungime:           4.805 mm\n"
        " - Latime:            1.865 mm\n"
        " - Inaltime:          1.490 mm\n"
        " - Ampatament:        2.785 mm\n"
        " - Volum portbagaj:   545 - 1.640 L\n"
        " - Masa proprie:      1.524 - 1.755 kg\n"
        " - Suspensie:         Citroen Advanced Comfort cu amortizoare\n"
        "                      hidraulice progresive\n"
        " - Tractiune:         fata\n"
        " - Cutie de viteze:   automata EAT8 (8 trepte)\n"
        " - Platforma:         EMP2 (Stellantis)\n"
    )
    return descriere


def culoare_c5():
    """
    Optiunile de culoare disponibile pentru Citroen C5 X.

    parametrii: -

    return:     lista formatata cu denumirea culorii si codul oficial
    """

    culori = [
        ("Pearl White",      "EWP",  "#F2F2F0", "perlat"),
        ("Polar White",      "EWS",  "#FFFFFF", "solid"),
        ("Cumulus Grey",     "M0YK", "#A6A9AC", "metalizat"),
        ("Platinum Grey",    "EVL",  "#7B8084", "metalizat"),
        ("Perla Nera Black", "EXY",  "#16181C", "perlat"),
        ("Eclipse Blue",     "EPQ",  "#1B2E55", "metalizat"),
        ("Volcano Red",      "EPY",  "#7A1F1F", "metalizat"),
    ]

    rezultat = "Optiuni de culoare disponibile pentru Citroen C5 X:\n"
    rezultat += "-" * 55 + "\n"
    rezultat += f"{'Nume':<20}{'Cod':<8}{'Hex':<10}{'Tip'}\n"
    rezultat += "-" * 55 + "\n"
    for nume, cod, hex_val, tip in culori:
        rezultat += f"{nume:<20}{cod:<8}{hex_val:<10}{tip}\n"
    rezultat += "-" * 55 + "\n"
    rezultat += f"Total: {len(culori)} culori disponibile.\n"

    return rezultat


def motor_c5():
    """
    Optiunile de motorizare disponibile pentru Citroen C5 X.

    parametrii: -

    return:     descrierea variantelor de motorizare
    """

    motoare = [
        {
            "nume":        "PureTech 130 EAT8",
            "tip":         "benzina",
            "cilindree":   "1.199 cmc (3 cilindri)",
            "putere":      "130 CP / 230 Nm",
            "transmisie":  "automata EAT8",
            "consum":      "6.4 - 6.8 L / 100 km (WLTP)",
            "co2":         "144 - 153 g/km",
            "0_100":       "10.4 s",
            "viteza_max":  "210 km/h",
        },
        {
            "nume":        "PureTech 180 EAT8",
            "tip":         "benzina",
            "cilindree":   "1.598 cmc (4 cilindri)",
            "putere":      "180 CP / 250 Nm",
            "transmisie":  "automata EAT8",
            "consum":      "6.6 - 7.0 L / 100 km (WLTP)",
            "co2":         "149 - 158 g/km",
            "0_100":       "8.8 s",
            "viteza_max":  "230 km/h",
        },
        {
            "nume":        "Hybrid 225 e-EAT8 (PHEV)",
            "tip":         "hibrid plug-in",
            "cilindree":   "1.598 cmc benzina + motor electric 81 kW",
            "putere":      "225 CP combinat / 360 Nm",
            "transmisie":  "automata e-EAT8",
            "consum":      "1.3 - 1.6 L / 100 km (WLTP, mod hibrid)",
            "co2":         "30 - 36 g/km",
            "0_100":       "7.8 s",
            "viteza_max":  "233 km/h (140 km/h electric)",
            "autonomie_e": "~ 55 km in mod electric",
            "baterie":     "12.4 kWh",
        },
        {
            "nume":        "BlueHDi 130 EAT8",
            "tip":         "diesel",
            "cilindree":   "1.499 cmc (4 cilindri)",
            "putere":      "130 CP / 300 Nm",
            "transmisie":  "automata EAT8",
            "consum":      "4.7 - 5.2 L / 100 km (WLTP)",
            "co2":         "124 - 137 g/km",
            "0_100":       "10.7 s",
            "viteza_max":  "210 km/h",
        },
    ]

    rezultat = "Motorizari disponibile pentru Citroen C5 X:\n"
    rezultat += "=" * 55 + "\n"
    for i, m in enumerate(motoare, 1):
        rezultat += f"\n[{i}] {m['nume']}\n"
        rezultat += "-" * 55 + "\n"
        rezultat += f"  Tip combustibil: {m['tip']}\n"
        rezultat += f"  Cilindree:       {m['cilindree']}\n"
        rezultat += f"  Putere:          {m['putere']}\n"
        rezultat += f"  Transmisie:      {m['transmisie']}\n"
        rezultat += f"  Consum:          {m['consum']}\n"
        rezultat += f"  Emisii CO2:      {m['co2']}\n"
        rezultat += f"  0-100 km/h:      {m['0_100']}\n"
        rezultat += f"  Viteza maxima:   {m['viteza_max']}\n"
        if "autonomie_e" in m:
            rezultat += f"  Autonomie el.:   {m['autonomie_e']}\n"
            rezultat += f"  Baterie:         {m['baterie']}\n"
    rezultat += "=" * 55 + "\n"
    rezultat += f"Total: {len(motoare)} motorizari disponibile.\n"

    return rezultat


def pachete_c5():
    """
    Pachetele (nivelele de echipare) disponibile pentru Citroen C5 X.

    parametrii: -

    return:     descrierea pachetelor cu echiparile incluse
    """

    pachete = [
        {
            "nume":        "You",
            "descriere":   "Nivelul de baza, dotari esentiale",
            "echipare": [
                "Jante din otel 17\"",
                "Faruri full LED",
                "Climatizare automata bizona",
                "Citroen Connect Radio cu ecran 10\"",
                "6 airbag-uri",
                "Active Safety Brake (frana automata de urgenta)",
                "Lane Keeping Assist",
                "Cruise control cu limitator de viteza",
                "Tapiterie textila",
            ],
        },
        {
            "nume":        "Plus",
            "descriere":   "Nivel intermediar, confort si tehnologie",
            "echipare": [
                "Toate dotarile de la nivelul You, plus:",
                "Jante din aliaj 18\"",
                "Citroen Advanced Comfort - amortizoare hidraulice",
                "Senzori de parcare fata + spate",
                "Camera marsarier",
                "Citroen Connect Nav - navigatie integrata",
                "Apple CarPlay / Android Auto wireless",
                "Incarcare smartphone wireless",
                "Tapiterie mixta textil + Alcantara",
                "Geamuri spate fumurii",
            ],
        },
        {
            "nume":        "Max",
            "descriere":   "Nivel de top, dotari premium si pachet de siguranta",
            "echipare": [
                "Toate dotarile de la nivelul Plus, plus:",
                "Jante din aliaj 19\"",
                "Faruri Matrix LED",
                "Highway Driver Assist (asistenta semi-autonoma)",
                "Adaptive Cruise Control Stop & Go",
                "Blind Spot Monitoring",
                "Head-Up Display color",
                "Sistem audio Hi-Fi",
                "Tapiterie din piele Nappa",
                "Scaune fata cu reglaj electric, incalzire si masaj",
                "Trapa panoramica",
                "Hayon electric cu actionare hands-free",
            ],
        },
        {
            "nume":        "C-Series (editie limitata)",
            "descriere":   "Editie speciala bazata pe nivelul Plus",
            "echipare": [
                "Pachet vopsea bicolora (acoperis negru)",
                "Detalii de exterior in finisaj 'Dark Chrome'",
                "Logo C-Series pe aripi",
                "Tapiterie speciala cu cusaturi rosii",
                "Praguri iluminate C-Series",
                "Covorase personalizate",
            ],
        },
    ]

    rezultat = "Pachete (nivele de echipare) disponibile pentru Citroen C5 X:\n"
    rezultat += "=" * 60 + "\n"
    for i, p in enumerate(pachete, 1):
        rezultat += f"\n[{i}] {p['nume']}\n"
        rezultat += f"    {p['descriere']}\n"
        rezultat += "-" * 60 + "\n"
        for dotare in p["echipare"]:
            rezultat += f"  - {dotare}\n"
    rezultat += "\n" + "=" * 60 + "\n"
    rezultat += f"Total: {len(pachete)} pachete disponibile.\n"

    return rezultat
