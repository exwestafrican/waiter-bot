import requests


class MobileWaiter:
    def __init__(self, *args, **kwargs):
        self.base_url = BASE_URL

    def create_restaurant(self, restaurant_name, school_id, owner_id, contact_person):
        payload = {
            "restaurantName": restaurant_name,
            "schoolId": school_id,
            "ownerId": owner_id,
            "contactPerson": contact_person,
        }
        response = requests.post(self.base_url + "/v1/restaurants", data=payload)
        if response.ok:
            json_response = response.json()
            if json_response.get("status") == "success":
                data = json_response.get("data")
                restaurant_data = data.get("restaurant")
                resturant_id = restaurant_data.get("id")
                return resturant_id
        return response.json()

    def create_food_item(self, name, category):
        payload = {"name": name, "category": category}
        response = requests.post(self.base_url + "/v1/item", data=payload)
        if response.ok:
            json_respone = response.json()
            if json_respone.get("status") == "success":
                return json_respone.get("data").get("id")
        else:
            # find the item
            pass

    def link_item_to_resturant(
        self,
        item_id,
        resturant_id,
        base_amount,
        amount_per_addition,
        available=1,
        packed=0,
        packed_amount=0,
    ):
        payload = {
            "itemId": item_id,
            "baseAmount": base_amount,
            "amountPerAddition": amount_per_addition,
            "available": available,
            "packed": packed,
            "packAmount": packed_amount,
        }
        response = requests.post(
            self.base_url + "/v1/restaurants/" + str(resturant_id), data=payload
        )
        if response.ok:
            return True
        return True

    def get_item(self, name, category):
        data = {"name": name, "category": category}
        response = requests.get(self.base_url + "/v1/item", params=data)
        if response.ok:
            json_respone = response.json()

            try:
                data = json_respone["data"]["response"][0]
                return data.get("id")
            except IndexError:
                return None

    def get_or_create_food_item(self, name, category):
        food_id = self.get_item(name=name, category=category)

        item_id = (
            food_id
            if food_id != None
            else self.create_food_item(name=name, category=category)
        )
        print("food_id", item_id)

        return item_id

    def all_resturants_in_school(self, school_id, **kwargs):
        data = {"schoolId": school_id}
        response = requests.get(self.base_url + "/v1/restaurants?", params=data)
        if response.ok:
            json_response = response.json()
            data = json_response["data"]["response"]
            return data

    def fetch_all_user(self):
        response = requests.get(self.base_url + "/v1/users")
        if response.ok:
            json_response = response.json()
            data = json_response["data"]["response"]
            return data


waiter_interface = MobileWaiter()