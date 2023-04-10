import os,sys
from StoreSales.constant import *
from StoreSales.logger import logging
from StoreSales.exception import CustomException
from StoreSales.entity.config_entity import DataIngestionConfig
from StoreSales.utils.utils import read_yaml_file
from StoreSales.entity.artifact_entity import DataIngestionArtifact


class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info("{'<<'}*30 Data Ingestion log started {'>>'}*30")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise CustomException(e,sys) from e
        
    def 