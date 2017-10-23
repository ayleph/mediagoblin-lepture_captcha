# mediagoblin-lepturecaptcha -- a plugin for GNU MediaGoblin
# This program is based on, and adapted from, GNU MediaGoblin.
# Copyright (C) 2016 Andrew Browning.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import logging

from mediagoblin import messages
from mediagoblin.tools import pluginapi
from mediagoblin.tools.translate import lazy_pass_to_ugettext as _

from hashlib import sha1

_log = logging.getLogger(__name__)


def extra_validation(register_form):
    config = pluginapi.get_config('mediagoblin.plugins.lepturecaptcha')
    captcha_secret = config.get('CAPTCHA_SECRET_PHRASE')

    if 'captcha_response' in register_form:
        captcha_response = register_form.captcha_response.data
    if 'captcha_hash' in register_form:
        captcha_hash = register_form.captcha_hash.data
        if captcha_hash == u'':
            for raw_data in register_form.captcha_hash.raw_data:
                if raw_data != u'':
                    captcha_hash = raw_data
    if 'remote_address' in register_form:
        remote_address = register_form.remote_address.data
        if remote_address == u'':
            for raw_data in register_form.remote_address.raw_data:
                if raw_data != u'':
                    remote_address = raw_data

    captcha_challenge_passes = False

    if captcha_response and captcha_hash:
        captcha_response_hash = sha1(captcha_secret + captcha_response).hexdigest()
        captcha_challenge_passes = (captcha_response_hash == captcha_hash)

    if not captcha_challenge_passes:
        register_form.captcha_response.errors.append(
            _('Sorry, CAPTCHA attempt failed.'))
        _log.info('Failed registration CAPTCHA attempt from %r.', remote_address)
        _log.debug('captcha response is: %r', captcha_response)
        _log.debug('captcha hash is: %r', captcha_hash)
        _log.debug('captcha response hash is: %r', captcha_response_hash)

    return captcha_challenge_passes
