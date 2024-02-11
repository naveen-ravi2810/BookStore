from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from datetime import datetime


class BaseUUID(SQLModel):
    id: UUID = Field(primary_key=True, index=True, default_factory=uuid4)
    created_on: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime | None = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}
    )
