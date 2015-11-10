# -*- coding: utf-8 -*-
# License AGPL-3: Antiun Ingenieria S.L. - Antonio Espinosa
# See README.rst file on addon root folder for more details

from openerp import models, fields, api

import logging
from pprint import pprint, pformat
import traceback
_logger = logging.getLogger(__name__)


class IrUiView(models.Model):
    _inherit = 'ir.ui.view'


    @api.model
    def get_inheriting_views_arch(self, view_id, model):
        # _logger.info('IrUiView::get_inheriting_views_arch: CUSTOM')
        sql_inherit = super(IrUiView, self).get_inheriting_views_arch(view_id, model)
        # _logger.info('IrUiView::get_inheriting_views_arch: CUSTOM sql_inherit = %s' % pformat(sql_inherit))
        sql_inherit_mod = []
        _logger.info('IrUiView::get_inheriting_views_arch: theme = %s' % pformat(self.env['website'].get_current_theme()))
        for view_arch, view_id in sql_inherit:
            view = self.browse(view_id)
            #if not view.xml_id.startswith('theme_enark.'):
            #    _logger.info('IrUiView::get_inheriting_views_arch: [+] view = %s' % pformat(view.xml_id))
            #    sql_inherit_mod.append((view_arch, view_id))
            #else:
            #    _logger.info('IrUiView::get_inheriting_views_arch: [-] view = %s' % pformat(view.xml_id))
            sql_inherit_mod.append((view_arch, view_id))

        return sql_inherit_mod

    @api.cr_uid_ids_context
    def render(self, cr, uid, id_or_xml_id, values=None, engine='ir.qweb', context=None):
        # _logger.info('IrUiView::render: xmlid = %s, request = %s, values = %s' % (pformat(id_or_xml_id), pformat(request), pformat(values)))
        _logger.info('IrUiView::render: theme = %s' % pformat(self.pool['website'].get_current_theme(cr, uid, context=context)))
        res = super(IrUiView, self).render(
            cr, uid, id_or_xml_id, values=values, engine=engine,
            context=context)
        return res
