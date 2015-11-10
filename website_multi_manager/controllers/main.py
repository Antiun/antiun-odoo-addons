# -*- coding: utf-8 -*-
# License AGPL-3: Antiun Ingenieria S.L. - Antonio Espinosa
# See README.rst file on addon root folder for more details

import functools
from cStringIO import StringIO

import openerp
from openerp.modules import get_module_resource
from openerp import http
from openerp.http import request

db_monodb = http.db_monodb


class Website(http.Controller):

    @http.route([
        '/web/binary/website_logo',
        '/website_logo',
        '/website_logo.png',
    ], type='http', auth="none", cors="*")
    def website_logo(self, dbname=None, **kw):
        imgname = 'website_nologo.png'
        placeholder = functools.partial(
            get_module_resource,
            'website_multi_manager', 'static', 'src', 'img')
        uid = None
        if request.session.db:
            dbname = request.session.db
            uid = request.session.uid
        elif dbname is None:
            dbname = db_monodb()

        if not uid:
            uid = openerp.SUPERUSER_ID

        response = False
        if dbname:
            try:
                # create an empty registry
                registry = openerp.modules.registry.Registry(dbname)
                env = request.httprequest.environ
                domain_name = env.get('HTTP_HOST', '').split(':')[0]
                with registry.cursor() as cr:
                    cr.execute("""SELECT logo, write_date
                                    FROM website
                                   WHERE name = %s
                               """, (domain_name,))
                    row = cr.fetchone()
                    if row and row[0]:
                        image_data = StringIO(str(row[0]).decode('base64'))
                        response = http.send_file(
                            image_data, filename=imgname, mtime=row[1])
                    # AEA - Un-comment this for using company logo by default
                    #if not response:
                    #    cr.execute("""SELECT c.logo_web, c.write_date
                    #                    FROM res_users u
                    #               LEFT JOIN res_company c
                    #                      ON c.id = u.company_id
                    #                   WHERE u.id = %s
                    #               """, (uid,))
                    #    row = cr.fetchone()
                    #    if row and row[0]:
                    #        image_b64 = StringIO(str(row[0])
                    #        image_data = image_b64.decode('base64'))
                    #        response = http.send_file(
                    #           image_data, filename=imgname, mtime=row[1])
            except Exception:
                response = http.send_file(placeholder(imgname))
        if not response:
            response = http.send_file(placeholder(imgname))
        return response
