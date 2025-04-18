from flask import Flask
from disaster_management.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Importing all blueprints
    from disaster_management.modules.main import main
    from disaster_management.modules.admin import admin
    from disaster_management.modules.vol import vol
    from disaster_management.modules.end_user import end_user
    from disaster_management.modules.org import org
    from disaster_management.modules.sub_admin import sub_admin
    from disaster_management.modules.errors import errors

    # Register all blueprints, setting their URL prefix
    app.register_blueprint(main, url_prefix="/")
    app.register_blueprint(admin, url_prefix="/admin")
    app.register_blueprint(vol, url_prefix="/vol")
    app.register_blueprint(end_user, url_prefix="/end_user")
    app.register_blueprint(org, url_prefix="/org")
    app.register_blueprint(sub_admin, url_prefix="/sub_admin")
    app.register_blueprint(errors)

    return app
