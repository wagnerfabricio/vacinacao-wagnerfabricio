from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import CheckConstraint, Column, String, DateTime
from datetime import timedelta, datetime as dt

@dataclass
class Vaccine(db.Model):
    cpf: str
    name: str
    first_shot_date: str
    second_shot_date: str
    vaccine_name: str
    health_unit_name: str

    __tablename__ = "vaccine_cards"

    cpf = Column(String(11), CheckConstraint('length("cpf") = 11'), primary_key=True)
    name = Column(String, nullable=False)
    first_shot_date = Column(DateTime)
    second_shot_date = Column(DateTime)
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String)

    days_second_shot = 90
    expected_keys = ["cpf", "name", "vaccine_name", "health_unit_name"]


    def __init__(self, cpf, name, vaccine_name, health_unit_name, **kwargs):
        self.cpf = cpf
        self.name = name.title()
        self.vaccine_name = vaccine_name.title()
        self.health_unit_name = health_unit_name.title()
        self.first_shot_date = dt.now()
        self.second_shot_date = self.first_shot_date + timedelta(days=self.days_second_shot)


    @classmethod
    def serialize(cls, data: dict) -> dict:
        return {
            "cpf": data.cpf,
            "name": data.name,
            "vaccine_name": data.vaccine_name,
            "health_unit_name": data.health_unit_name,
            "first_shot_date": data.first_shot_date.strftime(),
            "second_shot_date": data.second_shot_date.strftime()
        }
