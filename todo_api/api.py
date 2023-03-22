from flask_restful import Resource, reqparse
from flask import request

from werkzeug.security import generate_password_hash, check_password_hash

from todo_api.models import User, Tasks, db


ADMIN_TOKEN = 'q1w2e3'


class UserResource(Resource):
    def get():
        pass

    def post():
        pass

    def update():
        pass

    def delete():
        pass




class AdminUserResource(Resource):
    
    # Collecting any User
    def get(self, model_username=None) -> str or dict:
            
            if not model_username:

                if request.headers.get('AUTH_TOKEN') == None:
                    return 'Bad Token'
        
                if request.headers.get('AUTH_TOKEN') == ADMIN_TOKEN:
                    response = User.query.all()
                    return {'users': [{'id': user.id, 'name': user.username} for user in response]}

                return 'Bad Request "NOT VALID USER"'
            else:
                response = User.query.filter_by(username=model_username).first()
                if not response:
                    return '404'
                return {'id': response.id, 'username': response.username}
    
    """
    Define new User

    Need's next headers {'username': 'unique_username', 'password': 'any_password'}

    """
    def post(self):

        if request.headers:
            username = str(request.headers.get('username'))
            password = str(request.headers.get('password'))

            if not username or not password:
                return 'Bad headers. Check username/password', 403
            
            
            password_hash = generate_password_hash(password)
            new_user = User(username=username, password_hash=password_hash)
            db.session.add(new_user)
            db.session.commit()
            return {'status':'OK'}, 200
        
        return {'status':'Bad', 'message': 'Not found any headers'}, 403
        

    def patch(self):
        pass

    def delete(self):
        pass
        
        
