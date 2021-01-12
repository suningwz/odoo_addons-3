import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)

class MyMixedInStockMoveLine(models.Model):
    _name = 'stock.move.line'
    _inherit = ['stock.move.line']

    def write(self, values):
       _logger.info('FYI: This is happening')
       if self['product_uom_qty'] == self['qty_done']:
           #then we can call our api and say that this order is delivered
           _logger.info('the quantities are equal !')
       record = super(MyMixedInStockMoveLine, self).write(values)
       return record
