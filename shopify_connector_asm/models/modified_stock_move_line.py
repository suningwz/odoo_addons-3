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
               #now we want to get the sale.order id of this stock move
               stock_move_parent = self.env['stock.move'].search([['move_id', '=', rec['move_id']]])
               _logger.info('stock move parent: ' + stock_move_parent)
               #once we have that id, we can get the order and its associated store Domain, and shopify order domain

               #once we have the store domain we can hit up shopify's order api with those keys

               #and update the order status to delivered.
           record = super(MyMixedInStockMoveLine, self).write(values)
           return record
