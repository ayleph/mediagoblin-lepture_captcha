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
import wtforms

from mediagoblin.tools.translate import lazy_pass_to_ugettext as _
from mediagoblin.auth.tools import normalize_user_or_email_field
from mediagoblin.plugins.basic_auth import auth_forms


class CaptchaRegistrationForm(auth_forms.RegistrationForm):
    captcha_response = wtforms.StringField(
        _('Captcha response'),
        [wtforms.validators.InputRequired()])
