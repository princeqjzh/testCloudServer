from apps.auth.settings import config

if config.SERVER_ENV != 'dev':
    from gevent import monkey

    monkey.patch_all()
else:
    pass

from apps.auth.views.roles import role
from apps.auth.views.users import user
from apps.extention.views.tool import tool
from apps.message.views.message import message
from apps.public.views.public import public
from library.api.tFlask import tflask
from flask_cors import CORS


def create_app():
    app = tflask(config)
    register_blueprints(app)
    CORS(app, resources=r'/*')
    return app


def register_blueprints(app):
    app.register_blueprint(user, url_prefix="/v1/user")
    app.register_blueprint(message, url_prefix="/v1/message")
    app.register_blueprint(public, url_prefix="/v1/public")
    app.register_blueprint(role, url_prefix="/v1/role")
    app.register_blueprint(tool, url_prefix='/v1/tool')


if __name__ == '__main__':
    create_app().run(port=config.PORT)
