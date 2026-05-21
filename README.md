# curs_scc_441D_masini

Proiect pentru cursul **Servicii Cloud si Containerizare** (SCC), grupa
**441D**, tema **Masini**.

Aplicatia este o aplicatie WEB simpla scrisa in Python + Flask, dupa
modelul aplicatiei exemplu
[`crchende/sysinfo`](https://github.com/crchende/sysinfo/tree/devel).

---

## Cuprins

- [Tema si elementul ales](#tema-si-elementul-ales)
- [Structura aplicatiei](#structura-aplicatiei)
- [Rute (pagini) disponibile](#rute-pagini-disponibile)
- [Rulare locala](#rulare-locala)
- [Testare](#testare)
- [Containerizare (Docker)](#containerizare-docker)
- [Stadiu dezvoltatori](#stadiu-dezvoltatori)
- [Documentatie pe branch-uri de dezvoltare](#documentatie-pe-branch-uri-de-dezvoltare)

---

## Tema si elementul ales

| Aspect | Valoare |
|---|---|
| Grupa | 441D |
| Tema | Masini |
| Element ales | Citroen C5 (generatia C5 X, 2022+) |
| Dezvoltator | Iorga Iulian Dragos |
| Fisier biblioteca | `app/lib/biblioteca_masini.py` |
| Fisier principal Flask | `masini.py` |

Functii implementate in `app/lib/biblioteca_masini.py`:

- `descriere_c5()` — descriere tehnica scurta
- `culoare_c5()` — optiunile de culoare
- `motor_c5()` — optiunile de motorizare
- `pachete_c5()` — pachetele (nivelele de echipare)

---

## Structura aplicatiei

```
curs_scc_441D_masini/
├── masini.py                       # aplicatia Flask (rute)
├── app/
│   ├── __init__.py
│   ├── lib/
│   │   ├── __init__.py
│   │   └── biblioteca_masini.py    # functiile specifice elementului C5
│   └── tests/
│       └── test_lib_biblioteca_masini.py
├── static/
│   └── imagini/
│       ├── c5_fata.svg
│       ├── c5_lateral.svg
│       └── c5_spate.svg
├── Dockerfile
├── dockerstart.sh
├── Jenkinsfile
├── activeaza_venv
├── activeaza_venv_jenkins
├── ruleaza_aplicatia
├── pytest.ini
├── quickrequirements.txt
├── .gitignore
└── README.md
```

---

## Rute (pagini) disponibile

| Ruta | Functie | Descriere |
|---|---|---|
| `/`             | `index`         | Pagina principala: descriere tehnica scurta + 3 imagini + linkuri catre subpagini |
| `/masini`       | `tema_masini`   | Pagina pentru tema (Masini) |
| `/c5`           | `element_c5`    | Pagina pentru elementul Citroen C5 |
| `/c5/culori`    | `c5_culori`     | Optiuni de culoare (apel `culoare_c5()`) |
| `/c5/motoare`   | `c5_motoare`    | Optiuni de motorizare (apel `motor_c5()`) |
| `/c5/pachete`   | `c5_pachete`    | Pachete / nivele de echipare (apel `pachete_c5()`) |

---

## Rulare locala

### Prima rulare (creeaza venv-ul si instaleaza dependintele)

```bash
. ./activeaza_venv_jenkins
```

### Rularile urmatoare

```bash
. ./activeaza_venv
./ruleaza_aplicatia
```

Aplicatia va asculta pe `http://127.0.0.1:5011/`.

Alternativ:

```bash
python masini.py
```

---

## Testare

Testele sunt scrise cu `pytest` si se afla in `app/tests/`.

```bash
. ./activeaza_venv
pytest
```

`pytest.ini` adauga directorul `app/` in `pythonpath`, astfel incat
testele importa `lib.biblioteca_masini`.

Testele acopera fiecare dintre cele 4 functii din biblioteca:

- `test_descriere_c5_*` — descrierea tehnica
- `test_culoare_c5_*` — culorile disponibile (numar minim, denumiri-cheie)
- `test_motor_c5_*` — variantele de motorizare si unitatile de masura
- `test_pachete_c5_*` — pachetele (You / Plus / Max) si dotarile

In Jenkins, testarea ruleaza automat in pipeline-ul declarativ
(`Jenkinsfile`), in stage-ul **Unit Testing cu pytest**.

---

## Containerizare (Docker)

### Build imagine

```bash
docker build -t curs_scc_441d_masini:dev .
```

### Rulare container

```bash
docker run --rm -p 5011:5011 --name masini_c5 curs_scc_441d_masini:dev
```

Apoi se acceseaza in browser:
[http://localhost:5011/](http://localhost:5011/).

In documentatia branch-ului de dezvoltare se vor adauga capturi de
ecran pentru:

- imaginea de container creata (`docker images`)
- containerul rulat (`docker ps`)
- browser-ul accesand `http://localhost:5011/`
- mesajele afisate in consola containerului

---

## Stadiu dezvoltatori

| Element | Dezvoltator | Implementare | Testare | Integrare |
|---|---|---|---|---|
| Citroen C5 X | Iorga Iulian Dragos | DONE — `app/lib/biblioteca_masini.py` | DONE — `app/tests/test_lib_biblioteca_masini.py` | In curs (PR pe `main_iorga_iulian_dragos`) |

Pe masura ce alti colegi de grupa adauga elemente noi (alte modele de
masini), se completeaza tabelul de mai sus din branch-ul personal de
dezvoltare prin Pull Request.

---

## Documentatie pe branch-uri de dezvoltare

Pentru fiecare branch de dezvoltare (`dev_<nume_prenume>`), README-ul
contine sectiuni dedicate (vezi cerinte proiect):

1. **Functionalitatea adaugata** — ce element + ce functii
2. **Stadiul implementarii** — DONE / IN PROGRESS / TODO
3. **Testele** — ce teste, manual + Jenkins, status PASS/FAIL
4. **Integrarea** — PR-ul deschis, status review
5. **Containerizarea** — capturi de ecran (imagine, container, browser, log)
6. **PR-uri la care s-a facut review** — cu ID-uri
7. **De facut** — ramasite, idei viitoare

---

## Branch-uri (cerinte git)

- `main` — protejat, integrare via PR + minim un review
- `main_<nume_prenume>` — branch personal, integreaza modificari din `dev_<nume_prenume>`
- `dev_<nume_prenume>` — branch personal de dezvoltare zilnica

Pentru aceasta implementare:

- `main_iorga_iulian_dragos`
- `dev_iorga_iulian_dragos`
