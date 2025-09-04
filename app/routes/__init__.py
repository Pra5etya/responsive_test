def register_routes(app):
    from .app_route import app_bp

    # 
    app.register_blueprint(app_bp)      # App Routes