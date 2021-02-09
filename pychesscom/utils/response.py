from typing import List, Union


class Response:
    """
    Class for handling Chess.com API responses.

    :param url: URL of Chess.com API request
    :type url: str
    :param code: Code of API response
    :type code: int
    :param reason: Reason of API response
    :type reason: str
    :param content_type: Content type of API response
    :type content_type: str
    :param timestamp: Timestamp of API request
    :type timestamp: bytes
    :param content: Content of API response
    :type content: _SpecialForm[List[dict], dict]
    """
    def __init__(self, url: str, code: int, reason: str, content_type: str, timestamp: bytes,
                 content: Union[List[dict], dict]):
        self.url = url
        self.code = code
        self.reason = reason
        self.content_type = content_type
        self.timestamp = timestamp
        self.content = content

    def to_dict(self) -> dict:
        """
        Convert to dictionary.

        :return: Dictionary format
        :rtype: dict
        """
        _dict: dict = {}
        for key, val in vars(self).items():
            if hasattr(val, 'to_dict'):
                _dict[key] = val.to_dict()
            else:
                _dict[key] = val
        return _dict

    def __repr__(self):
        return str(self.to_dict())

    def __str__(self):
        return str(self.to_dict())
