import os, sys
from src.logger import logging
from src.exception import CustomException
from src.entity.config_entity import DataIngestionConfig
from src.constants import *
from src.utils.utils import read_yaml_file

class Configuration:
    def __init__(self,config_file_path: str = CONFIG_FILE_PATH):
        try:
            self.config_info = read_yaml_file(file_path = config_file_path)
        except Exception as e: 
            raise CustomException(e, sys)
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            data_ingestion_config = self.config_info['data_ingestion_config']
            artifact_dir = self.config_info['artifacts_config']['artifact_dir']
            dataset_dir = data_ingestion_config['dataset_dir']

            ingested_data_dir = os.path.join(artifact_dir,dataset_dir,  data_ingestion_config['ingested_dir'])
            raw_data_dir = os.path.join(artifact_dir,dataset_dir,  data_ingestion_config['raw_data_dir'])


            response = DataIngestionConfig(
                dataset_download_url = data_ingestion_config['dataset_download_url'],
                raw_data_dir = raw_data_dir,
                ingested_dir = ingested_data_dir
            )

            return response

        except Exception as e: 
            raise CustomException(e, sys)
        
