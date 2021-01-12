import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)

class MyMixedInStockMoveLine(models.Model):
    _name = 'stock.move.line'
    _inherit = ['stock.move.line']

    #test_field = fields.Char("Jack's Field")
    # def create(self, values):
    #     _logger.info('Called create')
    #     record = super(MyMixedInSaleOrderLine, self).create(values)
    #     return record

    # def flush(fnames, records):
    #     _logger.info('Called flush')
    #     _logger.info('Fnames: ' + str(fnames))
        # record = super(MyMixedInSaleOrderLine, self).flush()
        # return record

    # def update(self, values):
    #     _logger.info('Called update on sales order line')
    #     record = super(MyMixedInSaleOrderLine, self).update(values)
    #     return record

    # @api.depends('qty_delivered')
    # def on_delivered_count_change(self):
    #     _logger.info('Called special function')

    def write(self, values):
       _logger.info('FYI: This is happening')
       if self['product_uom_qty'] == self['qty_done']:
           #then we can call our api and say that this order is delivered
           _logger.info('the quantities are equal !')
       record = super(MyMixedInStockMoveLine, self).write(values)
       return record
