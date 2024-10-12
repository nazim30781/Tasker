from src.auth.utils import decode_token


class TasksService:
    @staticmethod
    def get_user_id(user_data, *args, **kwargs):
        access_token = dict(user_data)['credentials']
        user_data = decode_token(access_token)
        id = user_data['user']['id']

        return id