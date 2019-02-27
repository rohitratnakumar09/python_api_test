import unittest
import pytest
import requests
import json
import jsonpath

class Login_Test_API(unittest.TestCase):

    def setUp(self):
        # print("Running one time setUp")
        self.ApiUrl = "https://jsonplaceholder.typicode.com"

    def test_check_headers(self):
        url = self.ApiUrl+"/posts/1"
        response = requests.get(url)
        print(response.status_code)
        print(response.headers.get('Date'))
        print(response.headers.get('Server'))
        assert (response.status_code) == 200

    def test_json_data(self):
        url=self.ApiUrl+"/posts/1"
        json_data = requests.get(url).json()
        user_id=json_data['userId']
        title=json_data['title']
        print(user_id)
        print(title)
        assert user_id == 1


    def test_json_delete(self):
        url = self.ApiUrl + "/posts/1"
        response = requests.delete(url)
        print(response.status_code)
        assert (response.status_code) == 200

    def test_json_post(self):
        url = self.ApiUrl + "/posts"
        json_input={"title":"foo","body":"bar","userId":"1"}
        response=requests.post(url,json_input)
        print(response.content)
        print(response.status_code)
        assert response.status_code == 201

    def test_json_put(self):
        url = self.ApiUrl + "/posts/1"
        json_input = {"id": "1", "title": "Foo", "body": "bar","userId":"1"}
        response = requests.put(url, json_input)
        print(response.content)
        print(response.status_code)
        assert response.status_code == 200


    def test_json_patch(self):
        url = self.ApiUrl + "/posts/1"
        json_input = {"title": "fo00o"}
        response = requests.patch(url, json_input)
        print(response.content)
        print(response.status_code)
        # assert response.status_code == 201

    def tearDown(self):
          print("End of testing REST API")
