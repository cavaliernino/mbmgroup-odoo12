# -*- coding: utf-8 -*-
from odoo import http

# class PortalOc(http.Controller):
#     @http.route('/portal_oc/portal_oc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/portal_oc/portal_oc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('portal_oc.listing', {
#             'root': '/portal_oc/portal_oc',
#             'objects': http.request.env['portal_oc.portal_oc'].search([]),
#         })

#     @http.route('/portal_oc/portal_oc/objects/<model("portal_oc.portal_oc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('portal_oc.object', {
#             'object': obj
#         })