from http import HTTPStatus
from flask import jsonify, request, current_app
from app.models.vaccine_model import Vaccine
from sqlalchemy.exc import DataError, IntegrityError
import re

def create():
    data = request.get_json()


    try: 
        new_vaccine = Vaccine(**data)
        session = current_app.db.session
        session.add(new_vaccine)
        session.commit()

        serialized = {
            "cpf": new_vaccine.cpf,
            "name": new_vaccine.name,
            "first_shot_date": new_vaccine.first_shot_date,
            "second_shot_date": new_vaccine.second_shot_date,
            "vaccine_name": new_vaccine.vaccine_name,
            "health_unit_name": new_vaccine.health_unit_name
        }

        return serialized, HTTPStatus.CREATED

    except AttributeError as e:
        return {
            "error": "value error",
            "expected": { key: "string" for key in Vaccine.expected_keys},
            "received": {key: type(value).__name__ for key, value in data.items()}
            }, HTTPStatus.BAD_REQUEST

    except DataError as e:
        return {"error": "cpf lenght must be 11 digits"}, HTTPStatus.BAD_REQUEST

    except TypeError as e:
        return {"error": e.args[0].split(" ", 1)[-1]}, HTTPStatus.BAD_REQUEST

    except IntegrityError as e:
        return {"error": e.args[0].split("Key (", 1)[-1].replace("(", " ").replace(")", " ").replace("\n", "")}, HTTPStatus.CONFLICT


def retrieve_all():
    vaccines = Vaccine.query.all()

    serialized = [{
            "cpf": vaccine.cpf,
            "name": vaccine.name,
            "first_shot_date": vaccine.first_shot_date,
            "second_shot_date": vaccine.second_shot_date,
            "vaccine_name": vaccine.vaccine_name,
            "health_unit_name": vaccine.health_unit_name
        } for vaccine in vaccines]

    return jsonify(serialized), HTTPStatus.OK
