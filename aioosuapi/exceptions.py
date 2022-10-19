class AuthenticationError(Exception):
    """ Authentication Error. """
    def __init__(self, *args, **kwargs):
        pass


class ConnectionError(Exception):
    """ Connection Error. """
    def __init__(self, *args, **kwargs):
        pass


class OtherOsuAPIError(Exception):
    """ Error. """
    def __init__(self, *args, **kwargs):
        pass
