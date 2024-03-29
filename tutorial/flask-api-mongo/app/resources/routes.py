from resources.movie import MoviesApi, MovieApi
from resources.auth import SignupApi, LoginApi
from resources.reset_password import ForgotPassword, ResetPassword


def initialize_routes(api):
    # api.add_resource(MoviesApi, '/movies')
    # api.add_resource(MovieApi, '/movies/<id>')
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(MovieApi, '/api/movie/<id>')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    api.add_resource(ForgotPassword, '/api/auth/forgot')
    api.add_resource(ResetPassword, '/api/auth/reset')
