# -*- coding: utf-8 -*-
# from odoo import http


# class F:\odoo-community-1\extra\aradosFollowups(http.Controller):
#     @http.route('/f:\odoo-community-1\extra\arados_followups/f:\odoo-community-1\extra\arados_followups/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/f:\odoo-community-1\extra\arados_followups/f:\odoo-community-1\extra\arados_followups/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('f:\odoo-community-1\extra\arados_followups.listing', {
#             'root': '/f:\odoo-community-1\extra\arados_followups/f:\odoo-community-1\extra\arados_followups',
#             'objects': http.request.env['f:\odoo-community-1\extra\arados_followups.f:\odoo-community-1\extra\arados_followups'].search([]),
#         })

#     @http.route('/f:\odoo-community-1\extra\arados_followups/f:\odoo-community-1\extra\arados_followups/objects/<model("f:\odoo-community-1\extra\arados_followups.f:\odoo-community-1\extra\arados_followups"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('f:\odoo-community-1\extra\arados_followups.object', {
#             'object': obj
#         })
