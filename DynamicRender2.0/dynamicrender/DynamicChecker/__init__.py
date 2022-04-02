from typing import Optional

from pydantic import BaseModel

from BasicChecker import Basic
from ModulesChecker import Modules
from OriginChecker import Orig


class Item(BaseModel):
    id_str: str
    basic: Basic
    modules: Modules
    type: str
    orig: Optional[Orig]
