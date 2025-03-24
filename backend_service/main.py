import fastapi
import typing

app = fastapi.FastAPI(__name__)

@app.get('/api')
def index() -> typing.Any:
    return {
        'status': 'ok'
    }
