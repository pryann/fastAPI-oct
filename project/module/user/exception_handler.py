import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .exception import NotFoundError


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(NotFoundError)
    async def not_found_handler(request: Request, exc: NotFoundError):
        logging.error(f"NotFoundError: {exc.message}")
        return JSONResponse(status_code=404, content={"detail": str(exc.message)})
