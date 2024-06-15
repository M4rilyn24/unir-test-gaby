import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add_success(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        result = response.read().decode("utf-8")
        self.assertEqual(result, "4", "El resultado esperado es incorrecto")

    def test_api_add_failure_invalid_input(self):
        url = f"{BASE_URL}/calc/add/a/2"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST,
            f"Se esperaba un error de solicitud incorrecta en la petición API a {url}"
        )

    def test_api_add_failure_missing_input(self):
        url = f"{BASE_URL}/calc/add/2"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            cm.exception.code, http.client.NOT_FOUND,
            f"Se esperaba un error de recurso no encontrado en la petición API a {url}"
        )


if __name__ == "__main__":
    unittest.main()
