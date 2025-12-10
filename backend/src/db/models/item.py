from db.db import Base
from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime

class Item(Base):
    __tablename__ = "item"

    # Core
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    sku: Mapped[str] = mapped_column(unique=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    quantity_on_hand: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )
    is_active: Mapped[bool] = mapped_column(default=True)

