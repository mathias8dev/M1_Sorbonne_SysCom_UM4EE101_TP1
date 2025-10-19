# README — Setup LaTeX (français) pour LaTeX Workshop (VS Code)

Objectif : configurer un'environnement LaTeX en français sur Windows, Linux et macOS pour que l'extension LaTeX Workshop fonctionne correctement (compilation, affichage PDF, synctex).

## 1. Choix du moteur et packages recommandés
- Recommandé : utiliser latexmk + xelatex ou lualatex pour un support UTF‑8 et fontspec (meilleur pour le français moderne).
- Packages utiles : babel (ou polyglossia pour xelatex/lualatex), fontenc (T1), inputenc (si pdflatex), microtype, csquotes, biber (pour bibliographies).

## 2. Installation par plateforme

Windows
- Option simple : installer MiKTeX (https://miktex.org) ou TeX Live (https://tug.org/texlive/).
- Vérifier que les binaires sont sur le PATH (MiKTeX/TeX Live le fait normalement).
- Installer latexmk et biber via MiKTeX Console si nécessaire.

Linux (ex. Debian/Ubuntu)
- Exemple (Debian/Ubuntu) :
    sudo apt update
    sudo apt install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-lang-french latexmk biber
- Option complète (tout-en-un, volumineuse) :
    sudo apt-get install texlive-full -y
- Alternative légère / rapide (installer les paquets courants) :
    sudo apt-get install latexmk texlive-latex-extra texlive-lang-french -y
- Alternative : installer TeX Live via install-tl pour une version plus récente/complète.

macOS
- Installer MacTeX (https://tug.org/mactex/) ou BasicTeX + tlmgr.
- Si BasicTeX : sudo tlmgr install latexmk biber
- MacTeX ajoute /Library/TeX/texbin au PATH automatiquement.

## 3. VS Code — LaTeX Workshop (configuration minimale)
- Installer l’extension LaTeX Workshop.
- S’assurer que VS Code encode les fichiers en UTF‑8 (`"files.encoding": "utf8"`).
- Exemple minimal de `settings.json` pour utiliser latexmk + xelatex :

{
    "files.encoding": "utf8",
    "latex-workshop.latex.tools": [
        {
            "name": "latexmk",
            "command": "latexmk",
            "args": ["-synctex=1", "-interaction=nonstopmode", "-file-line-error", "-pdf", "-xelatex", "-outdir=%OUTDIR%", "%DOC%"]
        }
    ],
    "latex-workshop.latex.recipes": [
        {
            "name": "latexmk (xelatex)",
            "tools": ["latexmk"]
        }
    ],
    "latex-workshop.latex.autoBuild.run": "onSave",
    "latex-workshop.view.pdf.viewer": "tab"
}

- Si vous préférez pdflatex, remplacez `-xelatex` par l’option / outil adapté et utilisez inputenc + fontenc.

## 4. Option : latexindent (formatage / indentation)
- But : formater le code source LaTeX automatiquement (indentation, alignement).
- Installation :
  - TeX Live : sudo tlmgr install latexindent
  - Debian/Ubuntu : sudo apt install latexindent (ou installer le paquet TeX Live contenant latexindent comme texlive-extra-utils selon la distribution)
  - MiKTeX / MacTeX : latexindent est souvent disponible ; sinon installer via tlmgr ou MiKTeX Console.
  - Remarque : latexindent est un script Perl — il peut nécessiter des modules Perl (ex. YAML::Tiny). Si vous obtenez des erreurs, installez les modules manquants via cpan/cpanm (ex. `cpan -i YAML::Tiny`).
- Intégration dans VS Code (settings.json) — deux approches :

  a) Configuration de formatteur (LaTeX Workshop supporte directement latexindent) :
{
    "latex-workshop.latexindent.path": "latexindent",
    "latex-workshop.latexindent.args": ["-y=defaultIndent: '  '"]  // exemple d'argument YAML inline
}

  b) Définir comme outil / recette (pour l'utiliser manuellement ou dans une workflow) — étendre le bloc `latex-workshop.latex.tools` et `recipes` :

{
    "latex-workshop.latex.tools": [
        {
            "name": "latexmk",
            "command": "latexmk",
            "args": ["-synctex=1", "-interaction=nonstopmode", "-file-line-error", "-pdf", "-xelatex", "-outdir=%OUTDIR%", "%DOC%"]
        },
        {
            "name": "latexindent",
            "command": "latexindent",
            "args": ["-w", "%DOC%"] // -w pour écrire dans le fichier
        }
    ],
    "latex-workshop.latex.recipes": [
        {
            "name": "latexmk (xelatex)",
            "tools": ["latexmk"]
        },
        {
            "name": "Format (latexindent)",
            "tools": ["latexindent"]
        }
    ]
}

- Utilisation : lancer le formatage via la commande LaTeX Workshop (Format Document) ou via la recette ajoutée. Vérifier les chemins si VS Code ne trouve pas `latexindent`.

## 5. Préambule LaTeX minimal (deux variantes)

pdflatex (UTF‑8 compatible) :
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[french]{babel}
\usepackage{microtype}
\begin{document}
Bonjour, ceci est un test.
\end{document}

xelatex / lualatex (recommandé) :
\documentclass{article}
\usepackage{fontspec}
\usepackage[french]{babel} % ou \usepackage{polyglossia} + \setdefaultlanguage{french}
\usepackage{microtype}
\setmainfont{TeX Gyre Termes} % ou toute police système
\begin{document}
Bonjour, ceci est un test.
\end{document}

## 6. Vérifications & dépannage rapide
- Ouvrir un terminal dans VS Code et exécuter `latexmk --version` / `xelatex --version` / `latexindent --version` pour vérifier l’accès aux commandes.
- Si compilation échoue : consulter le log dans le panneau LaTeX Workshop (Output / LaTeX Workshop).
- SyncTeX (recherche avant/arrière) : nécessite `-synctex=1` (déjà dans l’exemple).
- Si packages manquants : MiKTeX peut installer à la volée ; TeX Live / tlmgr peuvent nécessiter l’installation manuelle.
- Pour biber : vérifier `biber --version` et ajouter aux recipes si utilisé.
- Pour latexindent : si formatage échoue, vérifier l'installation de Perl et des modules YAML::Tiny, File::HomeDir, etc.

