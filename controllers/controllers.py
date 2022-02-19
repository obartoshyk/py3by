# -*- coding: utf-8 -*-
# from odoo import http


# class Py3by(http.Controller):
#     @http.route('/py3by/py3by', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/py3by/py3by/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('py3by.listing', {
#             'root': '/py3by/py3by',
#             'objects': http.request.env['py3by.py3by'].search([]),
#         })

#     @http.route('/py3by/py3by/objects/<model("py3by.py3by"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('py3by.object', {
#             'object': obj
#         })
