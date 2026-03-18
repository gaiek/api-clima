from pydantic import BaseModel

class ClimaTempo(BaseModel):
    location: str
    temperature: float
    humidity: float
    description: str