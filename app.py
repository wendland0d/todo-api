from todo_api import app, api
from todo_api.views import app_route
from todo_api.api import UserResource, AdminUserResource

app.register_blueprint(app_route)

api.add_resource(UserResource, '/users', '/users/<int:user_id>', '/users/<string:username>')
api.add_resource(AdminUserResource, '/admin/users/', '/admin/users/<string:model_username>')

if __name__ == '__main__':
    app.run()