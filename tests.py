import unittest
from unittest import mock

from dicks_api import DicksApi


class TestDicksApi(unittest.TestCase):

    def setUp(self):
        self.api = DicksApi()
        self.url = self.api.url

    @mock.patch('urllib.request.urlopen')
    def test_get_single_random_dick(self, urlopen):
        urlopen().read.side_effect = [b'{"dicks":["8======D"]}']
        dicks = self.api.get()
        url = self.url + str(1)

        self.assertIsInstance(dicks, list)
        self.assertEqual(len(dicks), 1)
        self.assertRegex(dicks[0], '^8=+D$')
        self.assertEqual(urlopen.call_args, mock.call(url))

    @mock.patch('urllib.request.urlopen')
    def test_get_5_random_dicks(self, urlopen):
        urlopen().read.side_effect = [
            b'{"dicks":["8==D", "8======D", "8==D", "8=====D", "8==D"]}']
        dicks = self.api.get(amount=5)
        url = self.url + str(5)

        self.assertIsInstance(dicks, list)
        self.assertEqual(len(dicks), 5)
        for i in range(5):
            with self.subTest(dick=i+1):
                self.assertRegex(dicks[i], '^8=+D$')
        self.assertEqual(urlopen.call_args, mock.call(url))

    @mock.patch('urllib.request.urlopen')
    def test_get_minus_1_random_dick(self, urlopen):
        urlopen().read.side_effect = [b'{"dicks":[]}']
        dicks = self.api.get(amount=-1)
        url = self.url + str(-1)

        self.assertIsInstance(dicks, list)
        self.assertEqual(len(dicks), 0)
        self.assertEqual(urlopen.call_args, mock.call(url))

    @mock.patch('urllib.request.urlopen')
    def test_get_single_asian_dick(self, urlopen):
        urlopen().read.side_effect = [b'{"dicks":["8==D"]}']
        dicks = self.api.get(size="asian")
        url = self.url + str(1) + "?size=asian"

        self.assertIsInstance(dicks, list)
        self.assertEqual(len(dicks), 1)
        self.assertRegex(dicks[0], '^8=+D$')
        self.assertEqual(urlopen.call_args, mock.call(url))

    @mock.patch('urllib.request.urlopen')
    def test_get_13_black_dicks(self, urlopen):
        urlopen().read.side_effect = [
            b'{"dicks":["8============D","8===========D","8===========D",' +
            b'"8============D","8===========D","8===========D",' +
            b'"8===========D","8============D","8===========D",' +
            b'"8===========D","8============D","8===========D",' +
            b'"8===========D"]}']
        dicks = self.api.get(size='black', amount=13)
        url = self.url + str(13) + "?size=black"

        self.assertIsInstance(dicks, list)
        self.assertEqual(len(dicks), 13)
        for i in range(13):
            with self.subTest(dick=i+1):
                self.assertRegex(dicks[i], '^8=+D$')
        self.assertEqual(urlopen.call_args, mock.call(url))

    def test_get_3_and_a_half_random_dicks(self):
        self.assertRaises(TypeError, self.api.get, amount=3.5)

    def test_get_single_alaskan_dick(self):
        self.assertRaises(ValueError, self.api.get, size='alaskan')

if __name__ == "__main__":
    unittest.main()
