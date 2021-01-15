import logging
import requests
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
               sales_order_line = self.env['sale.order.line'].search([['id', '=', stock_move_parent['sale_line_id'].id]])
               _logger.info('sale line id: ' + str(sales_order_line['id']))
               sales_order = self.env['sale.order'].search([['id', '=', sales_order_line['order_id'].id]])
               _logger.info('sale order id: ' + str(sales_order['id']))
               #once we have that id, we can get the order and its associated store Domain, and shopify order id
               shopify_store_domain = sales_order['shopify_store_domain']
               shopify_order_id = sales_order['platform_order_id']
               #now we want to look up our shopify stores against this domain
               shopify_store = self.env['shopify_connector.store'].search([['shop_name', '=', shopify_store_domain]])
               api_key = shopify_store['api_key']
               password = shopify_store['password']

               shop_url = "https://" + api_key + ":" + password +"@" + shopify_store_domain + ".myshopify.com/admin/api/2020-10/orders/" + shopify_order_id + ".json"

               order_json = {
                "order": {
                 "id": shopify_order_id,
                 "fulfillment_status": "fulfilled"
                }
               }

               #once we have the store domain we can hit up shopify's order api with those keys
               headers = {
                'X-Shopify-Access-Token': password,
                'Content-Type': "application/json"
               }

               response = requests.put(shop_url, json=order_json, headers=headers)
               _logger.info(response)
           record = super(MyMixedInStockMoveLine, self).write(values)
           return record
