from base_api import ApiRequests


class SingleUser(ApiRequests):
    def get_resp(self, user_id):
        return self.send_get(
            url=f"https://reqres.in/api/users/{user_id}"
        )