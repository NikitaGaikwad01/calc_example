
import os
import pandas as pd
import shutil

from pathlib import Path


def abs_path_to_csv(filepath):
    """Converts a relative path into an absolute path"""
    return (Path(filepath)).absolute()

class FileReader:

    @staticmethod
    def read_from_file(filename):
        dir_path = os.getcwd()
        file_path = os.path.join(dir_path,"/csv_input_file/", filename)
        df = pd.read_csv(file_path)
        return df

    """Class is built to read csv files"""
    @staticmethod
    def csv_to_df(csv_to_convert):
        """Converts a csv file into a dataframe"""
        pathway = abs_path_to_csv(csv_to_convert)
        return pd.read_csv(pathway)

    @staticmethod
    def search_csv(name_of_csv):
        """Searches for a particular csv in an input folder and returns location"""
        absolute_location = "calc/tests/csv_input_file/" + name_of_csv
        return absolute_location

    """Will turn a pandas dataframe into a csv log file"""
    @staticmethod
    def df_to_csv(df_to_convert: pd.DataFrame, file_name):
        """Converts a dataframe into a csv file"""
        df_to_convert.to_csv(file_name + ".csv", index=False)
        return True

    @staticmethod
    def set_directory():
        """Changes the directory to 'results' in order to commit the logs"""
        os.chdir('calc/tests/result_csv_file')
        return True

    """Contains methods to move files around"""
    # pylint: disable='too-few-public-methods
    @staticmethod
    def move_to_destination(current_csv_file,
                            destination='calc/tests/result_csv_file'):
        """Moves csv files from one folder to another"""
        shutil.move(current_csv_file, destination)

if __name__ == '__main__':
    FileReader.main()
# with open('csv_input/addition.csv', 'r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#
#         for line in csv_reader:
#             print(line)
#
#         print(line[1] + line[2])
