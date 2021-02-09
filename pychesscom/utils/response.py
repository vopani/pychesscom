class Response:
    def __init__(self, url, code, reason, content_type, timestamp, content):
        self.url = url
        self.code = code
        self.reason = reason
        self.content_type = content_type
        self.timestamp = timestamp
        self.content = content

    def to_dict(self) -> dict:
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
