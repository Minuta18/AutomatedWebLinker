from pydantic_settings import BaseSettings
import typing

DbName: typing.TypeAlias = typing.Literal['sqlite', 'postgresql']

class AppSettings(BaseSettings):
    used_db: DbName
    sqlite_url: typing.Optional[str]
    postgres_url: typing.Optional[str]
    app_port: int = '8000'
    app_host: str = '0.0.0.0'
