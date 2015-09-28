# -*- coding: utf-8 -*-
# See README.rst file on addon root folder for license details

from openerp import models, fields, api, _
from openerp.exceptions import Warning

import logging
from pprint import pformat
_logger = logging.getLogger(__name__)


class ProductSupplierinfoPrintWizard(models.TransientModel):
    _name = 'product.supplierinfo.print.wizard'

    product_code = fields.Boolean(string="Partner Product Code")
    default_code = fields.Boolean(string="Internal Reference")
    min_qty = fields.Boolean(string="Minimal Quantity")
    delay = fields.Boolean(string="Delivery Lead Time")
    discount = fields.Boolean(string="Discount")
    supplierinfo_ids = fields.Many2many(comodel_name="product.supplierinfo",
                                        relation="supplierinfo_print_wizard")

    @api.multi
    def print_supplierinfo(self):
        if self.supplierinfo_ids.filtered(
                lambda r: r.name != self.supplierinfo_ids.name):
            raise Warning(
                _('You must select records with the same customer/supplier.'))
        self.supplierinfo_ids = self.env['product.supplierinfo'].browse(
            self.env.context.get('active_ids', []))
        data = self.read()
        _logger.info('DATA : %s' % pformat(data))
        datas = {
            'ids': [],
            'model': 'ir.ui.menu',
            'form': data
        }
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'product_supplierinfo_report.'
                           'product_supplierinfo_report',
            'datas': datas
        }
