import os

from SourceXlsReader import GetWorkbookAsDictionary

if __name__ == "__main__":
    srcData = GetWorkbookAsDictionary(
        os.path.join('test', 'customer_copy.xlsx'))

    print(srcData)
