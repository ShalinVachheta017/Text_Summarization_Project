from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "stage_01_data_ingestion"
try:
    logger.info(f">>>>>>>>>>>Pipeline for {STAGE_NAME} started<<<<<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>>>>>>>Pipeline for {STAGE_NAME} completed<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "stage_02_data_validation"
try:
    logger.info(f">>>>>>>>>>>Pipeline for {STAGE_NAME} started<<<<<<<")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(f">>>>>>>>>>>Pipeline for {STAGE_NAME} completed<<<<<<<\n\nx=========x")
    
except Exception as e:
    logger.exception(e)
    raise e

