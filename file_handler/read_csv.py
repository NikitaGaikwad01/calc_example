"""CSV File Class"""

import pandas as pd

class CSVFileRead:
    """Defining CSV class for file handling"""

    # pylint: disable=too-few-public-methods

    @staticmethod
    def read_userdata(path):
        """Returns the data that we will be reading from CSV"""
        return pd.read_csv(path)
