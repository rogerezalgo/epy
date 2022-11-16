from enum import Enum


class HttpStatus(Enum):
    BAD_REQUEST: int = 400
    INTERNAL_SERVER_ERROR: int = 500
