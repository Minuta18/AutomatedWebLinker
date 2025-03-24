from .conn_controller import DBConnectionController
from app import AppSettings

conn_str = ''
if AppSettings().used_db == 'sqlite':
    conn_str = f'sqlite+aiosqlite:///{ AppSettings().sqlite_url }'
elif AppSettings().used_db == 'postgresql':
    conn_str = f'postgresql+aiosqlite://{ AppSettings().postgres_url }'

db_controller = DBConnectionController(
    conn_str,
    AppSettings().used_db,
)
