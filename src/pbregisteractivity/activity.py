#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

"""
Enregistre l'activité
"""

# Tested with PYTHON 3.5. Not compatible with Python 2.x

import html
from datetime import datetime

from .parameters import parameters


class ActivityError(Exception):
    def __init__(self, fmt, *args, **kwargs):
        txt = fmt.format(*args, **kwargs)
        super().__init__(txt)


class Activity(object):
    DATE_FORMAT = "%Y%m%dT%H%M%S"

    def __init__(self, name, start, end, comment):
        self._name = "not set"
        self._start = datetime.now()
        self._end = datetime.now()
        self._comment = ""
        self._parent = None

        self.name = name
        self.start = start
        self.end = end
        self.comment = comment
        self.clear_modified()

    @classmethod
    def from_string(cls, string):
        fields = string.replace("%linefeed%", "\n").replace("%carriagereturn%", "\r").split("|", maxsplit=3)
        if len(fields) < 3:
            raise ActivityError("Ligne incorrectre, champs manquants: {0}", string)
        if len(fields) <= 3:
            fields.append("")
        return cls(fields[0].strip(),
                   fields[1].strip(),
                   fields[2].strip(),
                   fields[3].strip())

    def as_string(self):
        result = "{name}|{start}|{end}|{comment}".format(
            name=self.name,
            start=self.start.strftime(self.DATE_FORMAT),
            end=self.end.strftime(self.DATE_FORMAT),
            comment=self.comment,
        )
        return result.replace("\n", "%linefeed%").replace("\r", "%carriagereturn%")

    def as_html(self):
        fmt = "".join((
            '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" ',
            '"http://www.w3.org/TR/REC-html40/strict.dtd">',
            '<html>',
            '<head>',
            '<meta name="qrichtext" content="1"/>',
            '<style type="text/css">',
            'p, li {{ white-space: pre-wrap; font-style:normal; font-family:monospace }} ',
            'p {{ margin-top:0px; margin-bottom:0px; margin-left:0px; ',
            'margin-right:0px; -qt-block-indent:0; text-indent:0px;}}',
            '</style>',
            '</head>',
            '''<body style="font-family:'Sans Serif'; ''',
            '''font-size:9pt; font-weight:400; font-style:normal;">''',
            "<h2>{name}</h2><p>{comment}</p>",
            "<ul>",
            "<li>Début : {start}</li>",
            "<li>Fin   : {end}</li>",
            "<li>Durée : {duration}<br>",
            "        {hduration:1.5f} (heure décimale)</li>",
            "</ul",
            '</body>',
            '</html>',
        ))
        result = fmt.format(
            name=html.escape(self.name),
            comment=html.escape(self.comment).replace("\n", "<br>"),
            start=self.start,
            end=self.end,
            duration=self.duration,
            hduration=self.hour_duration,
        )
        return result

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        x = str(value).replace("|", " ")
        if x != self._name:
            self._modified = True
            self._name = x

    @property
    def start(self):
        # Replace a pour effet de bord de créer une copie de date
        return self._start.replace(microsecond=0)

    @start.setter
    def start(self, value):
        x = self._to_datetime(value, "Date de début")
        if x != self._start:
            self._modified = True
            self._start = x

    @property
    def end(self):
        return self._end.replace(microsecond=0)

    @end.setter
    def end(self, value):
        x = self._to_datetime(value, "Date de fin")
        if x != self._end:
            self._modified = True
            self._end = x

    @property
    def duration(self):
        return self.end - self.start

    @property
    def hour_duration(self):
        return self.duration.total_seconds() / 3600.0

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        x = str(value).strip()
        if x != self._comment:
            self._modified = True
            self._comment = x

    @property
    def modified(self):
        return self._modified

    def clear_modified(self):
        self._modified = False

    def _to_datetime(self, value, msg):
        try:
            if isinstance(value, datetime):
                d = value
            else:
                d =  datetime.strptime(value, self.DATE_FORMAT)
            return d.replace(microsecond=0)
        except ValueError as e:
            raise ActivityError("{} '{}' invalide (pas au format ISO): {}",
                                msg, value, e)

    def __str__(self):
        return self.as_string()


class _Activities(object):
    def __init__(self):
        self._activities = []
        self._modified = False
        try:
            with open(parameters.activity_file, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line != "":
                        self._activities.append(Activity.from_string(line))
        except FileNotFoundError:
            pass

    def add(self, *args):
        for a in args:
            assert isinstance(a, Activity)
            if a not in self._activities:
                self._activities.append(a)
                self._modified = True

    def remove(self, *args):
        for a in args:
            assert isinstance(a, Activity)
            try:
                del self._activities[self._activities.index(a)]
                self._modified = True
            except ValueError:
                # a not in list
                pass

    def actvitiy_names(self):
        return sorted({x.name for x in self._activities})

    def all_activities(self, recent_first=False):
        return sorted([x for x in self._activities],
                      key=lambda x: x.start.isoformat() + " " + x.name,
                      reverse=recent_first)

    def modified(self):
        return self._modified or any([x.modified for x in self._activities])

    def write(self):
        if not self.modified():
            return
        with open(parameters.activity_file, "w", encoding="utf-8") as f:
            for x in self._activities:
                # noinspection PyTypeChecker
                print(x, file=f)
                x.clear_modified()
        self._modified = False


activities = _Activities()
