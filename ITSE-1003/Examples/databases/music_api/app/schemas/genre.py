from pydantic import BaseModel, ConfigDict, Field


class GenreBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, examples=["Rock"])
    description: str | None = Field(None, examples=["Guitar-driven music genre"])


class GenreCreate(GenreBase):
    pass


class GenreUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=100)
    description: str | None = None


class GenreOut(GenreBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
