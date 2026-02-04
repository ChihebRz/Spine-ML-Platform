from fastapi import FastAPI
from app.api.routes import predict, health
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
app = FastAPI(title="Spine ML Platform")

app.include_router(health.router, tags=["health"])
app.include_router(predict.router, tags=["prediction"])

# Mount static files (CSS + JS)
app.mount("/static", StaticFiles(directory="web/static"), name="static")

# Serve the main HTML page at root URL
@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    html_path = "web/templates/index.html"
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)
