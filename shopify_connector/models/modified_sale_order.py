from odoo import fields, models, api

class MyMixedInSaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = ['sale.order']

    test_field = fields.Char("Jack's Field")

    @api.depends('delivery_count')
    def _on_delivered_count_change(self):
       _logger.debug('THink the delivery count changed!')
