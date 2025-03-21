from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline



STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"Starting {STAGE_NAME}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f"Starting {STAGE_NAME}")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"{STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"Starting {STAGE_NAME}")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"{STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f"Starting {STAGE_NAME}")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f"{STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e

