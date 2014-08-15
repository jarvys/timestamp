import unittest
import time
import timestamp
from datetime import datetime

class TestTimestamp(unittest.TestCase):

	def testIt(self):
		_timestamp = time.time()
		self.assertEqual(timestamp(datetime.fromtimestamp(_timestamp)), int(_timestamp)*1000)


if __name__ == '__main__':
	unittest.main()
