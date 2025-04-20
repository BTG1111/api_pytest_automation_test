import pytest

from api_requests.single_user import SingleUser

test_data = [
    ("1"),
    ("2"),
    ("3")
]


@pytest.mark.parametrize("user_id", test_data)
def test_overall(user_id):
    resp = SingleUser().get_resp(
        user_id
    )
    SingleUserTest.validate_status_code(resp)
    SingleUserTest.validate_schema(resp)
    SingleUserTest.validate_positive(resp)


class SingleUserTest:
    @staticmethod
    def validate_status_code(resp):
        assert resp.status_code == 200

    @staticmethod
    def validate_schema(resp):
        data = resp.json()["data"]
        assert type(data["id"]) is int
        assert type(data["email"]) is str
        assert type(data["first_name"]) is str
        assert type(data["last_name"]) is str
        assert type(data["avatar"]) is str

        support = resp.json()["support"]
        assert type(support["url"]) is str
        assert type(support["text"]) is str

    @staticmethod
    def validate_positive(resp):
        response = resp.json()
        assert "data" in response
        assert "id" in response["data"]
        assert "email" in response["data"]
        assert "first_name" in response["data"]
        assert "last_name" in response["data"]
        assert "avatar" in response["data"]

        assert "support" in response
        assert "url" in response["support"]
        assert "text" in response["support"]
