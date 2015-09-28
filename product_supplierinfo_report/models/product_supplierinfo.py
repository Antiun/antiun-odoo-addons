# -*- coding: utf-8 -*-
# See README.rst file on addon root folder for license details

from openerp import models, fields, api


class ProductSupplierinfo(models.Model):
    _inherit = 'product.supplierinfo'

    price = fields.Char(string="Price", compute="_compute_price")
    product_uom = fields.Many2one(
        related="product_tmpl_id.uom_po_id", store=True,
        string="Supplier Unit of Measure", readonly="1",
        help="This comes from the product form.")

    @api.depends('pricelist_ids.min_quantity', 'pricelist_ids.price')
    def _compute_price(self):
        symbol = self.env.user.company_id.currency_id.symbol
        for record in self:
            price = ""
            for pricelist in record.pricelist_ids:
                price += ">= " + str(pricelist.min_quantity) + ": "
                price += str(pricelist.price) + symbol + " /"
            record.price = price
