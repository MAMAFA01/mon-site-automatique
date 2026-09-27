import feedparser

# 1. Lire les actualités publiques
flux = feedparser.parse("https://news.ycombinator.com/rss")

# 2. Préparer la vitrine avec notre "Décorateur" (Le bloc <style>)
html = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Les Tendances Tech</title>
    <style>
        /* --- DÉBUT DU DÉCORATEUR --- */
        body {
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; /* Police d'écriture moderne */
            background-color: #f4f7f6; /* Un gris très clair et doux pour le fond */
            color: #333333; /* Texte gris foncé, plus agréable à lire que le noir pur */
            max-width: 800px; /* On limite la largeur pour ne pas s'étaler sur les grands écrans */
            margin: 0 auto; /* On centre le site au milieu de l'écran */
            padding: 20px;
            line-height: 1.6; /* On aère le texte */
        }
        h1 {
            text-align: center;
            color: #2c3e50;
        }
        /* Style de notre encadré légal Amazon */
        .transparence {
            background-color: #e9ecef;
            padding: 15px;
            border-radius: 8px; /* Bords arrondis */
            font-size: 0.9em;
            text-align: center;
            margin-bottom: 30px;
        }
        /* Style pour transformer chaque article en jolie "carte" */
        .article-carte {
            background-color: #ffffff; /* Fond blanc pur */
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px; /* Bords arrondis */
            box-shadow: 0 4px 6px rgba(0,0,0,0.05); /* Petite ombre légère en dessous */
        }
        h2 {
            margin-top: 0;
            font-size: 1.3em;
            color: #0366d6;
        }
        /* Style pour les liens partenaires */
        a {
            color: #28a745; /* Joli vert vendeur */
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline; /* Souligne quand on passe la souris */
        }
        ul {
            list-style-type: none; /* On retire les vilains points de liste noirs */
            padding: 0;
        }
        /* --- FIN DU DÉCORATEUR --- */
    </style>
</head>
<body>
    <h1>🚀 Les tendances Tech du jour</h1>
    
    <div class="transparence">
        <p><strong>Transparence :</strong> En tant que Partenaire Amazon, je réalise un bénéfice sur les achats remplissant les conditions requises.</p>
    </div>
    
    <ul>
"""

# 3. Prendre les 5 premiers articles du flux et créer les liens dans des cartes
for article in flux.entries[:5]:
    titre = article.title
    lien_affiliation = f"https://www.amazon.fr/dp/B08N5WRWNW?tag=montag-21"

    # On utilise notre style "article-carte" créé plus haut
    html += f"<li class='article-carte'>"
    html += f"<h2>{titre}</h2>"
    html += f"<p>Ce sujet est passionnant. Découvrez l'outil idéal pour cela, disponible via <a href='{lien_affiliation}'>ce lien partenaire</a>.</p>"
    html += f"</li>"

# 4. Préparer le bas du site web
html += """
    </ul>
</body>
</html>
"""

# 5. Sauvegarder tout ce texte dans un fichier "index.html"
with open("index.html", "w", encoding="utf-8") as fichier:
    fichier.write(html)
