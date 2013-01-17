from pyramid.config import Configurator
from sqlalchemy import engine_from_config

import controllers # added manually
from .models import (
    DBSession,
    Base,
    )

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    # todo
    config.add_route('home', '/')
    config.add_route('todo_index', '/todos')
    config.add_route('todo_create', '/todos/create')
    config.add_route('todo_update', '/todos/{id}/update')
    config.add_route('todo_delete', '/todos/{id}/update')
    config.scan()
    return config.make_wsgi_app()

