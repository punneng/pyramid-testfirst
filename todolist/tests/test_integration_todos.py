import unittest
import transaction
from datetime import datetime, timedelta

from pyramid.httpexceptions import HTTPNotFound
from pyramid import testing

from todolist.models import (
    Base,
    DBSession,
    Todo,
    )


class TestIntegrationTodolist(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        #engine = create_engine('sqlite:///todolist.sqlite')
        engine = create_engine('postgresql://dev:dev@localhost:5432/todolist_test')

        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        # the transaction commited after added so rolling back doesnt work on Postgres
        #with transaction.manager: 
        instances = (
            Todo(task='Second task', priority=0), 
            Todo(task='Thrid task', priority=5), 
            Todo(task='First task', priority=10),
            Todo(task="Done task", priority=5, done_at=datetime.now())
        )
        DBSession.add_all(instances)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()
        
    def test_index_pass(self):
        """ test_index_pass """
        from todolist.controllers.todos import index
        request = testing.DummyRequest()
        response = index(request)
        self.assertEqual(len(response['todos']), 3)
        self.assertEqual(len(response['done_todos']), 1)
        # test ordering
        self.assertEqual(response['todos'][0].task, "First task")
        self.assertEqual(response['todos'][2].task, "Second task")
    
    def test_create_pass(self):
        """ test_create_pass """
        from todolist.controllers.todos import create
        params = {'task':'New task', 'priority':1}
        request = testing.DummyRequest(params=params, post=params)
        response = create(request)
        self.assertTrue(response['id'])
        self.assertEqual(response['task'], params['task'])
        self.assertEqual(response['priority'], params['priority'])
    
    def test_create_fail(self):
        """ test_create_fail """
        from todolist.controllers.todos import create
        params = {'task':"", 'priority': "low"}
        request = testing.DummyRequest(params=params, post=params)
        response = create(request)
        self.assertTrue(response['errors'])
        self.assertEqual(len(response['errors']['priority']), 1)
        self.assertEqual(len(response['errors']['task']), 1)
        self.assertEqual(response['errors']['task'], ['Please enter a value'])

        
    def test_update_pass(self):
        """ test_update_pass """
        from todolist.controllers.todos import update
        params = {'task':'Updated task', 'priority':1}
        # provide the todo with id
        todo = DBSession.query(Todo).first()
        request = testing.DummyRequest(params=params, matchdict={'id':todo.id}, post=params)
        response = update(request)
        updated_todo = DBSession.query(Todo).filter_by(id=todo.id).one()
        self.assertEqual(response['task'], params['task'])
        self.assertEqual(updated_todo.task, params['task'])
        
    def test_update_fail(self):
        """ test_update_fail """
        from todolist.controllers.todos import update
        # test query not found
        request = testing.DummyRequest(params={}, matchdict={'id':1}, post={})
        response = update(request)
        self.assertEqual(response['errors'], "No todo id: 1")
        
        # test validation
        params = {'task':"", 'priority': "low"}
        todo = DBSession.query(Todo).first()
        request = testing.DummyRequest(params=params, matchdict={'id':todo.id}, post=params)
        response = update(request)
        self.assertTrue(response['errors'])
        self.assertEqual(len(response['errors']['priority']), 1)
        self.assertEqual(response['errors']['task'], ['Please enter a value'])
        self.assertEqual(response['errors']['priority'], ['Please enter an integer value'])
        
    def test_delete_pass(self):
        """ test_delete_pass """
        from todolist.controllers.todos import delete
        todo = DBSession.query(Todo).first()
        request = testing.DummyRequest(params={},matchdict={'id':todo.id}, post={})
        response = delete(request)
        todo_count = DBSession.query(Todo).count()
        self.assertIsNot(todo, DBSession.query(Todo).first())
        self.assertEqual(response['messages'], '%s has been deleted' % todo.task)
        self.assertEqual(todo_count, 3)
        
    def test_delete_fail(self):
        """ test_delete_fail """
        from todolist.controllers.todos import delete
        # test query not found
        request = testing.DummyRequest(params={}, matchdict={'id':1}, post={})
        response = delete(request)
        self.assertEqual(response['errors'], "No todo id: 1")
        

    
