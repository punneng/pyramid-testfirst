# import unittest
# class TestFunctionalTodolist(unittest.TestCase):
#     def setUp(self):
#         from todolist import main
#         app = main({})
#         from webtest import TestApp
#         self.testapp = TestApp(app)
        
        
#     def test_index_passed(self):
#         response = self.testapp.get('/', status=200)
# #     def test_create_passed(self):
# #         # self.assertEqual(response.status, '200 OK')
# #         # self.assertEqual(result.headerlist[0], ('Content-Type', 'application/json; charset=utf-8'))
# #         # body = response.app_iter[0]
# #         # self.assertIn(body, "New task")


# def test_create_without_xhr(self):
#     """
#         test_create_without_xhr
#         # note: this checking should be in the before_filter decorator
#         response = post("/todos", {'task':'New task'})
#         assert Raise HTTPForbidden
#     """
#     from todolist.controllers.todos import create
#     from pyramid.httpexceptions import HTTPForbidden
#     params = {'task':'New task'}
#     request = testing.DummyRequest(params=params, post=params)
#     dec_func = view_config(route_name='todo_create', renderer='json', request_method='POST', xhr=True)
#     #dec_func(route_name='todo_create', renderer='json', request_method='POST', xhr=True)
#     #response = dec_func(create)(request)
#     #print response
#     self.assertRaises(HTTPForbidden, dec_func(create), request)