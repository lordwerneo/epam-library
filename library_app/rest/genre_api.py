"""
This module contains REST operations to work with genres.
"""
# pylint: disable=cyclic-import
from flask_restful import Resource, reqparse
from library_app.service import genre_service

genre_args = reqparse.RequestParser()
genre_args.add_argument("name", type=str, help="Name required", required=True)
genre_args.add_argument("description", type=str, help="Description required",
                        required=True)


class GenresList(Resource):
    """
    Class for GenresList API Resource available at /api/genres
    """
    @staticmethod
    def get():
        """
        Called when GET request is received
        :return: json of all genres if success or error message
        """
        genres = genre_service.get_all_genres()
        if genres == 'Error':
            return {'Message': 'No genres in DB'}, 200
        return {'genres': genres}

    @staticmethod
    def post():
        """
        Called when POST request is received
        :return: json with information and link of created genre if success,
        or error message
        """
        args = genre_args.parse_args()
        if args['name'] == '' or args['description'] == '':
            return{'Message': 'Wrong data input'}, 400
        genres = genre_service.post_genre(name=args['name'],
                                          description=args['description'])
        if genres == 'Error':
            return {'Message': 'Genre already exists',
                    'link': f'/api/genre/{args["name"]}'}, 405
        return {'genre': args, 'link': f'/api/genre/{args["name"]}'}, 201


class GenresSolo(Resource):
    """
    Class for GenresSolo API Resource available at /api/genre/<string:name>
    """
    @staticmethod
    def get(name):
        """
        Called when GET request is received
        :param name: name of the genre
        :return: json with information about genre if success, or error message
        if no such genre in table
        """
        genre = genre_service.get_genre_by_name(name)
        if genre == 'Error':
            return {'Message': 'No such genre'}, 404
        return {'genre': genre}, 200

    # pylint: disable=inconsistent-return-statements
    @staticmethod
    def put(name):
        """
        Called when put request is received
        :param name: name of the genre
        :return: Json with information about created genre if no such genre in
        table and success, json with information about updated genre in table
        if json in table and success, or error message
        """
        args = genre_args.parse_args()
        if args['name'] == '' or args['description'] == '':
            return {'Message': 'Wrong data input'}, 400
        genre = genre_service.put_genre(current_name=name,
                                        name=args['name'],
                                        description=args['description'])
        if genre == 'Created':
            return {'genre': args, 'link': f'/api/genre/{args["name"]}'}, 201
        if genre == 'Updated':
            return {'genre': args, 'link': f'/api/genre/{args["name"]}'}, 200
        if genre == 'Unknown':
            return {'Message': f'No such genre {name} to update, or '
                               f'{args["name"]} is busy'}, 404
        if genre == 'Busy':
            return {'Message': f'Can\'t update genre {name},'
                               f'genre {args["name"]} already exist'}, 400

    @staticmethod
    def delete(name):
        """
        Called when DELETE request is received
        :param name: name of the genre
        :return: Json with success message if success, or error message if no
        genre in table
        """
        genre = genre_service.delete_genre(name)
        if genre == 'Error':
            return {'Message': 'No such genre'}, 404
        return {'Message': f'Genre {name} deleted.'}, 200
