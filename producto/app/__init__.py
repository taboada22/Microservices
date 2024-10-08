from app.config import config
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate



db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

def create_app() -> None:
    app_context = os.getenv('FLASK_CONTEXT')
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    
    from app.resources import home
    app.register_blueprint(home, url_prefix='/api/v1')
    from app.resources import producto
    app.register_blueprint(producto)
    
    
    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app
