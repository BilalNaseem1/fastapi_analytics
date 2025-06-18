from pydantic import BaseModel, Field
from typing import Optional, Union


class EventSchema(BaseModel):
    id: int 