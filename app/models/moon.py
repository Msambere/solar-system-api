from ..db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from typing import Optional

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    size: Mapped[str]
    description: Mapped[str]
    planet_id: Mapped[Optional[int]]= mapped_column(ForeignKey("planet.id"))