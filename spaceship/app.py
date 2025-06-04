from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from spaceship.config import Settings
from spaceship.routers import api, health
from starlette.responses import FileResponse


def make_app(settings: Settings) -> FastAPI:
    app = FastAPI(
        debug=settings.debug,
        title=settings.app_title,
        description=settings.app_description,
        version=settings.app_version,
    )
    app.state.settings = settings

    print("Tkachenko Zenoviia")

    if settings.debug:
        app.mount("/static", StaticFiles(directory="build"), name="static")

    app.include_router(api.router, prefix="/api", tags=["api"])
    app.include_router(health.router, prefix="/health", tags=["health"])

    @app.get("/", include_in_schema=False, response_class=FileResponse)
    async def root() -> str:
        return "build/index.html"

    return app
