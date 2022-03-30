from uuid import UUID
from enum import Enum
from datetime import datetime
from typing import Optional, List, Dict
from pydantic import BaseModel, AnyHttpUrl


class Dataset(int, Enum):
    ETHEREUM = 4
    XDAI = 6
    POLYGON = 7
    OPTIMISM_1 = 8
    OPTIMISM_2 = 10
    BINANCE = 9
    SOLANA = 1


class ParameterEnum(str, Enum):
    TEXT = 'text'
    ENUM = 'enum'
    DATETIME = 'datetime'


class User(BaseModel):
    id: int
    name: str
    profile_image_url: Optional[AnyHttpUrl]

    @property
    def handle(self) -> str:
        return f'@{self.name}'


class QueryParameter(BaseModel):
    key: str
    type: Optional[ParameterEnum]
    value: str
    enumOptions: Optional[List[str]]

    class Config:
        use_enum_values = True


class QueryMetadata(BaseModel):
    id: int
    name: str
    description: str
    user: User
    query: str  # SQL
    # https://sqlparse.readthedocs.io/en/latest/#:~:text=sqlparse%20is%20a%20non%2Dvalidating,of%20the%20New%20BSD%20license.
    parameters: List[QueryParameter]
    created_at: datetime
    updated_at: datetime


class RawRow(BaseModel):
    data: Dict
    __typename: str


class QueryResultData(BaseModel):
    id: UUID
    job_id: UUID
    runtime: int  # seconds
    generated_at: datetime
    columns: List[str]
    raw_data: List[RawRow]


class Query(BaseModel):
    metadata: QueryMetadata
    result_data: QueryResultData
