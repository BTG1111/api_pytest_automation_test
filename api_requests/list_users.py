from base_api import ApiRequests


class ListUsers(ApiRequests):
    def get_resp(self):
        return self.send_get(
            url="https://reqres.in/api/users?page=2"
        )
