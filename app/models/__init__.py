"""Import models from this package so they are registered on Base.metadata."""

from .base import Base

import app.modules.sample_folder_structure_main_module.models as sample_main_module_models

__all__ = ["Base", "sample_main_module_models"]
