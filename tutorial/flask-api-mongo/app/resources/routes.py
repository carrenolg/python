from resources.movie import MoviesApi, MovieApi


def initialize_routes(api):
    # api.add_resource(MoviesApi, '/movies')
    # api.add_resource(MovieApi, '/movies/<id>')
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(MovieApi, '/api/movie/<id>')