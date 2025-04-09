import fastapi
import typing
import uvicorn
import app

asgi_app = fastapi.FastAPI(__name__)

@asgi_app.get('/api')
def index() -> typing.Any:
    return {
        'status': 'ok'
    }

if __name__ == '__main__':
    settings = app.AppSettings()

    uvicorn.run(asgi_app,
        host=settings.app_host,
        port=settings.app_port,
        reload=True,
    )
