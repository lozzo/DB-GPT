from typing import TypedDict, Optional, Dict, List
from dataclasses import dataclass
from pydantic import BaseModel, Field
from typing import TypeVar, Generic, Any

T = TypeVar('T')

class PagenationFilter(BaseModel, Generic[T]):
    page_index: int = 1
    page_size: int  = 20
    filter: T = None

class PagenationResult(BaseModel, Generic[T]):
    page_index: int = 1
    page_size: int  = 20
    total_page: int = 0
    total_row_count: int = 0
    datas: List[T] = []

@dataclass
class PluginHubFilter(BaseModel):
    name: str
    description: str
    author: str
    email: str
    type: str
    version: str
    storage_channel: str
    storage_url: str


@dataclass
class MyPluginFilter(BaseModel):
    tenant: str
    user_code: str
    user_name: str
    name: str
    file_name: str
    type: str
    version: str


class PluginHubParam(BaseModel):
    channel: str  = Field(..., description="Plugin storage channel")
    url: str  = Field(..., description="Plugin storage url")

    branch: Optional[str]   =  Field(None, description="github download branch", nullable=True)
    authorization: Optional[str]   = Field(None, description="github download authorization", nullable=True)


