"""
Unit teste pentru biblioteca_masini.

Se ruleaza cu:
    pytest

`pytest.ini` adauga `app` in `pythonpath` astfel incat
`import lib.biblioteca_masini` functioneaza fara configurare suplimentara.
"""

import logging

import lib.biblioteca_masini as biblioteca_masini

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# descriere_c5
# ---------------------------------------------------------------------------

def test_descriere_c5_returneaza_string_nevida():
    rez = biblioteca_masini.descriere_c5()

    assert isinstance(rez, str), "descriere_c5 trebuie sa returneze un string"
    assert len(rez) > 0, "descriere_c5 nu trebuie sa fie vida"
    logger.info("descriere_c5 a returnat %d caractere", len(rez))


def test_descriere_c5_contine_modelul_si_specificatii():
    rez = biblioteca_masini.descriere_c5()

    # cuvinte cheie care trebuie sa apara in descrierea tehnica
    for cuv in ("Citroen", "C5 X", "Lungime", "Ampatament", "EAT8"):
        assert cuv in rez, f"In descriere_c5 lipseste textul: {cuv}"


# ---------------------------------------------------------------------------
# culoare_c5
# ---------------------------------------------------------------------------

def test_culoare_c5_contine_minim_5_culori():
    rez = biblioteca_masini.culoare_c5()

    assert isinstance(rez, str)
    # numaram aparitiile de cod hex (#RRGGBB)
    nr_hex = sum(1 for ln in rez.splitlines() if ln.count("#") >= 1
                 and "#" in ln and any(ch.isdigit() for ch in ln))
    assert nr_hex >= 5, (
        f"Asteptam minim 5 culori cu cod hex, am gasit {nr_hex}.\n{rez}"
    )


def test_culoare_c5_contine_culori_emblematice():
    rez = biblioteca_masini.culoare_c5()

    for nume in ("Pearl White", "Eclipse Blue", "Volcano Red"):
        assert nume in rez, (
            f"Culoarea '{nume}' lipseste din lista returnata de culoare_c5"
        )


# ---------------------------------------------------------------------------
# motor_c5
# ---------------------------------------------------------------------------

def test_motor_c5_listeaza_variantele_principale():
    rez = biblioteca_masini.motor_c5()

    assert isinstance(rez, str)
    for varianta in ("PureTech", "BlueHDi", "Hybrid"):
        assert varianta in rez, (
            f"Varianta de motorizare '{varianta}' lipseste din motor_c5"
        )


def test_motor_c5_contine_unitati_de_masura():
    rez = biblioteca_masini.motor_c5()

    # un raspuns tehnic decent trebuie sa contina aceste unitati
    for unit in ("CP", "Nm", "km/h", "L"):
        assert unit in rez, (
            f"Unitatea de masura '{unit}' lipseste din motor_c5"
        )


# ---------------------------------------------------------------------------
# pachete_c5
# ---------------------------------------------------------------------------

def test_pachete_c5_contine_pachetele_principale():
    rez = biblioteca_masini.pachete_c5()

    assert isinstance(rez, str)
    for pachet in ("You", "Plus", "Max"):
        assert pachet in rez, (
            f"Pachetul '{pachet}' lipseste din pachete_c5"
        )


def test_pachete_c5_listeaza_dotari():
    rez = biblioteca_masini.pachete_c5()

    # cel putin cateva dotari recunoscute trebuie mentionate
    cuvinte_cheie = ("LED", "jante", "navigatie", "airbag", "piele")
    gasite = [c for c in cuvinte_cheie if c.lower() in rez.lower()]
    assert len(gasite) >= 3, (
        f"Asteptam minim 3 dotari recunoscute, gasite: {gasite}"
    )
