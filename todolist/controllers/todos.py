from pyramid.view import view_config
from pyramid.renderers import get_renderer

from sqlalchemy.exc import DBAPIError #, IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    )

from todolist.models import (
    DBSession,
    Todo,
    )

# def site_layout():
#     renderer = get_renderer("templates/layout.pt")
#     layout = renderer.implementation().macros['layout']
#     return layout

# def include_defaults(**kwargs):
#     kwargs['layout'] = site_layout()
#     return kwargs

def get_todo_set():
    todos = DBSession.query(Todo).filter(Todo.done_at==None).order_by(Todo.priority.desc()).all()
    done_todos = DBSession.query(Todo).filter(Todo.done_at!=None).order_by(Todo.priority.desc()).all()
    return todos, done_todos



# todo next is move todos, done_todos = get_todo_set() into a decorator
# also test
@view_config(route_name='todo_index', renderer='todos/index.mako')
def index(request):
    todos, done_todos = get_todo_set()
    return dict(todos=todos, done_todos=done_todos)
    
@view_config(route_name='todo_create', renderer='json', request_method='POST', xhr=True)
def create(request):
    todo = Todo(
        task=request.POST.get('task', None), 
        priority=request.POST.get('priority', None)
    )
    if not todo.save():
        return {'errors': todo.errors}
    # todos, done_todos = get_todo_set()
    return {'id': todo.id, 'task': todo.task, 'priority':todo.priority, 'messages': '%s has been created' % todo.task } #, \
    #        'todos':todos, 'done_todos':done_todos}
    
@view_config(route_name='todo_update', renderer='json', request_method='POST', xhr=True)
def update(request):
    todo_id = request.matchdict['id']
    try:
        todo = DBSession.query(Todo).filter_by(id=todo_id).one()
    except NoResultFound:
        return {'errors': "No todo id: %s" % todo_id}
    
    todo.task=request.POST.get('task', None)
    todo.priority=request.POST.get('priority', None)
    # big bug here!
    if not todo.update():
        return {'errors': todo.errors}
    # todos, done_todos = get_todo_set()
    return {'task': todo.task, 'priority':todo.priority, 'messages': '%s has been updated' % todo.task} #, \
    #         'todos':todos, 'done_todos':done_todos}
    
@view_config(route_name='todo_delete', renderer='json', request_method='POST', xhr=True)
def delete(request):
    todo_id = request.matchdict['id']
    try:
        todo = DBSession.query(Todo).filter_by(id=todo_id).one()
    except NoResultFound:
        return {'errors': "No todo id: %s" % todo_id}     
    if not todo.delete():
        return {'errors': "%s can't be deleted" % todo.task}
    #todos, done_todos = get_todo_set()
    return {'id': todo.id, 'messages': '%s has been deleted' % todo.task}#, \
    #    'todos':todos, 'done_todos':done_todos}