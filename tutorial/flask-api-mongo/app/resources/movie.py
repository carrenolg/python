from flask import Response, request
from database.models import Movie, User
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from mongoengine.errors import FieldDoesNotExist, \
    NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

from resources.errors import SchemaValidationError, MovieAlreadyExistsError, \
    InternalServerError, UpdatingMovieError, DeletingMovieError, MovieNotExistsError


class MoviesApi(Resource):
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    @jwt_required()
    def post(self):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)
            movie = Movie(**body, added_by=user)
            movie.save()
            user.update(push__movies=movie)
            user.save()
            id = movie.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise MovieAlreadyExistsError
        except Exception as e:
            raise InternalServerError


class MovieApi(Resource):
    @jwt_required()
    def put(self, id):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)
            # movie = Movie(**body, added_by=user)
            movie = Movie.objects.get(id=id, added_by=user)
            # Movie.objects.get(id=id).update(**body)
            movie.update(**body)
            return 'Updated', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingMovieError
        except Exception:
            raise InternalServerError

    @jwt_required()
    def delete(self, id):
        try:
            user_id = get_jwt_identity()
            # Movie.objects.get(id=id).delete()
            user = User.objects.get(id=user_id)
            movie = Movie.objects.get(id=id, added_by=user)
            movie.delete()
            return 'Deleted', 200
        except DoesNotExist:
            raise DeletingMovieError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            movies = Movie.objects.get(id=id).to_json()
            return Response(movies, mimetype="application/json", status=200)
        except DoesNotExist:
            raise MovieNotExistsError
        except Exception:
            raise InternalServerError


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
