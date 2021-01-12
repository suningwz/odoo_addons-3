import logging
from odoo import fields, models, api

class ShopifyStore(models.Model):
    _name = 'shopify_connector.store'
    _description = 'Shopify Store'
    api_key = fields.Char('API Key', required=True)
    password = fields.Char('Password', required=True)
    shop_name = fields.Char('Shop Name/Domain', required=True)
