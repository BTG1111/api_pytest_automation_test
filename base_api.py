import json
from urllib import parse
import urllib3
import requests

from config import logger

urllib3.disable_warnings()


class ApiRequests(object):
    def __basic__logger(self, req_type, url, params, headers, data, resp):
        logger.debug(f"request type = {req_type}")
        logger.debug(f"request url = {url}")
        if params:
            logger.debug(f"request params = {params}")
        if headers:
            logger.debug(f"request headers = {headers}")
        if data:
            logger.debug(f"request data = {data}")
        logger.debug(f"response status code = {resp.status_code}")
        logger.debug(f"response body = {resp.text}")

    def __trans_body_format(self, headers, body):
        if body is None:  # 如果沒有request body， 就直接回body
            return body

        try:
            content_type = headers["Content-Type"]  # 如果request headers裡面有Content-Type這個key
        except KeyError:  # 如果request headers裡面沒有Content-Type這個key
            return body
        if content_type == "application/json":
            data = json.dumps(body)
        elif content_type == "application/x-www-form-urlencoded":
            data = parse.urlencode(body)
        else:
            data = body

        return data

    def get_session_cookie(self, url, params=None, headers=None, body=None):
        data = self.__trans_body_format(headers, body)
        session = requests.Session()
        resp = session.post(url=url, params=params, headers=headers, data=data)
        self.__basic__logger("POST", url, params, headers, data, resp)
        cookies_dict = session.cookies.get_dict()
        logger.debug(f"cookies = {cookies_dict}")
        return cookies_dict

    def send_post(self, url, params=None, headers=None, body=None):
        data = self.__trans_body_format(headers, body)
        resp = requests.post(url=url, params=params, headers=headers, data=data, verify=False)
        self.__basic__logger("POST", url, params, headers, data, resp)
        return resp

    def send_get(self, url, params=None, headers=None, body=None):
        data = self.__trans_body_format(headers, body)
        resp = requests.get(url=url, params=params, headers=headers, data=data, verify=False)
        self.__basic__logger("GET", url, params, headers, data, resp)
        return resp

    def send_put(self, url, params=None, headers=None, body=None):
        data = self.__trans_body_format(headers, body)
        resp = requests.put(url=url, params=params, headers=headers, data=data, verify=False)
        self.__basic__logger("PUT", url, params, headers, data, resp)
        return resp

    def send_patch(self, url, params=None, headers=None, body=None):
        data = self.__trans_body_format(headers, body)
        resp = requests.patch(url=url, params=params, headers=headers, data=data, verify=False)
        self.__basic__logger("PATCH", url, params, headers, data, resp)
        return resp

    def send_delete(self, url, params=None, headers=None, body=None):
        data = self.__trans_body_format(headers, body)
        resp = requests.delete(url=url, params=params, headers=headers, data=data, verify=False)
        self.__basic__logger("DELETE", url, params, headers, data, resp)
        return resp
