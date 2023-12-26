class JSONDecodeException(Exception):
    def __init__(self, msg=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.msg = msg


class JSONSchemaException(Exception):
    def __init__(self, msg=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.msg = msg
