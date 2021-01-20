import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)

class MyMixedInSaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = ['sale.order']

    platform_order_id = fields.Char('Platform Order ID')
    shopify_store_domain = fields.Char('Shopify Store Domain')

    def write(self, values):
       _logger.info('FYI: This is happening')
       for rec in self:
           if rec['shopify_store_domain'] != '':
               print('thinks we should let know shopify know...maybe')
               shopify_store_domain = rec['shopify_store_domain']
               shopify_order_id = rec['platform_order_id']
               ### CANCELLED CASE ###
               if rec['state'] == 'cancel':
                   shopify_store = self.env['shopify_connector.store'].search([['shop_name', '=', shopify_store_domain]])
                   api_key = shopify_store['api_key']
                   password = shopify_store['password']
                   order_shop_url = "https://" + str(api_key) + ":" + str(password) +"@" + str(shopify_store_domain) + ".myshopify.com/admin/api/2020-10/orders/" + str(shopify_order_id) + "/cancel.json"

                   headers = {
                    'X-Shopify-Access-Token': password,
                    'Content-Type': "application/json"
                   }

                   #no refund
                   #get reckt
                   cancel_json = {

                   }

                   response = requests.post(order_shop_url, json=cancel_json, headers=headers)
           record = super(MyMixedInStockMoveLine, self).write(values)
           return record
