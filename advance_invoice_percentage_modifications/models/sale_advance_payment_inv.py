# -*- coding: utf-8 -*-

##############################################################################
#
# advance_invoice_percentage_modifications
# Copyright (C) 2017 OpusVL (<http://opusvl.com/>)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api


class SaleAdvancePayementInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"


    @api.multi
    def onchange_method(self, advance_payment_method, product_id):
        """We need to inherit this to prevent product_id getting set back
        to false when we use a payment method of percentage
        """
        if advance_payment_method == 'percentage':
            return {'value': {'amount':0}}
        if product_id:
            product = self.env['product.product'].browse(product_id)
            return {'value': {'amount': product.list_price}}
        return {'value': {'amount': 0}}


    @api.multi
    def _prepare_advance_invoice_vals(self):
        """Inherit the prep func to pass in our flag
        Note that this func is called when 'Percentage' is selected on the
        Invoice Creation wizard
        """
        res = super(SaleAdvancePayementInv, self)._prepare_advance_invoice_vals()
        for k, v in res:
            v['advance_inv_flag'] = True
        return res
