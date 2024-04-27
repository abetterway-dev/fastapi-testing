from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/assets", StaticFiles(directory="public"), name="assets")
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello World"})

count = 0
@app.get("/htmx-test")
def say_hello():
    global count
    count += 1
    return f"<strong>Hello World for {count}{'st' if count == 1 else 'nd' if count == 2 else 'rd' if count == 3 else 'th'} time</strong>"
