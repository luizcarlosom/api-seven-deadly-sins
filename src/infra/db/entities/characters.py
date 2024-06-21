from sqlalchemy import Column, String, Integer
from src.infra.db.settings.base import Base

class Characters(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    sin = Column(String, nullable=False)
    sacred_treasure = Column(String, nullable=True)
    description = Column(String, nullable=False)

    def __repr__(self):
        return f"Characters [id={self.id}, first_name={self.name}]"
