import uuid

class User:

    def __init__(self, username):
        self.object_id = uuid.uuid1()
        self.name = username
