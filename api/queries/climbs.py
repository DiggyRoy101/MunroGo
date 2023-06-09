from queries.client import Queries
from models.climbs import ClimbParams, Climb
from typing import List
from bson import ObjectId


class ClimbsQueries(Queries):
    COLLECTION = "climbs"

    def get_all_by_account(self, account_id: str) -> List[Climb]:
        climbs = []
        climbs_cursor = self.collection.find({"account_id": account_id})
        for climb in climbs_cursor:
            climb["id"] = str(climb["_id"])
            climbs.append(Climb(**climb))
        return climbs

    def get_all_by_munro(self, munro_id: str) -> List[Climb]:
        climbs = []
        climbs_cursor = self.collection.find({"munro_id": munro_id})
        for climb in climbs_cursor:
            climb["id"] = str(climb["_id"])
            climbs.append(Climb(**climb))
        return climbs

    def create_one(
        self, account_id: str, munro_id: str, climb: ClimbParams
    ) -> Climb:

        climb_dict = climb.dict()
        climb_dict["account_id"] = account_id
        climb_dict["munro_id"] = munro_id
        self.collection.insert_one(climb_dict)
        climb_dict["id"] = str(climb_dict["_id"])
        return Climb(**climb_dict)

    def get_one(self, climb_id: str) -> Climb:
        climb = self.collection.find_one({"_id": ObjectId(climb_id)})
        climb["id"] = str(climb["_id"])
        return Climb(**climb)

    def delete_one(self, climb_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(climb_id)})
        return result.deleted_count == 1
