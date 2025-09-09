from flask import Blueprint, render_template, session
from config.logger import setup_logger

app_bp = Blueprint("main", __name__)
logger = setup_logger()

# 🔹 Inject role langsung ke blueprint
@app_bp.app_context_processor
def inject_role():
    # Ambil role dari session (default user)
    return {"role": session.get("role", "admin")}


# Public Pages
# ===========================
@app_bp.route("/")
def index():
    logger.info("Memasuki halaman utama")
    return render_template("index.html")

@app_bp.route("/about")
def about(): 
    logger.info("Memasuki halaman about")
    return render_template("about.html")

@app_bp.route("/services")
def services(): 
    logger.info("Memasuki halaman services")
    return render_template("services.html")

@app_bp.route("/portfolio")
def portfolio(): 
    logger.info("Memasuki halaman portfolio")
    return render_template("portfolio.html")

@app_bp.route("/contact")
def contact(): 
    logger.info("Memasuki halaman contact")
    return render_template("contact.html")


# Restricted Page
# ===========================
@app_bp.route("/forbidden")
def forbidden():
    logger.warning("Akses ditolak: user tidak punya izin")
    return render_template("restricted/forbidden.html"), 403

@app_bp.route("/unsupported")
def unsupported():
    logger.warning("Memasuki halaman unsupported")
    return render_template("restricted/unsupported.html"), 406


# Role Testing / Session Setter
# ===========================
@app_bp.route("/set_role/<role>")
def set_role(role):
    session["role"] = role
    logger.info(f"Role di-set ke {role}")
    return f"Role di-set ke {role}. <a href='/'>Kembali</a>"
