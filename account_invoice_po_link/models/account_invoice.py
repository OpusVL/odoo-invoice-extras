# -*- coding: utf-8 -*-

##############################################################################
#
# account_invoice_po_link
# Copyright (C) 2016 OpusVL (<http://opusvl.com/>)
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

from openerp import models, fields

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    purchase_ids = fields.Many2many(
        'purchase.order',
        'purchase_invoice_rel',
        'invoice_id',
        'purchase_id',
        copy=False,
        help="Purchase Orders which made this invoice",
    )
