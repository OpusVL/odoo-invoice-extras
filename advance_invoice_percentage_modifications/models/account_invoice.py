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

from openerp import models, fields


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    advance_inv_flag = fields.Boolean(default=False, string="Advance Invoice",
        help="Displays whether the Invoice was created as an advance invoice, or not",
        readonly=True,
    )
