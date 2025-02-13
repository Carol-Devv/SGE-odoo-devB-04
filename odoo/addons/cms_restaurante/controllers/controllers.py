# -*- coding: utf-8 -*-
# from odoo import http


# class CmsRestaurante(http.Controller):
#     @http.route('/cms_restaurante/cms_restaurante', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cms_restaurante/cms_restaurante/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cms_restaurante.listing', {
#             'root': '/cms_restaurante/cms_restaurante',
#             'objects': http.request.env['cms_restaurante.cms_restaurante'].search([]),
#         })

#     @http.route('/cms_restaurante/cms_restaurante/objects/<model("cms_restaurante.cms_restaurante"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cms_restaurante.object', {
#             'object': obj
#         })

