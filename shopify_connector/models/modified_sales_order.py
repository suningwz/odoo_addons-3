import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)

class MyMixedInSaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = ['sale.order']

    platform_order_id = field.Char('Platform Order ID', required=True)
