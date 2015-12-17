# -*- coding: utf-8 -*-
'''
Syndic module to declare a new Diacamma appli

@author: Laurent GAY
@organization: sd-libre.fr
@contact: info@sd-libre.fr
@copyright: 2015 sd-libre.fr
@license: This file is part of Lucterios.

Lucterios is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Lucterios is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Lucterios.  If not, see <http://www.gnu.org/licenses/>.
'''

from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _, ugettext
from os.path import join, dirname
import diacamma.syndic
from lucterios.framework import signal_and_lock


def get_subtitle():
    try:
        from django.apps.registry import apps
        legalentity = apps.get_model("contacts", "LegalEntity")
        our_detail = legalentity.objects.get(id=1)
        return our_detail.name
    except LookupError:
        return ugettext("Condominium application")

APPLIS_NAME = diacamma.syndic.__title__()
APPLIS_VERSION = diacamma.syndic.__version__
APPLI_EMAIL = "support@diacamma.org"
APPLIS_LOGO_NAME = join(dirname(__file__), "Diacamma.png")
APPLIS_FAVICON = join(dirname(__file__), "Diacamma.ico")
APPLIS_COPYRIGHT = _("(c) GPL Licence")
APPLIS_SUBTITLE = get_subtitle


@signal_and_lock.Signal.decorate('initial_account')
def initial_account_asso(account_list):
    if isinstance(account_list, list):
        account_list.append(join(dirname(__file__), 'init_french.csv'))
    return True
