# -*- coding: utf-8 -*-

##############################################################################
#
# fiscal_position_onchange_fix
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

from openerp import models, fields, api, exceptions


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def onchange_partner_id(self, type, partner_id, date_invoice=False,
            payment_term=False, partner_bank_id=False, company_id=False):
        res = super(AccountInvoice, self).onchange_partner_id(type, partner_id,
                    date_invoice, payment_term, partner_bank_id, company_id
        )
        addr = self.env['res.partner'].browse(partner_id).address_get(['delivery'])
        fiscal_position = self.env['account.fiscal.position'].get_fiscal_position(
            self.env.user.company_id.id, partner_id, addr['delivery']
        )
        if fiscal_position:
            res['value']['fiscal_position'] = fiscal_position
        return res