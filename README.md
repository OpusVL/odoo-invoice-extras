# Enhancements to Invoices Records and Printouts

This is intended to be a collection of little utilities to link together
objects for reporting, for example to provide a link from an invoice back
to its originating sales order so that fields on the sales order can be looked
up in report printouts etc.

## invoice\_delivery\_address

Add a delivery address, and hooks for adding more shipping-related addresses besides,
to the bottom of the invoice.

If the delivery address is the same as the invoice address partner, it is not shown.

## invoice\_sale\_link

This links back to an original sales order from an invoice, if that invoice was generated
from a sales order or from a delivery order that was in turn generated from a sales order.

It exposes the link table that Odoo holds internally, for use in reports.

## hide\_refund\_invoice\_if\_refunded
Small tweak to hide the 'Refund Invoice' button once an invoice has already been Refunded.
