"""Source des diagrammes du livrable 1 (MaintiDoc). Lancer : python make_diagrammes.py
Produit : architecture.png, flux_ingestion.png, flux_requete.png, flux_ticket.png"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = os.environ.get("DIAGOUT", os.path.dirname(os.path.abspath(__file__)))
BLUE, LBLUE, GRAY = "#2B6CB0", "#DCEBFA", "#4A4A4A"
ORANGE, LORANGE, GREEN, LGREEN, RED = "#E07B00", "#FDE3C0", "#2F855A", "#DDF3E4", "#C62828"


def canvas(w, h, xl, yl):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(*xl); ax.set_ylim(*yl); ax.axis("off")
    return fig, ax


def box(ax, x, y, w, h, text, fc=LBLUE, ec=BLUE, fs=8.5, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3,rounding_size=1.0", fc=fc, ec=ec, lw=1.4))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, fontweight="bold" if bold else "normal")


def arrow(ax, p1, p2, style="-|>", color=GRAY, lw=1.4, ls="-"):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=12, color=color, lw=lw, linestyle=ls))


def marker(ax, x, y, label):
    ax.plot([x], [y], "o", ms=15, mfc=RED, mec="white", mew=1.2, zorder=5)
    ax.text(x, y, label, color="white", fontsize=7.5, fontweight="bold", ha="center", va="center", zorder=6)


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ architecture
def architecture():
    fig, ax = canvas(10, 6.6, (0, 100), (-3, 70))
    W = 29
    box(ax, 1, 58, W, 9, "Interface web\n(question + photo, réponse,\nbrouillon de ticket à approuver)", fs=8)
    box(ax, 36, 58, W, 9, "API\n(authentification, groupe\nde l'utilisateur)", fs=8)
    box(ax, 70, 58, W, 9, "Orchestrateur de workflow\n(états, limites, pause pour\nvalidation humaine)", fs=8, fc=LORANGE, ec=ORANGE)
    arrow(ax, (30.6, 62.5), (35.4, 62.5)); arrow(ax, (65.6, 62.5), (69.4, 62.5))
    # bus orchestrateur -> 3 blocs
    ax.plot([84.5, 84.5], [58, 53], color=GRAY, lw=1.4); ax.plot([15.5, 84.5], [53, 53], color=GRAY, lw=1.4)
    for x in (15.5, 50.5, 84.5):
        arrow(ax, (x, 53), (x, 47.4))
    box(ax, 1, 34, W, 13, "Recherche documentaire\n(texte + images, filtre par groupe,\nfusion et reranking)", fs=8)
    box(ax, 36, 34, W, 13, "Modèle vision-langage\n(décrit la photo, rédige\nla réponse à partir des extraits)", fs=8)
    box(ax, 70, 34, W, 13, "Client MCP\n(historique, tickets ouverts,\ncréation après approbation)", fs=8)
    # bas
    box(ax, 1, 17, W, 11, "Index vectoriel\n(passages, figures, métadonnées)", fs=8)
    box(ax, 36, 17, W, 11, "Vérificateur\n(citations, format de sortie)", fs=8, fc=LGREEN, ec=GREEN)
    box(ax, 70, 17, W, 11, "Serveur MCP de maintenance\n(historique, tickets fictifs)", fs=8)
    arrow(ax, (15.5, 33.4), (15.5, 28.6), style="<|-|>"); arrow(ax, (50.5, 33.4), (50.5, 28.6))
    arrow(ax, (84.5, 33.4), (84.5, 28.6), style="<|-|>")
    box(ax, 1, 0, W, 11, "Ingestion\n(OCR, découpage, embeddings,\najout des métadonnées)", fs=8)
    box(ax, 36, 0, W, 11, "Stockage\n(fichiers originaux : MinIO ;\nmétadonnées : PostgreSQL)", fs=8)
    box(ax, 70, 0, W, 11, "Suivi et journalisation\n(MLflow, événements sans\ncontenu brut)", fs=8)
    arrow(ax, (15.5, 11.6), (15.5, 16.4)); arrow(ax, (30.6, 5.5), (35.4, 5.5), style="<|-|>")
    arrow(ax, (50.5, 11.6), (50.5, 16.4), style="<|-|>", ls="--")
    # points de contrôle
    marker(ax, 65.2, 67.2, "C1"); marker(ax, 30.4, 46.8, "C2"); marker(ax, 64.8, 10.6, "C3")
    marker(ax, 65.2, 27.6, "C4"); marker(ax, 98.6, 27.6, "C5"); marker(ax, 98.6, 46.6, "C6"); marker(ax, 98.6, 66.8, "C7")
    ax.text(50, -3, "Points de contrôle : C1 identité et groupe, C2 filtre avant recherche, C3 filtre à l'ouverture des fichiers, "
            "C4 citations et format,\nC5 autorisation à chaque appel MCP, C6 validation humaine du ticket, C7 budgets (appels, temps)",
            ha="center", va="top", fontsize=7.5, color=GRAY)
    save(fig, "architecture.png")


# ------------------------------------------------------------------ flux en serpentin
def snake(name, steps, per_row=4, w=20, h=13, gap=5.3, fs=7.8, figw=10, title_note=None):
    rows = (len(steps) + per_row - 1) // per_row
    H = rows * h + (rows - 1) * 12 + 8
    fig, ax = canvas(figw, 0.5 + rows * 1.8, (0, 100), (0, H))
    pos = []
    for i in range(len(steps)):
        r, c = divmod(i, per_row)
        col = c if r % 2 == 0 else per_row - 1 - c
        x = 1 + col * (w + gap)
        y = H - 4 - (r + 1) * h - r * 12
        pos.append((x, y))
    for i, (txt, mk, kind) in enumerate(steps):
        fc, ec = {"n": (LBLUE, BLUE), "h": (LORANGE, ORANGE), "v": (LGREEN, GREEN)}[kind]
        x, y = pos[i]
        box(ax, x, y, w, h, f"{i + 1}. {txt}", fc=fc, ec=ec, fs=fs)
        if mk:
            marker(ax, x + w - 0.5, y + h - 0.2, mk)
    for i in range(len(steps) - 1):
        (x1, y1), (x2, y2) = pos[i], pos[i + 1]
        if abs(y1 - y2) < 1e-6:
            if x2 > x1:
                arrow(ax, (x1 + w + 0.5, y1 + h / 2), (x2 - 0.5, y2 + h / 2))
            else:
                arrow(ax, (x1 - 0.5, y1 + h / 2), (x2 + w + 0.5, y2 + h / 2))
        else:
            arrow(ax, (x1 + w / 2, y1 - 0.5), (x2 + w / 2, y2 + h + 0.5))
    save(fig, name)


def flux():
    snake("flux_ingestion.png", [
        ("Documents PDF\net images\n(originaux conservés)", None, "n"),
        ("PDF scanné ?\noui : OCR local\nnon : extraction directe", None, "h"),
        ("Extraction du texte\net des images\n(PyMuPDF)", None, "n"),
        ("Découpage en\npassages, tableaux,\nfigures, pages", None, "n"),
        ("Embeddings texte\net image", None, "n"),
        ("Ajout des métadonnées\n(document, version, page,\néquipement, groupes)", None, "n"),
        ("Index vectoriel\n+ stockage des\nfichiers originaux", None, "v"),
    ])
    snake("flux_requete.png", [
        ("Question + photo\nenvoyées par\nl'utilisateur", None, "n"),
        ("Identité et groupe\nvérifiés", "C1", "h"),
        ("Photo décrite par\nle modèle vision-\nlangage", None, "n"),
        ("Recherche texte et\nimage dans les\ndocuments autorisés", "C2", "h"),
        ("Historique consulté\nvia MCP si utile\n(3 appels max)", "C5", "h"),
        ("Réponse rédigée\navec ses sources", None, "n"),
        ("Citations et format\nvérifiés", "C4", "h"),
        ("Réponse, clarification\nou abstention\nrenvoyée", None, "v"),
    ])
    snake("flux_ticket.png", [
        ("Brouillon du ticket\n(équipement, titre,\ndescription)", None, "n"),
        ("Contenu exact\naffiché à\nl'utilisateur", None, "n"),
        ("Approbation explicite\nrequise (toute\nmodification = nouvelle\nvalidation)", "C6", "h"),
        ("Jeton d'approbation\nlié à l'utilisateur\net au contenu", None, "n"),
        ("Appel create_ticket\navec clé\nd'idempotence", None, "n"),
        ("Serveur MCP :\ndroits, jeton,\ndoublon vérifiés", "C5", "h"),
        ("Ticket créé et\nconfirmation\njournalisée", None, "v"),
    ])


if __name__ == "__main__":
    architecture()
    flux()
    print("ok")
