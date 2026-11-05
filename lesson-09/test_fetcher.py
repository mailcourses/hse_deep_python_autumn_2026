import unittest
from unittest import mock

import fetcher


class TestFetcher(unittest.IsolatedAsyncioTestCase):
    async def test_fetch_url(self):
        with mock.patch("fetcher.aiohttp.ClientSession.get") as mget:
            text_mock = mock.AsyncMock(return_value="orig_text")
            resp_mock = mock.AsyncMock(text=text_mock)

            mget.return_value.__aenter__.return_value = resp_mock

            result = await fetcher.fetch_url("url1")

            self.assertEqual("orig_text", result)

            expected_calls = [
                mock.call("url1"),
                mock.call().__aenter__(),
                mock.call().__aenter__().text(),
                mock.call().__aexit__(None, None, None),
            ]
            self.assertEqual(expected_calls, mget.mock_calls)

            text_mock.assert_awaited()
            text_mock.assert_awaited_with()

    async def test_fetch_url_error(self):
        with mock.patch("fetcher.aiohttp.ClientSession.get") as mget:
            mget.return_value.__aenter__.side_effect = ValueError("wrong")

            with self.assertRaises(ValueError) as err:
                await fetcher.fetch_url("url1")

            expected_calls = [
                mock.call("url1"),
                mock.call().__aenter__(),
            ]
            self.assertEqual(expected_calls, mget.mock_calls)


if __name__ == "__main__":
    unittest.main()
