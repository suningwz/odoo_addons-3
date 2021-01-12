import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)

class MyMixedInSaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = ['sale.order']

    #test_field = fields.Char("Jack's Field")

    @api.model
    def write(self, values):
       _logger.info('FYI: This is happening')
       order_id = self['id']
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
       record = super(MyMixedInSaleOrder, self).write(values)
       return record
