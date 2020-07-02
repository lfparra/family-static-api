from flask_sqlalchemy import SQLAlchemy
from random import randint
db = SQLAlchemy()

class Family:

    def __init__(self, last_name):
        
        self.last_name = last_name
        # example list of members
        self._members = [{
            "id": 1,
            "first_name": "John",
            "last_name": "Jackson",
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        },
            {
                "id": 2,
                "first_name": "Jane",
                "last_name": "Jackson",
                "age": 35,
                "lucky_numbers": [10, 14, 3]
        },
            {
                "id": 3,
                "first_name": "Jimmy",
                "last_name": "Jackson",
                "age": 5,
                "lucky_numbers": [1]
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        ## you have to implement this method
        ## append the member to the list of _members
        self._members.append(member)

    def delete_member(self, member_id):
        ## you have to implement this method
        ## loop the list and delete the member with the given id
        member = self.get_member(member_id)
        self._members.remove(member)
        return True

    def update_member(self, member_id, update):
        ## you have to implement this method
        ## loop the list and replace the memeber with the given id
        up_member = self.get_member(member_id)
        up_member = up_member.update(update)
        return up_member

    def get_member(self, member_id):
        ## you have to implement this method
        ## loop all the members and return the one with the given id
        member = list(filter(lambda member: member["id"] == member_id, self._members))
        return member[0] if len(member) > 0 else None
       
    def get_all_members(self):
        return self._members