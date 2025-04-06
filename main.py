import logging
from fastapi import FastAPI

from src.internal import utils
from src.routes import contacts

logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.INFO)

app = FastAPI(
    title="Contacts Organizer", version="0.5", description="GoIT Home Work 08"
)

app.include_router(utils.router)
app.include_router(contacts.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
