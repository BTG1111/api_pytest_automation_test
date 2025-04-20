import pytest

from api_requests.list_users import ListUsers


@pytest.fixture(scope="module")
def resp():
    return ListUsers().get_resp(
    )


def test_status_code(resp):
    assert resp.status_code == 200


def test_schema(resp):
    response = resp.json()
    assert type(response["page"]) is int
    assert type(response["per_page"]) is int
    assert type(response["total"]) is int
    assert type(response["total_pages"]) is int
    assert type(response["data"]) is list

    data = response["data"]
    for single_data in data:
        assert type(single_data["id"]) is int
        assert type(single_data["email"]) is str
        assert type(single_data["first_name"]) is str
        assert type(single_data["last_name"]) is str
        assert type(single_data["avatar"]) is str

    assert type(response["support"]) is dict
    assert type(response["support"]["url"]) is str
    assert type(response["support"]["text"]) is str


def test_positive(resp):
    response = resp.json()
    assert "page" in response
    assert "per_page" in response
    assert "total" in response
    assert "total_pages" in response
    assert "data" in response
    assert "support" in response

    for item in response["data"]:
        assert "id" in item
        assert "email" in item
        assert "first_name" in item
        assert "last_name" in item
        assert "avatar" in item

    assert "url" in response["support"]
    assert "text" in response["support"]
