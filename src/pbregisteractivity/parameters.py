# -*- coding: utf-8 -*-
"""
Paramètres généraux
"""

# Tested with PYTHON 3.5. Not compatible with Python 2.x

import io
import os
from configparser import ConfigParser

from PyQt5.QtCore import QByteArray


class _Parameters(object):
    PARAM_SECTION = "windows"
    GEOMETRY = "_geometry"
    STATE = "_state"

    def __init__(self):
        self._modified = False
        self._application_name = "PBRegisterActivity"
        self._app_section = self._application_name.lower()
        self._config_dir = "." + self._application_name.lower()

        c = ConfigParser()
        self._conf = c

        c.read(self.config_file)

    def _base_dir(self):
        bd = os.path.join(os.environ["HOME"], self._config_dir)
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

    @property
    def day_duration(self):
        return self.app_get_float("day_duration", default=8.0)

    @day_duration.setter
    def day_duration(self, value):
        self.app_set("day_duration", "{:1.02f}".format(float(value)))

    @property
    def minimize_to_tray(self):
        return self.app_get_bool("minimize_to_tray", default=False)

    @minimize_to_tray.setter
    def minimize_to_tray(self, value):
        self.app_set("minimize_to_tray", bool(value))

    @property
    def auto_save(self):
        return self.app_get_bool("auto_save", default=False)

    @auto_save.setter
    def auto_save(self, value):
        self.app_set("auto_save", bool(value))

    @property
    def misc_duration(self):
        return self.app_get_int("miscellaneous_duration", default=60)

    @misc_duration.setter
    def misc_duration(self, value):
        self.app_set("miscellaneous_duration", int(value))

    def restore_window_state(self, window):
        name = window.WINDOW_NAME
        data = self._get_wininfo(name + self.GEOMETRY)
        if data != "":
            # noinspection PyArgumentList,PyCallByClass
            window.restoreGeometry(QByteArray.fromBase64(data.encode("utf-8")))

        if hasattr(window, "restoreState"):
            data = self._get_wininfo(name + self.STATE)
            if data != "":
                # noinspection PyArgumentList,PyCallByClass
                window.restoreState(QByteArray.fromBase64(data.encode("utf-8")))

    def save_window_state(self, window):
        name = window.WINDOW_NAME
        self._set_wininfo(name + self.GEOMETRY, window.saveGeometry().toBase64())
        if hasattr(window, "saveState"):
            self._set_wininfo(name + self.STATE, window.saveState().toBase64())

    def app_get(self, name, default=None):
        return self._conf.get(self._app_section, name, fallback=default)

    def app_set(self, name, value):
        old = self.app_get(name)
        if old is not None and old == value:
            return
        self._modified = True
        if not self._conf.has_section(self._app_section):
            self._conf.add_section(self._app_section)
        self._conf.set(self._app_section, name, str(value))

    def app_get_bool(self, name, default=False):
        return self._conf.getboolean(self._app_section, name, fallback=default)

    def app_get_int(self, name, default=None):
        return self._conf.getint(self._app_section, name, fallback=default)

    def app_get_float(self, name, default=None):
        return self._conf.getfloat(self._app_section, name, fallback=default)

    def write(self):
        if self._modified:
            try:
                with open(self.config_file, "w") as f:
                    f.write(self._get_conf_str())
                self._modified = False
            except IOError:
                pass

    def _get_wininfo(self, name):
        if self._conf.has_option(self.PARAM_SECTION, name):
            return self._conf.get(self.PARAM_SECTION, name)
        return ""

    def _set_wininfo(self, name, data):
        if isinstance(data, str):
            d = str
        else:
            d = str(data, encoding="utf8", errors="replace")
        if not self._conf.has_section(self.PARAM_SECTION):
            self._conf.add_section(self.PARAM_SECTION)
        if self._get_wininfo(name) != d:
            self._conf.set(self.PARAM_SECTION, name, d)
            self._modified = True


parameters = _Parameters()
