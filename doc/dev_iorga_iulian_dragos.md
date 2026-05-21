# dev_iorga_iulian_dragos — documentatie branch personal

Acesta este README-ul branch-ului de dezvoltare. Va fi integrat in
`README.md` din `main` prin Pull Request, cu minim un review de la
un coleg de grupa.

---

## 1. Functionalitatea adaugata

Element ales: **Citroen C5** (generatia C5 X, 2022+).

Functiile adaugate in `app/lib/biblioteca_masini.py`:

- `descriere_c5()` — descrierea tehnica scurta a modelului
- `culoare_c5()` — optiunile de culoare (7 culori cu cod si tip)
- `motor_c5()` — optiunile de motorizare (PureTech 130/180, Hybrid 225 PHEV, BlueHDi 130)
- `pachete_c5()` — pachetele de echipare (You, Plus, Max, C-Series)

Rute Flask adaugate in `masini.py`:

| Ruta | Functie Flask |
|---|---|
| `/`             | `index` (descriere + 3 poze + meniu) |
| `/masini`       | `tema_masini` |
| `/c5`           | `element_c5` |
| `/c5/culori`    | `c5_culori` (apeleaza `culoare_c5()`) |
| `/c5/motoare`   | `c5_motoare` (apeleaza `motor_c5()`) |
| `/c5/pachete`   | `c5_pachete` (apeleaza `pachete_c5()`) |

Imaginile (placeholder SVG) folosite pe pagina principala:

- `static/imagini/c5_fata.svg`
- `static/imagini/c5_lateral.svg`
- `static/imagini/c5_spate.svg`

## 2. Stadiul implementarii

- [x] Cod functionalitate adaugat
- [x] Cod test adaugat
- [x] Dockerfile + dockerstart.sh
- [x] Jenkinsfile
- [ ] Capturi de ecran din Docker (de adaugat dupa build local)
- [ ] PR catre `main_iorga_iulian_dragos` (de creat dupa push)
- [ ] PR pentru integrarea README.md in `main` (de creat dupa review)

## 3. Teste

### Manuale

```
flask run -h 0.0.0.0 -p 5011
curl -s http://127.0.0.1:5011/         | head
curl -s http://127.0.0.1:5011/c5/culori
curl -s http://127.0.0.1:5011/c5/motoare
curl -s http://127.0.0.1:5011/c5/pachete
```

### Automate (pytest)

```
pytest
```

Asteptat: toate testele PASS (8 teste in `app/tests/test_lib_biblioteca_masini.py`).

### Jenkins

Pipeline declarativ in `Jenkinsfile`, cu stage-urile:

1. `Build` — venv + dependinte
2. `pylint - calitate cod` — pylint pe lib/tests/masini.py (exit-zero)
3. `Unit Testing cu pytest` — `pytest`
4. `Deploy` — placeholder

Rezultatele rularii Jenkins se ataseaza la PR.

## 4. Integrarea

- PR `dev_iorga_iulian_dragos` -> `main_iorga_iulian_dragos`: **TBD**
- PR README.md catre `main`: **TBD** (cere minim 1 review)

## 5. Containerizarea

```bash
docker build -t curs_scc_441d_masini:dev .
docker run --rm -p 5011:5011 --name masini_c5 curs_scc_441d_masini:dev
```

Capturi de ecran necesare in branch:

- iesirea `docker images` cu imaginea creata
- iesirea `docker ps` cu containerul rulat
- browser-ul afisand `http://localhost:5011/` (pagina principala cu cele 3 poze)
- consola Docker cu request-urile primite (200 OK)

## 6. PR-uri la care s-a facut review

| PR ID | Repo | Autor | Concluzie |
|---|---|---|---|
| (TBD) | curs_scc_441D_masini | (coleg) | (approve / changes) |

## 7. De facut

- inlocuit imaginile placeholder cu fotografii reale (cu drepturi de utilizare)
- adaugat un test e2e cu `flask test_client` pentru rute
- optional: publicare imaginea Docker pe DockerHub
