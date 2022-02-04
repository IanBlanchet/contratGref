from sqlalchemy.ext.declarative import declarative_base
from app.config import session, engine
from sqlalchemy import Column, Integer, String, Boolean, Float, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship

Base = declarative_base()


class Contrat(Base):
    __tablename__ = "contrat"
    id = Column(Integer, primary_key=True)
    no = Column(String)
    description = Column(String)
    service = Column(String)
    event = relationship('Event', backref='contrat')

class Event(Base):
    __tablename__ = "event"
    id = Column(Integer, primary_key=True)
    echeance = Column(Date)
    description = Column(String)
    categorie = Column(String)
    contrat_id = Column(Integer, ForeignKey('contrat.id'))
    
Base.metadata.create_all(engine)