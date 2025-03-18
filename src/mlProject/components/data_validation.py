import os
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
        
    def validate_columns(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            dataset_columns = set(data.columns)
            schema_columns = set(self.config.all_schema.keys())

            if dataset_columns == schema_columns:
                validation_status = True
            else:
                validation_status = False
            
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation Status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e
