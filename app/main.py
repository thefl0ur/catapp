import asyncio

import httpx
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

CAT_FACT_URL = "https://meowfacts.herokuapp.com/"
CAT_IMAGE_URL = "https://api.thecatapi.com/v1/images/search"
FAVICON_PATH = "app/static/favicon.ico"

templates = Jinja2Templates(directory="app/templates")

app = FastAPI(docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


async def fetch_cat_fact(client: httpx.AsyncClient) -> str:
    response = await client.get(CAT_FACT_URL)
    response.raise_for_status()
    return response.json()["data"][0]


async def fetch_cat_image(client: httpx.AsyncClient) -> dict:
    response = await client.get(CAT_IMAGE_URL)
    response.raise_for_status()
    image_data = response.json()[0]
    return {
        "image_url": image_data["url"],
        "image_width": image_data["width"],
        "image_height": image_data["height"],
    }


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    context = {"request": request}

    async with httpx.AsyncClient() as client:
        fact_task = fetch_cat_fact(client)
        image_task = fetch_cat_image(client)

        fact, image_info = await asyncio.gather(fact_task, image_task)

        context["fact"] = fact
        context.update(image_info)

    return templates.TemplateResponse("main.jinja2", context)


@app.get("/favicon.ico", response_class=FileResponse)
async def favicon():
    return FileResponse(FAVICON_PATH)
