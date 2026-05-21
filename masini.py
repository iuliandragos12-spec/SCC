"""
Aplicatie Flask: tema 'Masini' (grupa 441D).
Element: Citroen C5 (generatia C5 X, 2022+).

Rute:
  /                      -> pagina principala (index): tema + element +
                            descriere tehnica scurta + 3 poze + meniu
  /masini                -> pagina pentru tema 'Masini'
  /c5                    -> pagina pentru elementul Citroen C5
  /c5/culori             -> optiunile de culoare (culoare_c5)
  /c5/motoare            -> optiunile de motorizare (motor_c5)
  /c5/pachete            -> pachetele de echipare (pachete_c5)

Autor: Iorga Iulian Dragos
"""

from flask import Flask, url_for

from app.lib import biblioteca_masini

print('masini - Citroen C5 X')

app = Flask(__name__)


# ---------------------------------------------------------------------------
# Helper: stil comun + structura HTML pentru toate paginile
# ---------------------------------------------------------------------------

PAGE_CSS = """
<style>
  body {
    font-family: 'Segoe UI', Arial, sans-serif;
    margin: 0;
    background: #f4f6fa;
    color: #1a1a1a;
  }
  header {
    background: linear-gradient(90deg, #102050, #2a3f72);
    color: #fff;
    padding: 24px 32px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.15);
  }
  header h1 { margin: 0; font-size: 28px; letter-spacing: 1px; }
  header .sub { opacity: 0.85; font-size: 14px; margin-top: 4px; }

  nav {
    background: #fff;
    padding: 12px 32px;
    border-bottom: 1px solid #d8dde6;
  }
  nav a {
    display: inline-block;
    margin-right: 16px;
    padding: 6px 14px;
    border-radius: 4px;
    color: #102050;
    text-decoration: none;
    font-weight: 500;
    border: 1px solid #d8dde6;
  }
  nav a:hover { background: #102050; color: #fff; }
  nav a.home { background: #102050; color: #fff; }

  main { padding: 24px 32px; max-width: 1100px; margin: auto; }

  .card {
    background: #fff;
    border: 1px solid #d8dde6;
    border-radius: 8px;
    padding: 20px 24px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    margin-bottom: 24px;
  }
  .card h2 { margin-top: 0; color: #102050; }

  .gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 16px;
    margin-top: 16px;
  }
  .gallery figure {
    margin: 0;
    background: #fff;
    border: 1px solid #d8dde6;
    border-radius: 6px;
    overflow: hidden;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }
  .gallery figure img { width: 100%; display: block; }
  .gallery figure figcaption {
    padding: 8px 12px;
    font-size: 13px;
    color: #555;
    border-top: 1px solid #eef0f5;
  }

  pre {
    background: #0e1226;
    color: #e8eef5;
    padding: 16px 18px;
    border-radius: 6px;
    overflow: auto;
    font-size: 13px;
    line-height: 1.5;
  }
  footer {
    text-align: center;
    color: #777;
    font-size: 12px;
    padding: 24px;
  }
</style>
"""


def render_page(title, body):
    """Construieste o pagina HTML completa cu antet, navigare si continut."""
    nav = (
        f'<a class="home" href="{url_for("index")}">Acasa</a>'
        f'<a href="{url_for("tema_masini")}">Tema: Masini</a>'
        f'<a href="{url_for("element_c5")}">Citroen C5</a>'
        f'<a href="{url_for("c5_culori")}">Culori</a>'
        f'<a href="{url_for("c5_motoare")}">Motoare</a>'
        f'<a href="{url_for("c5_pachete")}">Pachete</a>'
    )

    return (
        "<!doctype html><html lang='ro'><head>"
        f"<meta charset='utf-8'><title>{title}</title>"
        f"{PAGE_CSS}"
        "</head><body>"
        f"<header><h1>{title}</h1>"
        "<div class='sub'>SCC - Proiect 441D / Tema Masini / Citroen C5 X</div>"
        "</header>"
        f"<nav>{nav}</nav>"
        f"<main>{body}</main>"
        "<footer>"
        "Iorga Iulian Dragos &middot; curs_scc_441D_masini "
        "&middot; Citroen C5 X (2022+)"
        "</footer>"
        "</body></html>"
    )


# ---------------------------------------------------------------------------
# Rute
# ---------------------------------------------------------------------------

