from typing import List, Union


class Response:
    """
    Class for handling Chess.com API responses.

    Args:
        url(str): URL of Chess.com API request
        code(int): Code of API response
        reason(str): Reason of API response
        content_type(str): Content type of API response
        timestamp(bytes): Timestamp of API request
        content(_SpecialForm[List[dict], dict]): Content of API response
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

        Returns:
            dict: Dictionary format
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
