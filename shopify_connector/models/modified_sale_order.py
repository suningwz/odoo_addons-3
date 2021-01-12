import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)

class MyMixedInSaleOrderLine(models.Model):
    _name = 'sale.order.line'
    _inherit = ['sale.order.line']

    #test_field = fields.Char("Jack's Field")
    def create(self, values):
        _logger.info('Called create')
        record = super(MyMixedInSaleOrderLine, self).create(values)
        return record

    def flush(fnames, records):
        _logger.info('Called flush')
        _logger.info('Fnames: ' + str(fnames))
        record = super(MyMixedInSaleOrderLine, self).flush(values)
        return record

    def write(self, values):
       _logger.info('FYI: This is happening')
       _logger.info('order id object type: ' + str(type(self['order_id'])))
       order_id = self['order_id'].id
       order_lines = self.env['sale.order.line'].search([('order_id', '=', order_id)])
       total_quantity_to_deliver = 0
       total_quantity_delivered = 0
       for line in order_lines:
           total_quantity_to_deliver += line['qty_to_deliver']
           total_quantity_delivered += line['qty_delivered']
       _logger.info('Total quantity delivered: ' + str(total_quantity_delivered))
       _logger.info('Total quantity to deliver: ' + str(total_quantity_to_deliver))
       if total_quantity_delivered == total_quantity_to_deliver:
           #then we can call our api and say that this order is delivered
           _logger.info('the quantities are equal !')
       record = super(MyMixedInSaleOrderLine, self).write(values)
       return record
