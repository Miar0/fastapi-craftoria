from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db_session
from app.schemas.health import HealthCheckResponse

router = APIRouter()

DbSession = Annotated[AsyncSession, Depends(get_db_session)]


@router.get(
    "/health",
    status_code=status.HTTP_200_OK,
    summary="Health Check",
)
async def health_check(db: DbSession) -> HealthCheckResponse:
    try:
        await db.execute(text("SELECT 1"))
        return HealthCheckResponse(status="ok", database="connected")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Database connection error: {e!s}",
        ) from e
