import requests


class TestCLIOptions:
    def test_cli_options(self, url, status_code):
        response = requests.get(url)
        assert response.status_code == status_code
