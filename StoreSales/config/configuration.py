import sys
from StoreSales.logger import logging
from StoreSales.exception import CustomException
from StoreSales.entity.config_entity import *
from StoreSales.utils.utils import read_yaml_file
from StoreSales.constant import *

class Configuration:
    def __init__(self,
                 config_file_path:str = CONFIG_FILE_PATH,
                 current_time_stamp:str = CURRENT_TIME_STAMP):
        try:
            self.config_info = read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp

        except Exception as e:
            raise CustomException(e,sys) from e
        
    
    def get_data_ingestion_config(self) ->DataIngestionConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir = os.path.join(
                artifact_dir,
                DATA_INGESTIONN_ARTIFACT_DIR,
                self.time_stamp
            )
            

        except Exception as e:
            raise CustomException(e,sys) from e