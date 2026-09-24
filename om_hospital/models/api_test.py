from odoo import models, fields
from zaphalo_api import WhatsappAPI


class APITest(models.Model):
    _name = "api.test"
    _description = "API Test"

    name = fields.Char(string="Name")

    def test_api(self):

        client = WhatsappAPI(
            base_url="https://jsonplaceholder.typicode.com",
            api_key="test",
        )

        # GET
        get_result = client.get("/posts/1")
        print("GET RESPONSE:", get_result)

        # POST
        post_data = {
            "title": "Hello from Odoo",
            "body": "This was sent using my Python library",
            "userId": 1,
        }

        post_result = client.post("/posts", post_data)
        print("POST RESPONSE:", post_result)

        # PUT
        put_data = {
            "id": 1,
            "title": "Updated from Odoo",
            "body": "This was updated using my Python library",
            "userId": 1,
        }

        put_result = client.put("/posts/1", put_data)
        print("PUT RESPONSE:", put_result)

        # DELETE
        delete_result = client.delete("/posts/1")
        print("DELETE RESPONSE:", delete_result)

        return True

        # client py in api folder
        # import requests


        # class WhatsappAPI:

        #     def __init__(self, base_url, api_key):
        #         self.base_url = base_url
        #         self.api_key = api_key

        #     def _headers(self):
        #         return {
        #             "Authorization": f"Bearer {self.api_key}",
        #             "Content-Type": "application/json",
        #         }

        #     def get(self, endpoint):
        #         url = f"{self.base_url}{endpoint}"

        #         response = requests.get(
        #             url,
        #             headers=self._headers(),
        #         )

        #         response.raise_for_status()

        #         return response.json()

        #     def post(self, endpoint, data):
        #         url = f"{self.base_url}{endpoint}"

        #         response = requests.post(
        #             url,
        #             json=data,
        #             headers=self._headers(),
        #         )

        #         response.raise_for_status()

        #         return response.json()

        #     def put(self, endpoint, data):
        #         url = f"{self.base_url}{endpoint}"

        #         response = requests.put(
        #             url,
        #             json=data,
        #             headers=self._headers(),
        #         )

        #         response.raise_for_status()

        #         return response.json()

        #     def delete(self, endpoint):
        #         url = f"{self.base_url}{endpoint}"

        #         response = requests.delete(
        #             url,
        #             headers=self._headers(),
        #         )

        #         response.raise_for_status()

        #         return response.json()