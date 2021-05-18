from flask import Response, request
from database.models import Movie, User
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity


class MoviesApi(Resource):
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    @jwt_required()
    def post(self):
        body = request.get_json()
        user_id = get_jwt_identity()
        user = User.objects.get(id=user_id)
        movie = Movie(**body, added_by=user)
        movie.save()
        user.update(push__movies=movie)
        user.save()
        id = movie.id
        return {'id': str(id)}, 200


class MovieApi(Resource):
    @jwt_required()
    def put(self, id):
        user_id = get_jwt_identity()
        movie = Movie.objects.get(id=id, added_by=user_id)
        body = request.get_json()
        movie.update(**body)
        return 'Updated', 200

    @jwt_required()
    def delete(self, id):
        user_id = get_jwt_identity()
        #Movie.objects.get(id=id).delete()
        movie = Movie.objects.get(id=id, added_by=user_id)
        movie.delete()
        return 'Deleted', 200

    def get(self, id):
        movies = Movie.objects.get(id=id).to_json()
        return Response(movies, mimetype="application/json", status=200)


"""
@movies.route('/')
def hello():
    return {'hello': 'world'}


@movies.route('/movies')
def get_movies():
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)


@movies.route('/movies', methods=['POST'])
def add_movie():
    body = request.get_json()
    movie = Movie(**body).save()
    id = movie.id
    return {'id': str(id)}, 200


@movies.route('/movies/<id>', methods=['PUT'])
def update_movie(id):
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    return '', 200


@movies.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    Movie.objects.get(id=id).delete()
    return '', 200
"""
