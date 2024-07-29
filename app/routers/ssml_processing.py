from fastapi import APIRouter, HTTPException

from app.model.ssml_model import ContentSSMLResponse, ContentSSMLRequest
from app.services.ssml_service import generate_ssml
from loguru import logger

router = APIRouter()


@router.post("/api/v1/process-content/", response_model=ContentSSMLResponse)
async def process_text(request: ContentSSMLRequest):
    try:
        logger.info(f"Received text: {request.content}")
        ssml_content = generate_ssml(request.content)
        logger.info(f"Generated SSML: {ssml_content}")
        return ContentSSMLResponse(
            code=200,
            status="success",
            message="SSML generated successfully",
            ssml=ssml_content
        )
    except Exception as e:
        logger.error(f"Error processing text: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
