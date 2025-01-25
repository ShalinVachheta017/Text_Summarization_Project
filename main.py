from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from textSummarizer.logging import logger

STAGE_01_DATA_INGESTION = "stage_01_data_ingestion"
try:
    logger.info(f">>>>>>>>>>>Pipeline for {STAGE_01_DATA_INGESTION} started<<<<<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>>>>>>>Pipeline for {STAGE_01_DATA_INGESTION} completed<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e
