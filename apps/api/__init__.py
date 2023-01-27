from flask import Blueprint
from flask_restful import Api


blueprint = Blueprint('api',__name__,url_prefix='api/v1')
api = Api(blueprint) #for using blueprint Api

from apps.api.v1 import register_ulrs
register_ulrs()
