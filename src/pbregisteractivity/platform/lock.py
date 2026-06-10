"""Verrou d'instance unique, indépendant de la plateforme.

- Linux / macOS : fcntl.lockf  (verrou consultatif POSIX sur un fichier)
- Windows       : msvcrt.locking (verrou d'octet sur un fichier)
"""

import os
import sys


class SingleInstanceException(BaseException):
    """Levée quand une autre instance du programme est déjà en cours."""


if sys.platform == "win32":
    import msvcrt

    class SingleInstance:  # type: ignore[no-redef]
        def __init__(self, lock_file: str) -> None:
            self._initialized = False
            self._lock_file = lock_file
            self._fp = open(lock_file, "w")  # noqa: SIM115
            self._fp.flush()
            try:
                msvcrt.locking(self._fp.fileno(), msvcrt.LK_NBLCK, 1)
            except OSError:
                print(
                    "Application déjà en cours de fonctionnement, fermeture.",
                    file=sys.stderr,
                )
                raise SingleInstanceException()
            self._initialized = True

        def __del__(self) -> None:
            if not self._initialized:
                return
            try:
                self._fp.seek(0)
                msvcrt.locking(self._fp.fileno(), msvcrt.LK_UNLCK, 1)
            except OSError:
                pass
            self._fp.close()
            try:
                os.unlink(self._lock_file)
            except OSError:
                pass

else:
    import fcntl

    class SingleInstance:  # type: ignore[no-redef]
        def __init__(self, lock_file: str) -> None:
            self._initialized = False
            self._lock_file = lock_file
            self._fp = open(lock_file, "w")  # noqa: SIM115
            self._fp.flush()
            try:
                fcntl.lockf(self._fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError:
                print(
                    "Application déjà en cours de fonctionnement ailleurs et "
                    "pas forcément sur ce poste, fermeture.",
                    file=sys.stderr,
                )
                raise SingleInstanceException()
            self._initialized = True

        def __del__(self) -> None:
            if not self._initialized:
                return
            fcntl.lockf(self._fp, fcntl.LOCK_UN)
            if os.path.isfile(self._lock_file):
                os.unlink(self._lock_file)
