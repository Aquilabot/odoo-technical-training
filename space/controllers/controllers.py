# -*- coding: utf-8 -*-
# from odoo import http


# class Space(http.Controller):
#     @http.route('/space/space', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/space/space/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('space.listing', {
#             'root': '/space/space',
#             'objects': http.request.env['space.space'].search([]),
#         })

#     @http.route('/space/space/objects/<model("space.space"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('space.object', {
#             'object': obj
#         })
