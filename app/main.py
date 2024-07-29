from fastapi import FastAPI

from loguru import logger

from app.routers import ssml_processing

app = FastAPI()

# Include the router
app.include_router(ssml_processing.router)

if __name__ == '__main__':
    import uvicorn
    logger.info("Starting server...")
    uvicorn.run(app, host="0.0.0.0", port=8030)
