from unittest import TestCase


class TestSMA(TestCase):
	def test_imports(self):
		from sma_sunnyboy import WebConnect, Key, Right

		obj = WebConnect("0.0.0.0", Right.USER, "")
		del obj

		key = Key.device_state
		del key
