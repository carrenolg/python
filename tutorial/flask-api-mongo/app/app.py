from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from database.db import initialize_db
from resources.routes import initialize_routes


app = Flask(__name__)
api_rest = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# connect(host="mongodb://my_user:my_password@hostname:port/my_db?authSource=admin")
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://root:1q2w3e4r@localhost:27017/movie-bag?authSource=admin'
}
app.config.from_envvar('ENV_FILE_LOCATION')

initialize_db(app)
initialize_routes(api_rest)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