@app.route("/", methods=['GET'])
def index():
    """Pagina principala: descriere scurta + 3 poze + linkuri."""
    descriere = biblioteca_masini.descriere_c5()

    body = ""
    body += "<div class='card'>"
    body += "<h2>Citroen C5 X — descriere tehnica scurta</h2>"
    body += f"<pre>{descriere}</pre>"
    body += "</div>"

    body += "<div class='card'>"
    body += "<h2>Galerie foto (3 imagini)</h2>"
    body += "<div class='gallery'>"
    body += (
        "<figure>"
        f"<img src='{url_for('static', filename='imagini/c5_fata.webp')}' alt='Fata'>"
        "<figcaption>Vedere din fata</figcaption></figure>"
    )
    body += (
        "<figure>"
        f"<img src='{url_for('static', filename='imagini/c5_lateral.webp')}' alt='Lateral'>"
        "<figcaption>Vedere laterala</figcaption></figure>"
    )
    body += (
        "<figure>"
        f"<img src='{url_for('static', filename='imagini/c5_spate.webp')}' alt='Spate'>"
        "<figcaption>Vedere din spate</figcaption></figure>"
    )
    body += "</div></div>"

    body += "<div class='card'>"
    body += "<h2>Sectiuni disponibile</h2>"
    body += "<ul>"
    body += (
        f"<li><a href='{url_for('c5_culori')}'>"
        "Optiuni de culoare</a></li>"
    )
    body += (
        f"<li><a href='{url_for('c5_motoare')}'>"
        "Optiuni de motorizare</a></li>"
    )
    body += (
        f"<li><a href='{url_for('c5_pachete')}'>"
        "Pachete (nivele de echipare)</a></li>"
    )
    body += "</ul>"
    body += "</div>"

    return render_page("Citroen C5 X — pagina principala", body)


@app.route("/masini", methods=['GET'])
def tema_masini():
    """Pagina pentru tema 'Masini'."""
    body = ""
    body += "<div class='card'>"
    body += "<h2>Tema: Masini</h2>"
    body += (
        "<p>Tema proiectului grupei 441D in cadrul cursului "
        "'Servicii Cloud si Containerizare' este <b>Masini</b>.</p>"
        "<p>In cadrul acestei teme, elementul ales pentru aceasta "
        "implementare este <b>Citroen C5</b> (generatia C5 X, 2022+).</p>"
    )
    body += "</div>"

    body += "<div class='card'>"
    body += "<h2>Elemente disponibile</h2>"
    body += "<ul>"
    body += f"<li><a href='{url_for('element_c5')}'>Citroen C5 X</a></li>"
    body += "</ul>"
    body += "</div>"

    return render_page("Tema: Masini", body)


@app.route("/c5", methods=['GET'])
def element_c5():
    """Pagina pentru elementul Citroen C5."""
    descriere = biblioteca_masini.descriere_c5()

    body = ""
    body += "<div class='card'>"
    body += "<h2>Element: Citroen C5 X</h2>"
    body += f"<pre>{descriere}</pre>"
    body += "</div>"

    body += "<div class='card'>"
    body += "<h2>Informatii detaliate</h2>"
    body += "<ul>"
    body += (
        f"<li><a href='{url_for('c5_culori')}'>"
        "Optiuni de culoare</a> — culoare_c5()</li>"
    )
    body += (
        f"<li><a href='{url_for('c5_motoare')}'>"
        "Optiuni de motorizare</a> — motor_c5()</li>"
    )
    body += (
        f"<li><a href='{url_for('c5_pachete')}'>"
        "Pachete</a> — pachete_c5()</li>"
    )
    body += "</ul>"
    body += "</div>"

    return render_page("Citroen C5 X", body)


@app.route("/c5/culori", methods=['GET'])
def c5_culori():
    """Optiuni de culoare pentru Citroen C5 X."""
    info = biblioteca_masini.culoare_c5()

    body = "<div class='card'>"
    body += "<h2>Optiuni de culoare — Citroen C5 X</h2>"
    body += f"<pre>{info}</pre>"
    body += "</div>"

    return render_page("Citroen C5 X — Culori", body)


@app.route("/c5/motoare", methods=['GET'])
def c5_motoare():
    """Optiuni de motorizare pentru Citroen C5 X."""
    info = biblioteca_masini.motor_c5()

    body = "<div class='card'>"
    body += "<h2>Optiuni de motorizare — Citroen C5 X</h2>"
    body += f"<pre>{info}</pre>"
    body += "</div>"

    return render_page("Citroen C5 X — Motoare", body)


@app.route("/c5/pachete", methods=['GET'])
def c5_pachete():
    """Pachete (nivele de echipare) pentru Citroen C5 X."""
    info = biblioteca_masini.pachete_c5()

    body = "<div class='card'>"
    body += "<h2>Pachete (nivele de echipare) — Citroen C5 X</h2>"
    body += f"<pre>{info}</pre>"
    body += "</div>"

    return render_page("Citroen C5 X — Pachete", body)


# ---------------------------------------------------------------------------
# Pornire locala (fara `flask run`)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011, debug=True)
