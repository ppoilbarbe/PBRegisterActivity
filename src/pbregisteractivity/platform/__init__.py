"""Platform-specific abstractions for PBRegisterActivity."""

from .dirs import app_dir
from .lock import SingleInstance, SingleInstanceException

__all__ = ["app_dir", "SingleInstance", "SingleInstanceException"]
