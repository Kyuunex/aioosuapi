class AuthenticationError(Exception):
    """ Authentication Error. """
    def __init__(self, *args, **kwargs):
        pass


class HTTPException(Exception):
    """ Connection Error. """
    def __init__(self, *args, **kwargs):
        pass


class OtherOsuAPIError(Exception):
    """ Error. """
    def __init__(self, *args, **kwargs):
        pass


class NotReady(Exception):
    """ Not ready. """
    def __init__(self, *args, **kwargs):
        pass
