"""Import sub-module ORM modules so their tables register on Base.metadata."""

import app.modules.sample_folder_structure_main_module.sub_module_1.model as sub_module_one_model
import app.modules.sample_folder_structure_main_module.sub_module_2.model as sub_module_two_model

__all__ = ["sub_module_one_model", "sub_module_two_model"]
