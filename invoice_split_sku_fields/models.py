# -*- coding: utf-8 -*-

from openerp import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'account.invoice.line'

    description_without_sku = fields.Char(
        compute="_description_without_sku_compute",
        readonly=True,
    )

    product_sku = fields.Char(
        related=['product_id', 'default_code'],
        readonly=True,
    )

    @api.depends('name', 'product_sku')
    @api.one
    def _description_without_sku_compute(self):
        if self.product_sku and self.name:
            sku_prefix = '[%s] ' % (self.product_sku,)
            self.description_without_sku = self.name.replace(sku_prefix, '')
        else:
            self.description_without_sku = self.name

