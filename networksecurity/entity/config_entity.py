from datetime import datetime
import os
from networksecurity.constants import training_pipeline

print( training_pipeline.PIPELINE_NAME)
print( training_pipeline.ARTIFACT_DIR)

class TrainingPipelineConfig:
    """
    Configuration for the overall ML training pipeline.
    Responsible for defining the artifact directory structure and timestamping.
    """
    def __init__(self, timestamp=datetime.now()):
        
         # Convert timestamp into a clean string format
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")

        # Name of the pipeline (defined in constants)
        self.pipeline_name = training_pipeline.PIPELINE_NAME 

        # Root folder name for pipeline artifacts
        self.artifact_name = training_pipeline.ARTIFACT_DIR 

        # Full path where artifacts will be stored for this run
        #(Bug FIXED: using artifact_name instead of self.ARTIFACT_DIR)
        self.artifact_dir = os.path.join(self.artifact_name, timestamp)

        # Store timestamp string for later use (e.g., versioning)
        self.timestamp: str = timestamp  
        


class DataIngestionConfig:
    """
    Configuration object for the data ingestion step.
    Defines where data will be stored, file names, and ingestion parameters.
    """
    def __init__(self, training_pipeline_config):
        # Root directory inside the pipeline artifact folder for ingestion artifacts
        self.data_ingestion_dir = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME
        )

         # Location where the raw dataset (feature store) will be saved
        self.feature_store_file_path = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,
            training_pipeline.FILE_NAME
        )

        # Path for the generated train dataset after splitting
        self.train_file_path = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR,
            training_pipeline.TRAIN_FILE_NAME
        )

        # Path for the generated test dataset after splitting
        self.test_file_path = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR,
            training_pipeline.TEST_FILE_NAME
        )

        # Ratio used to split data into train/test
        self.train_test_split_ratio = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO

        # Database and collection names (for pulling raw data)
        self.collection_name = training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name = training_pipeline.DATA_INGESTION_DATABASE_NAME
        
