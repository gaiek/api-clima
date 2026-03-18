import redis
from fastapi import APIRouter, HTTPException
from app.infrastructure.redis_adapter import RedisAdapter
from app.application.clima_service import ClimaService
from app.infrastructure.visual_crossing_adapter import VisualCrossingAdapter
from app.config import settings

router = APIRouter()

redis_client = redis.Redis(host='localhost', port=6379, db=0)
api_key = settings.clima_api_key

clima_adapter = VisualCrossingAdapter(api_key)
cache_adapter = RedisAdapter(redis_client)
clima_service = ClimaService(clima_adapter, cache_adapter)

@router.get("/clima/{location}")
def get_clima(location: str):
    try:
        return clima_service.get_clima(location)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))