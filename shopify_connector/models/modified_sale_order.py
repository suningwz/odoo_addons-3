import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)

class MyMixedInSaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = ['sale.order']

    test_field = fields.Char("Jack's Field")

    @api.model
    def write(self):
       _logger.debug('THink the delivery count changed!')
       _logger.info('FYI: This is happening')
