#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

"""
Paramètres généraux
"""

# Tested with PYTHON 3.5. Not compatible with Python 2.x

import io
import os
from configparser import ConfigParser

from .utils import to_string


class _Parameters(object):
    PARAM_SECTION = "windows"
    GEOMETRY = "main_window_geometry"
    STATE = "main_window_state"

    def __init__(self):
        self._modified = False
        self._application_name = "PBRegisterActivity"
        self._config_dir = "." + self._application_name.lower()

        c = ConfigParser()
        self._conf = c

        c.read(self.config_file)

    def _base_dir(self):
        bd = os.path.join(os.environ['HOME'], self._config_dir)
        if not os.path.isdir(bd):
            os.mkdir(bd)
        return bd

    def _get_conf_str(self):
        f = io.StringIO()
        self._conf.write(f)
        return f.getvalue()

    @property
    def application_name(self):
        return self._application_name

    @property
    def config_file(self):
        return os.path.join(self._base_dir(), "config.ini")

    @property
    def activity_file(self):
        return os.path.join(self._base_dir(), "activity.txt")

    @property
    def unique_instance_lock_file(self):
        basename = "{0}_running_once.lock".format(self.application_name.lower())
        return os.path.join(self._base_dir(), basename)

    def get_window_geometry(self):
        return self._get_wininfo(self.GEOMETRY)

    def get_window_state(self):
        return self._get_wininfo(self.STATE)

    def _get_wininfo(self, name):
        if self._conf.has_option(self.PARAM_SECTION, name):
            return self._conf.get(self.PARAM_SECTION, name)
        return ""

    def set_window_geometry(self, geometry):
        self._set_wininfo(self.GEOMETRY, geometry)

    def set_window_state(self, state):
        self._set_wininfo(self.STATE, state)

    def _set_wininfo(self, name, data):
        d = to_string(data)
        if not self._conf.has_section(self.PARAM_SECTION):
            self._conf.add_section(self.PARAM_SECTION)
        if self._get_wininfo(name) != d:
            self._conf.set(self.PARAM_SECTION, name, d)
            self._modified = True

    def write(self):
        if self._modified:
            try:
                with open(self.config_file, "w") as f:
                    f.write(self._get_conf_str())
            except IOError:
                pass


parameters = _Parameters()
