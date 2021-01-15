import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)

class MyMixedInStockMoveLine(models.Model):
    _name = 'stock.move.line'
    _inherit = ['stock.move.line']


    def write(self, values):
       _logger.info('FYI: This is happening')
       for rec in self:
           if rec['product_uom_qty'] == rec['qty_done']:
               #then we can call our api and say that this order is delivered
               _logger.info('the quantities are equal !')
               _logger.info('move_id_type: ' + str(type(rec['move_id'])))
               _logger.info('move_id.id: ' + str(rec['move_id'].id))
               #now we want to get the sale.order id of this stock move
               stock_move_parent = self.env['stock.move'].search([['id', '=', rec['move_id'].id]])
               _logger.info('stock move parent: ' + str(stock_move_parent['id']))
               sales_order_line = self.env['sale.order.line'].search([['id', '=', stock_move_parent['sale_line_id']]])
               _logger.info('sale line parent: ' + str(sales_order_line['id']))
               sales_order = self.env['sale.order'].search([['id', '=', sales_order_line['order_id']]])
               #once we have that id, we can get the order and its associated store Domain, and shopify order domain

               #once we have the store domain we can hit up shopify's order api with those keys

               #and update the order status to delivered.
           record = super(MyMixedInStockMoveLine, self).write(values)
           return record