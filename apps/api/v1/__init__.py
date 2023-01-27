from apps.api.v1.resource.names import Names
from apps.api import api

def register_ulrs():
    api.add_resource(Names,'/names',endpoint="names")