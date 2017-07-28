# -*- coding: utf-8 -*-

# //////////////////////////////////////////////////////////////////////
#
# Supplier Invoice Smart Button
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
# //////////////////////////////////////////////////////////////////////

# Generic module to add a 'Supplier Invoice Total' smart button to the partner view
# Method takes a kwarg 'price_field' that defaults to the base Odoo field which can be used for custom cases

from openerp.osv import fields, osv


class res_partner(osv.osv):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'Partner'

    def _supplier_invoice_total(self, cr, uid, ids, field_name, arg, context=None, price_field='price_total'):
        result = {}
        account_invoice_report = self.pool.get('account.invoice.report')
        user = self.pool['res.users'].browse(cr, uid, uid, context=context)
        user_currency_id = user.company_id.currency_id.id
        for partner_id in ids:
            all_partner_ids = self.pool['res.partner'].search(
                cr, uid, [('id', 'child_of', partner_id)], context=context)

            # searching account.invoice.report via the orm is comparatively expensive
            # (generates queries "id in []" forcing to build the full table).
            # In simple cases where all invoices are in the same currency than the user's company
            # access directly these elements

            # generate where clause to include multicompany rules
            where_query = account_invoice_report._where_calc(cr, uid, [
                ('partner_id', 'in', all_partner_ids), ('state', 'not in', ['draft', 'cancel'])
            ], context=context)
            account_invoice_report._apply_ir_rules(cr, uid, where_query, 'read', context=context)
            from_clause, where_clause, where_clause_params = where_query.get_sql()
            query = """ WITH currency_rate (currency_id, rate, date_start, date_end) AS (
                                SELECT r.currency_id, r.rate, r.name AS date_start,
                                    (SELECT name FROM res_currency_rate r2
                                     WHERE r2.name > r.name AND
                                           r2.currency_id = r.currency_id
                                     ORDER BY r2.name ASC
                                     LIMIT 1) AS date_end
                                FROM res_currency_rate r
                                )
                      SELECT SUM(%(price_field)s * cr.rate) as total
                        FROM account_invoice_report account_invoice_report, currency_rate cr
                       WHERE %(where_clause)s
                         AND cr.currency_id = %%s
                         AND (COALESCE(account_invoice_report.date, NOW()) >= cr.date_start)
                         AND (COALESCE(account_invoice_report.date, NOW()) < cr.date_end OR cr.date_end IS NULL)
                         AND account_invoice_report.type in ('in_invoice', 'in_refund')
                    """ % {"price_field": price_field, "where_clause": where_clause}
            cr.execute(query, where_clause_params + [user_currency_id])
            result[partner_id] = cr.fetchone()[0]

        return result

    _columns = {
        'supplier_total_invoiced': fields.function(_supplier_invoice_total, string="Supplier Invoiced", type='float',
                                          groups='account.group_account_invoice'),
    }
