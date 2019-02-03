
class ErrorInvalidInput(Exception):
    def __init__(self, message):
        super().__init__(message)


class BVGError(Exception):
    MESSAGE = 'Unknown Error Occurred'

    def __init__(self, message=MESSAGE):
        super().__init__(message)
