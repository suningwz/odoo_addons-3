import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)

class MyMixedInSaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = ['sale.order']

    test_field = fields.Char("Jack's Field")

    @api.onchange('delivery_count')
    def _on_delivered_count_change(self):
       _logger.debug('THink the delivery count changed!')
