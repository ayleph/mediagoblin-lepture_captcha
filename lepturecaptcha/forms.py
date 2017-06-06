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


class CaptchaStringField(wtforms.StringField):
    '''
    The below syntax for overriding the name of a field was copied from 
    code posted on github.com at the link below.

    https://github.com/wtforms/wtforms/issues/205
    '''
    def __init__(self, *args, **kwargs):
        name = kwargs.pop('name', None)
        super(CaptchaStringField, self).__init__(*args, **kwargs)
        if name:
            self.name = name
