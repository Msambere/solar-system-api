from flask import abort, make_response
from ..db import db

# Helper Functions
def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        response = {"msg": f"{cls.__name__} id {model_id} is invalid."}
        abort(make_response(response,400))
    
    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)

    if not model:
        response = {"msg": f"{cls.__name__} id {model_id} not found."}
        abort(make_response(response,404))

    return model