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
               #now we want to get the sale.order id of this stock move
               stock_move_parent = self.env['stock.move'].search([['id', '=', rec['move_id'].id]])
               sales_order_line = self.env['sale.order.line'].search([['id', '=', stock_move_parent['sale_line_id'].id]])
               sales_order = self.env['sale.order'].search([['id', '=', sales_order_line['order_id'].id]])
               #once we have that id, we can get the order and its associated store Domain, and shopify order id
               #its actually possible that they got an order from a platform that isnt shopify,
               #in which case we've broken all their write operations for this record
               #lets add an if to ask if the sales order contains the shopify store Domain
               if sales_order['shopify_store_domain'] != '':
                   shopify_store_domain = sales_order['shopify_store_domain']
                   shopify_order_id = sales_order['platform_order_id']
                   #now we want to look up our shopify stores against this domain
                   shopify_store = self.env['shopify_connector.store'].search([['shop_name', '=', shopify_store_domain]])
                   api_key = shopify_store['api_key']
                   password = shopify_store['password']
                   fulfillment_shop_url = "https://" + str(api_key) + ":" + str(password) +"@" + str(shopify_store_domain) + ".myshopify.com/admin/api/2020-10/orders/" + str(shopify_order_id) + "/fulfillments.json"

                   #fulfillment locaion id hardcoded here
                   #for now we're going to change this to the first location the store offers
                   #there should always be at least one
                   #it bears mentioning this location could totally be wrong
                   locations_shop_url = "https://" + str(api_key) + ":" + str(password) +"@" + str(shopify_store_domain) + ".myshopify.com/admin/api/2020-10/locations.json"

                   headers = {
                    'X-Shopify-Access-Token': password,
                    'Content-Type': "application/json"
                   }

                   locations_response = requests.get(locations_shop_url, headers=headers)

                   first_location_id = locations_response.json()['locations'][0]['id']

                   fulfillment_json = {
                      "fulfillment": {
                        #### THIS IS A HUGE PROBLEM ####
                        "location_id": first_location_id,
                        "shipment_status": "delivered",
                        "notify_customer": True
                      }
                    }
                   response = requests.post(fulfillment_shop_url, json=fulfillment_json, headers=headers)
                   _logger.info(response.json())
           record = super(MyMixedInStockMoveLine, self).write(values)
           return record
