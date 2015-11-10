.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

============================
Website multi domain manager
============================

This module was written to extend the functionality of website_multi to
support management of pages created in each website domai in an easy way.

It also allows to set a theme to each domain.


Installation
============

To install this module, you need to:

* Install addon themes you need, they must support multi website and
  inherit from this addon (ir.module.module.multi_website_support field)


Configuration
=============

To configure this module, you need to:

* Create domains in Settings > Configuration > Website settings
* Associate a theme to each domain


Usage
=====

You can go to Knowledge > Websites

* Pages: To view all the pages and what domains belong to
* Menus: To view all menus and what domains belong to
* Domains: To see all domains declared and configure them
* Layouts: To see all views related with layouts
    * Layout
    * Header
    * Foooter
    * Default page
* Website wizard: Wizard for creating a new domain website
    * Create a new domain
    * Create a top menu
    * Create a home page
    * Create a contact us page (with form if website_crm is installed)
    * Create a default layout, default header, default footer and default page


Known issues / Roadmap
======================

* Set a list of users allowed to edit pages for a domain


Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/Antiun/antiun-odoo-addons/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback
`here <https://github.com/Antiun/antiun-odoo-addons/issues/new?body=module:%20{module_name}%0Aversion:%20{version}%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.


License
=======

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/agpl-3.0-standalone.html>.


Credits
=======

Contributors
------------

* Rafael Blasco <rafabn@antiun.com>
* Antonio Espinosa <antonioea@antiun.com>


Maintainer
----------

.. image:: http://www.antiun.com/images/logo.png
   :alt: Antiun Ingeniería S.L.
   :target: http://www.antiun.com

This module is maintained by Antiun Ingeniería S.L.

Antiun Ingeniería S.L. is an IT consulting company especialized in Odoo
and provides Odoo development, install, maintenance and hosting
services.

To contribute to this module, please visit https://github.com/Antiun
or contact us at comercial@antiun.com
