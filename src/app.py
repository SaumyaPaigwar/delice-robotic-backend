from fastapi import FastAPI

from src.configs import routes
from src.configs.constants import APP_NAME, BUILD_NUMBER
from src.routers import delice_router

app = FastAPI(
    docs_url=routes.DOCS_URL, openapi_url=routes.DOCS_URL + "/openapi.json",
    title="Delice Robotics",
    description="FUTURE OF FOOD PREPARATION"
)


@app.head(routes.HEALTHCHECK_URL, include_in_schema=False)
def healthcheck_head():
    return


@app.get(routes.HEALTHCHECK_URL, include_in_schema=False)
def healthcheck():
    return {
        "APP_NAME": APP_NAME,
        "BUILD_NUMBER": BUILD_NUMBER
    }


app.include_router(delice_router.router, prefix=routes.PREFIX, tags=["process"])
