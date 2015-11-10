# -*- coding: utf-8 -*-
# License AGPL-3: Antiun Ingenieria S.L. - Antonio Espinosa
# See README.rst file on addon root folder for more details

from openerp import models, fields, api
import logging
from pprint import pprint, pformat
import traceback
_logger = logging.getLogger(__name__)


class Website(models.Model):
    _inherit = 'website'

    theme = fields.Many2one(
        string="Theme", comodel_name='ir.module.module', default=False,
        domain="[('website_multi_support', '=', True),"
               " ('state', '=', 'installed')]",
        help="Select theme for this domain. In order to see a theme addon "
             "selectable you must install the addon and it must support "
             "website multi (ir.module.module.website_multi_support = True)")
    layout = fields.Many2one(
        string="Layout", comodel_name='ir.ui.view', default=False,
        domain="[('layout', '=', True),"
               " ('type', '=', 'qweb')]",
        help="Select layout for this domain. Layout defines ")
    logo = fields.Binary(
        string="Website logo",
        help="This field holds the logo for this website, showed in header."
             "Recommended size is 180x50")

    @api.model
    def get_current_theme(self):
        return self.get_current_website().theme

    @api.model
    def new_page(self, name, template='website.default_page', ispage=True):
        """Change default page depending on website, if exits"""
        website = self.get_current_website().name
        template_module, template_name = template.split('.')
        imd = self.env['ir.model.data']
        if website:
            website = website.replace('.', '_').strip()
            _logger.info('new_page: website = %s' % pformat(website))
            alt_name = '_'.join([template_name, website])
            _logger.info('new_page: alt_name = %s' % pformat(alt_name))
            template_id = False
            try:
                _, template_id = imd.get_object_reference(
                    template_module, alt_name)
            except Exception:
                pass
            if template_id:
                template = '.'.join([template_module, alt_name])
        _logger.info('new_page: using template = %s' % pformat(template))
        return super(Website, self).new_page(
            name, template=template, ispage=ispage)
