# -*- coding: utf-8 -*-
# See README.rst file on addon root folder for license details

{
    'name': "Product Supplier info Report",
    'category': 'Purchase Management',
    'version': '8.0.1.0.0',
    'depends': [
        'product_supplierinfo_for_customer',
    ],
    'external_dependencies': {},
    'data': [
        'views/product_supplierinfo_view.xml',
        'wizard/product_supplierinfo_print_wizard.xml',
        'report/product_supplierinfo_report.xml'
    ],
    'author': 'Antiun Ingeniería S.L., '
              'Odoo Community Association (OCA)',
    'website': 'http://www.antiun.com',
    'license': 'AGPL-3',
    'installable': True,
}
