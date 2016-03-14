# -*- coding: utf-8 -*-
{
    'name': "account.invoice.line - split SKU and description fields",

    'summary': """
        Technical Module - Add separate SKU and Description to the account.invoice.line model
    """,

    'description': """
        This is a technical module, to assist with report customisation.

        Provides a product_sku and description_without_sku fields on account.invoice.line

        product_sku is the default_code from the product_id, and
        description_without_sku is the 'name' (Description) field with the [SKU] stripped
        from the beginning if present.
    """,

    'author': "OpusVL",
    'website': "http://opusvl.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Technical',
    'version': '0.1',

    'depends': ['account'],

    # always loaded
    'data': [
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
