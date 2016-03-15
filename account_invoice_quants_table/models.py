# -*- coding: utf-8 -*-

from openerp import models, fields, api

class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    def quants_table(self):
        """Return list of dictionaries detailing lots for reports.

        E.g.
            [
                {'lot': '123456', 'qty': 0.5},
                {'lot': '654321', 'qty': 0.8},
            ]

        The above format was chosen to allow extension to add more quant data
        to reports later.
        """
        mv = self.move_id
        if not mv:
            return {}
        counts = {}
        for quant in mv.quant_ids.filtered('lot_id'):
            lot_name = quant.lot_id.name
            counts.setdefault(lot_name, 0.0)
            counts[lot_name] += quant.qty
        return [
            {'lot': lotname, 'qty': qty}
            for (lotname, qty) in sorted(counts.items())
        ]
