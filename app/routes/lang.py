# Data multi-bahasa
translations = {
    "id": {
        "title": "Selamat Datang di Website Kami",
        "description": "Website resmi dengan dukungan bahasa Indonesia, Inggris, dan Prancis.",
        "heading": "Tentang Kami",
        "content": "Kami menyediakan layanan global dalam berbagai bahasa."
    },
    "en": {
        "title": "Welcome to Our Website",
        "description": "Official website available in English, Indonesian, and French.",
        "heading": "About Us",
        "content": "We provide global services in multiple languages."
    },
    "fr": {
        "title": "Bienvenue sur notre site web",
        "description": "Site officiel disponible en français, indonésien et anglais.",
        "heading": "À propos de nous",
        "content": "Nous proposons des services mondiaux dans plusieurs langues."
    }
}



# @app.route('/')
# def home():
#     lang = request.accept_languages.best_match(["id", "en", "fr"]) or "en"
#     return redirect(url_for('index', lang=lang))

# @app.route('/<lang>/')
# def index(lang):
#     if lang not in translations:
#         lang = "en"
#     data = translations[lang]
#     return render_template("index.html", lang=lang, data=data)