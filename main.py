from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger


STAGE_NAME = "stage_01_data_ingestion"

try:
    logger.info(f"Pipeline started for stage: {STAGE_NAME}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"Pipeline ended for stage: {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e
