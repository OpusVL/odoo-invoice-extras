# -*- coding: utf-8 -*-

##############################################################################
#
# hide_refund_invoice_if_refunded
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

from openerp.osv import fields, osv


class account_invoice_refund(osv.osv_memory):
    _inherit = "account.invoice.refund"

    def invoice_refund(self, cr, uid, ids, context=None):
        res = super(account_invoice_refund, self).invoice_refund(
            cr, uid, ids, context=context
        )
        self.pool.get('account.invoice').write(
            cr, uid, context.get('active_ids'), {
                'refund_created': True,
        }, context=context)
        return res
