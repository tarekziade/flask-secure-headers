import unittest


class TestHeaders(unittest.TestCase):
    """ Test policy creation """
    def assertHeaderEquals(self, header1, header2):
        header1 = [h.strip() for h in header1.split(";")]
        header1.sort()
        header2 = [h.strip() for h in header2.split(";")]
        header2.sort()
        self.assertEquals(header1, header2)


