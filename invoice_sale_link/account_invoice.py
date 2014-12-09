# -*- coding: utf-8 -*-

##############################################################################
#
# Link from Invoice to its originating Sales Order
# Copyright (C) 2014 OpusVL (<http://opusvl.com/>)
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

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    sale_order_id = fields.Many2one('sale.order',
        compute='_compute_sale_order_id',
        string='Sales Order',
        readonly=True,
    )

    @api.depends('origin')
    @api.one
    def _compute_sale_order_id(self):
        cr = self.env.cr
        cr.execute('SELECT order_id FROM sale_order_invoice_rel WHERE invoice_id = %s', (self.id,))
        results = cr.fetchall()
        if len(results) == 0:
            self.sale_order_id = False
        elif len(results) == 1:
            self.sale_order_id = results[0][0]
        else:
            raise ValueError("More than one sale order linked to this invoice")


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
