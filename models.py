from mongoengine import *

# to be changed to azure conn string once deployed to production
connect('pakistan-census')


class District(Document):
    name = StringField(required = True)
    latitude = FloatField()
    longitude = FloatField()
    measurements = ListField(EmbeddedDocumentField(Measurement))

    meta = {
        'indexes': [
            'name',
            '$name'
        ]
    }

class Measurement(EmbeddedDocument):
    areaType = StringField() # rural or urban area type
    year = IntField()
    households =  IntField()
    male = IntField()
    female = IntField()
    transgenders = IntField()