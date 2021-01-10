# -*- coding: utf-8 -*-
# from odoo import http


# class OdooWebhookApp(http.Controller):
#     @http.route('/odoo_webhook_app/odoo_webhook_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_webhook_app/odoo_webhook_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_webhook_app.listing', {
#             'root': '/odoo_webhook_app/odoo_webhook_app',
#             'objects': http.request.env['odoo_webhook_app.odoo_webhook_app'].search([]),
#         })

#     @http.route('/odoo_webhook_app/odoo_webhook_app/objects/<model("odoo_webhook_app.odoo_webhook_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_webhook_app.object', {
#             'object': obj
#         })
