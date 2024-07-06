from behave import *
from payLoad import *
from utilities.configurations import *
from utilities.resources import *
import requests


@given('the book details which needs to be added to library')
def step_impl(context):
    context.url_addBook = getConfig()['API']['endpoint'] + APIResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payload = addBookPayLoad("vgjif", "12485")


@when(u'we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url_addBook, json=context.payload, headers=context.headers, )


@then(u'book is successfully added')
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    print(type(response_json))
    context.bookId = response_json['ID']
    print("Book id:", context.bookId)
    assert response_json["Msg"] == "successfully added"


@given('the book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url_addBook = getConfig()['API']['endpoint'] + APIResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payload = addBookPayLoad(isbn, aisle)


@then('status code of response should be {statuscode:d}')
def step_impl(context, statuscode):
    print(context.response.status_code)
    assert context.response.status_code == statuscode
