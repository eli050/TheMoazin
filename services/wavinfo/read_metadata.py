from pathlib import Path
import os
import stat
from datetime import datetime


class ReadMetaData:
    def __init__(self, folder_path:str):
        self.folder_path = folder_path
    @staticmethod
    def _get_meta_data(file_path:str):
        file_path = Path(file_path)
        file_stat = file_path.stat()
        meta_data = dict()
        meta_data["file_path"] = file_path
        meta_data["file_size"] = file_stat.st_size
        meta_data["create_time"] = str(datetime.fromtimestamp(file_stat.st_ctime))
        meta_data["file_name"] = file_path.name
        meta_data["permissions_file"] = stat.filemode(file_stat.st_mode)
        meta_data["file_id"] = str(hash(f"{meta_data["file_path"]}{meta_data["create_time"]}"
                                    f"{meta_data["permissions_file"]}"))
        return meta_data
    def read_folder(self):
        list_of_metadata = list()
        for file_name in os.listdir(self.folder_path):
            file_path = self.folder_path+"\\"+file_name
            list_of_metadata.append(ReadMetaData._get_meta_data(file_path))
        return list_of_metadata







