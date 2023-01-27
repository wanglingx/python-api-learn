from flask_restful import Resource

class Names(Resource):
    def get(self):
        return dict(names='Hello Api')