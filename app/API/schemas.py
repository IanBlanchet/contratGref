from app.models import Contrat, Event
from flask_marshmallow import Marshmallow
from marshmallow import post_load, INCLUDE, EXCLUDE, fields
from app.config import session
from app import app


ma = Marshmallow(app)


class ContratSchema(ma.Schema):
    class Meta:
        model = Contrat
        include_fk = True
        unknown = EXCLUDE
        sqla_session = session
        fields = ('id', 'no', 'description', 'service')
        
    @post_load
    def make_position(self, data, **kwargs):
        return Contrat(**data)



class EventSchema(ma.Schema):
    class Meta:
        model = Event
        include_fk = True
        unknown = EXCLUDE
        sqla_session = session
        fields = ('id', 'echeance', 'description', 'categorie', 'contrat_id')

    @post_load
    def make_contrat(self, data, **kwargs):
        return Event(**data)





