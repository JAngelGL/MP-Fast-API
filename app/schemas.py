from pydantic import BaseModel, Field, ConfigDict

class ItemBase(BaseModel):
    name: str = Field(..., min_length=2)
    description: str
    price: float = Field(..., gt=0)
    available: bool

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int

    model_config = ConfigDict(from_attributes=True)