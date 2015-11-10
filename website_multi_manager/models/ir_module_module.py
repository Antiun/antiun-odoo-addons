# -*- coding: utf-8 -*-
# License AGPL-3: Antiun Ingenieria S.L. - Antonio Espinosa
# See README.rst file on addon root folder for more details

from openerp import models, fields, api


class IrModuleModule(models.Model):
    _inherit = 'ir.module.module'

    website_multi_support = fields.Boolean(
        string="Is a theme that supports multi-website?", default=False)
