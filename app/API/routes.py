from flask.wrappers import Request
from app.API import bp
from app.models import Contrat, Event
from app import app
from app.config import session, engine
from flask_restful import Resource, Api, abort
from datetime import datetime, timedelta
from flask import Response, request
from flask_apispec.views import MethodResource
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec import marshal_with

from app.API.schemas import ContratSchema, EventSchema

api = Api(app)




# Serialize the data for the response
contrat_schema = ContratSchema(many=True)
event_schema = EventSchema(many=True)


class ContratApi(MethodResource,Resource):
    @marshal_with(contrat_schema)
    def get(self):
        "GET all contrat"       
        contrat = session.query(Contrat).all()
        return contrat_schema.dump(contrat)

    def post(self):
        
        return

class EventApi(MethodResource, Resource):
    @marshal_with(event_schema)
    def get(self):
        "Get related events"
        if request.args.get('contrat_id'):
            relatedEvents = session.query(Event).filter_by(contrat_id=request.args.get('contrat_id')).all()
            return event_schema.dump(relatedEvents)
        events = session.query(Event).all()
        return event_schema.dump(events)

api.add_resource(ContratApi, '/api/v1/contrat')
api.add_resource(EventApi, '/api/v1/event')


app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Gestion contrat légaux',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON 
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)

docs.register(ContratApi)
docs.register(EventApi)