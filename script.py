import feedparser

# 1. Lire les actualités publiques
flux = feedparser.parse("https://news.ycombinator.com/rss")

# 2. Préparer le haut de notre site web (la vitrine)
html = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Mon Site d'Actualités Automatique</title>
</head>
<body>
    <h1>Les tendances Tech du jour</h1>
    
    <div style="background-color: #f0f0f0; padding: 10px; border: 1px solid #ccc;">
        <p><strong>Transparence :</strong> En tant que Partenaire Amazon, je réalise un bénéfice sur les achats remplissant les conditions requises.</p>
    </div>
    
    <ul>
"""

# 3. Prendre les 5 premiers articles du flux et créer les liens
for article in flux.entries[:5]:
    titre = article.title
    # Voici le faux lien d'affiliation Amazon généré
    lien_affiliation = f"https://www.amazon.fr/dp/B08N5WRWNW?tag=montag-21"

    html += f"<li>"
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
