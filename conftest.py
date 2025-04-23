import sys
import os


def pytest_configure(config):
    root_path = os.path.abspath(os.path.dirname(__file__))
    api_requests_path = os.path.join(root_path, 'api_requests')
    if api_requests_path not in sys.path:
        sys.path.insert(0, api_requests_path)