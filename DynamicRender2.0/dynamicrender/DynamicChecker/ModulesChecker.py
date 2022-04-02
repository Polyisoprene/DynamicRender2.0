from typing import Optional, Union

from pydantic import BaseModel, AnyUrl


# 三级
class Fan(BaseModel):
    color: Optional[str] = None
    is_fan: Optional[bool] = None


# 二级
class Decorate(BaseModel):
    card_url: Optional[AnyUrl]
    fan: Optional[Fan]
    name: Optional[str]
    type: Optional[int]


class OfficialVerify(BaseModel):
    desc: Optional[str] = None
    type: Optional[int]


class Pendant(BaseModel):
    expire: Optional[int]
    image: Optional[AnyUrl]
    image_enhance: Optional[AnyUrl]
    name: str


class Vip(BaseModel):
    avatar_subscript_url: Union[AnyUrl, str, None] = None
    due_date: Optional[int]
    nickname_color: Optional[str]
    status: Optional[int]
    theme_type: Optional[int]
    type: Optional[int]


# 一级
class ModuleAuthor(BaseModel):
    decorate: Optional[Decorate] = None
    face: Optional[AnyUrl]
    face_nft: Optional[bool]
    following: Optional[int] = None
    jump_url: Optional[AnyUrl]
    label: Optional[str] = None
    mid: Optional[int]
    name: Optional[str]
    official_verify: Optional[OfficialVerify]
    pendant: Optional[Pendant] = None
    pub_time: str
    pub_ts: int
    type: str
    vip: Optional[Vip]


class ModuleDynamic(BaseModel):
    pass


class ModuleMore(BaseModel):
    pass


class ModuleStat(BaseModel):
    pass


class Modules(BaseModel):
    module_author: Optional[ModuleAuthor]
    module_dynamic: Optional[ModuleDynamic]
    module_more: Optional[ModuleMore]
    module_stat: Optional[ModuleStat]
