from pydantic import BaseModel
from typing import Optional, Dict

class RecipeBase(BaseModel):
    cuisine: Optional[str]
    title: str
    rating: Optional[float]
    prep_time: Optional[int]
    cook_time: Optional[int]
    total_time: Optional[int]
    description: Optional[str]
    nutrients: Optional[Dict]
    serves: Optional[str]

class RecipeOut(RecipeBase):
    id: int

    class Config:
        orm_mode = True
