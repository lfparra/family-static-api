from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Family:

    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [{
            "id": 1,
            "first_name": "John",
            "last_name": "Jackson",
            "age": 30,
            "lucky_numbers": [7, 12, 15]
        },
            {
                "id": 2,
                "first_name": "Diego",
                "last_name": "Jackson",
                "age": 25,
                "lucky_numbers": [13, 46, 79]
        },
            {
                "id": 3,
                "first_name": "Luis",
                "last_name": "Jackson",
                "age": 35,
                "lucky_numbers": [54, 101, 1]
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        ## you have to implement this method
        ## append the member to the list of _members
        pass

    def delete_member(self, id):
        ## you have to implement this method
        ## loop the list and delete the member with the given id
        pass

    def update_member(self, id, member):
        ## you have to implement this method
        ## loop the list and replace the memeber with the given id
        pass

    def get_member(self, id):
        ## you have to implement this method
        ## loop all the members and return the one with the given id
        pass

    def get_all_members(self, id):
        return self._members