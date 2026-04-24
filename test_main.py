from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_products():
    response = client.get('/products/products/all')
    assert response.content != None
    assert response.status_code == 200

def test_auth_success():
    response = client.post('/token',data = {"username":"zek","password":"zek"})
    access_token = response.json().get("access_token")

    assert access_token != None

def test_auth_error():
    response = client.post('/token',data = {"username":"","password":""})
    access_token = response.json().get("access_token")
    message = response.json().get("detail")[0].get("msg")

    assert access_token == None
    assert message == "Field required"

def test_post_article():
    response = client.post('/token',data = {"username":"zek","password":"zek"})
    access_token = response.json().get("access_token")
    assert access_token

    mock_body = {
        "title":"Test Article",
        "content":"Test Content",
        "published":True,
        "creator_id":2
    }
    response = client.post('/articles/', json=mock_body,headers={"Authorization":"bearer " + access_token})

    print(response.json())

    assert response.status_code == 201
    assert response.json().get("title") == mock_body["title"]
    assert response.json().get("content") == mock_body["content"]
    assert response.json().get("published") == mock_body["published"]
    assert response.json().get("user")["id"] == mock_body["creator_id"]