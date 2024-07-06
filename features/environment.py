import requests
from behave import *
from payLoad import *
from utilities.configurations import *
from utilities.resources import *


def after_scenario(context, scenario):
    if "library" in scenario.tags:
        url_deleteBook = getConfig()['API']['endpoint'] + APIResources.deleteBook
        context.response_deleteBook = requests.post(url_deleteBook, json={

            "ID": context.bookId
        }, headers={"Content-Type": "application/json"}, )

        print(context.response_deleteBook.status_code)

        assert context.response_deleteBook.status_code == 200
        res_json = context.response_deleteBook.json()

        print(res_json["msg"])
        assert res_json["msg"] == "book is successfully deleted"
