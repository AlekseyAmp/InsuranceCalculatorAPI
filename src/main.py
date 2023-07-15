from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from config.settings import settings
from config.database import get_db_url

from routes import (
    insurance as InsuranceRouter,
    rate as RateRouter
)


app = FastAPI(title="InsuranceCalculator", version="0.1")


register_tortoise(
    app,
    db_url=get_db_url(
        user=settings.POSTGRESQL_USERNAME,
        password=settings.POSTGRESQL_PASSWORD,
        host=settings.POSTGRESQL_HOSTNAME,
        db_name=settings.POSTGRESQL_DATABASE
    ),
    modules={"models": ["models.rate"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/")
def root():
    return {
        "message": "Go to /docs"
    }


app.include_router(RateRouter.router, tags=['rates'], prefix='/api')
app.include_router(InsuranceRouter.router, tags=['insurance'], prefix='/api')
