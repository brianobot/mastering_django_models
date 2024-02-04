from unittest import mock, TestCase


class SomeClass:
    def _hidden_method(self):
        return 0

    def public_method(self, x):
        return self._hidden_method() + x


class TestClass(TestCase):
    @mock.patch.object(SomeClass, "_hidden_method")
    def test_public_method(self, mock_method):
        print("mock method: ", mock_method)
