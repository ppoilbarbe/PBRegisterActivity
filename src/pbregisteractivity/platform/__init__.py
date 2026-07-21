"""Platform-specific abstractions for PBRegisterActivity.

The implementation module for the current OS (``_linux``, ``_macos`` or
``_windows``) is selected once here, at import time, and its public symbols
are re-exported so the rest of the codebase only ever imports from
``pbregisteractivity.platform``.
"""

import sys

if sys.platform == "win32":
    from . import _windows as _impl
elif sys.platform == "darwin":
    from . import _macos as _impl
else:
    from . import _linux as _impl

app_dir = _impl.app_dir
SingleInstance = _impl.SingleInstance
SingleInstanceException = _impl.SingleInstanceException
apply = _impl.installer.apply

__all__ = ["app_dir", "SingleInstance", "SingleInstanceException", "apply"]
