import os


from flask import Flask


__author__ = 'kozloffsky@hotmail.com'

__all__ = ['create_app']


def create_app(app_name='project'):
    app = Flask(app_name,
                static_folder=os.path.join(os.path.dirname(__file__), '..', 'static'),
                template_folder="templates"
        )

    bootstrap_extensions(app)

    return app


def bootstrap_extensions(app):
    from .extensions import db, migrate
    db.init_app(app)

    migrate.init_app(app, db)


