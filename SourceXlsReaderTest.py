import os
import unittest

from openpyxl.utils.exceptions import InvalidFileException

import SourceXlsReader


class SourceXlsReaderTest(unittest.TestCase):
    def test_ShouldReadAllRows(self):
        workbookDict = SourceXlsReader.GetWorkbookAsDictionary(
            os.path.join('test', 'customer_copy.xlsx'))

        expected = _GenerateExpectedData()
        self.assertCountEqual(workbookDict, expected)

    def test_ShoudRaiseIfWorkbookNotFound(self):
        with self.assertRaises(InvalidFileException):
            SourceXlsReader.GetWorkbookAsDictionary('')


def _GenerateExpectedData():
    rows = []
    for i in range(1, 3):
        d = {}
        for j in range(1, 10):
            d['Column {0}'.format(str(j))] = 'data {0}'.format(str(i))
        rows.append(d)
    return rows


if __name__ == "__main__":
    unittest.main()
