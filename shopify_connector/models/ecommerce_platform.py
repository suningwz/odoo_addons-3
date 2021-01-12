import logging
from odoo import fields, models, api

class EcommercePlatform(models.Model):
    _name = 'shopify_connector.platform'
    _description = 'Ecommerce Platform'
    brand_name = fields.Char('Platform Brand Name', required=True)
    api_key = fields.Char('API Key', required=True)
    password = fields.Char('Password', required=True)
    shop_name = fields.Char('Shop Name/Domain', required=True)
