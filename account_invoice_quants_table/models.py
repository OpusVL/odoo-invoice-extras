# -*- coding: utf-8 -*-

from openerp import models, fields, api

class StockMove(models.Model):
    _inherit = 'stock.move'

    def lots_table(self):
        """Return list of dictionaries summarising lots for reports.

        The 'lot' field is the name of the lot, and the 'qty' field is
        the sum of the quantities shipped from the quant movement records
        pointing at lots with that name.

        E.g.
            [
                {'lot': '123456', 'qty': 0.5},
                {'lot': '654321', 'qty': 0.8},
            ]

        The above format was chosen to allow extension to add more lot and quant data
        to reports later.
        """
        counts = {}
        for quant in self.quant_ids.filtered('lot_id'):
            lot_name = quant.lot_id.name
            counts.setdefault(lot_name, 0.0)
            counts[lot_name] += quant.qty
        return [
            {'lot': lotname, 'qty': qty}
            for (lotname, qty) in sorted(counts.items())
        ]

class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    def lots_table(self):
        """Return list of dictionaries summarising lots for reports.

        The 'lot' field is the name of the lot, and the 'qty' field is
        the sum of the quantities shipped from the quant movement records
        pointing at lots with that name.

        E.g.
            [
                {'lot': '123456', 'qty': 0.5},
                {'lot': '654321', 'qty': 0.8},
            ]

        The above format was chosen to allow extension to add more lot and quant data
        to reports later.

        If the invoice line has no move_id associated with it, or the move doesn't have
        any quants or lots, then this will return the empty dictionary.
        """
        mv = self.move_id
        return mv.lots_table() if mv else {}
