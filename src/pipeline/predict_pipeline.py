import sys
import pandas as pd
import os
from pathlib import Path
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
       
        self.project_root = Path(__file__).parent.parent.parent
        self.artifacts_dir = os.path.join(self.project_root, 'artifacts')
        
        os.makedirs(self.artifacts_dir, exist_ok=True)

        self.model_path = os.path.join(self.artifacts_dir, 'model.pkl')

    def check_artifacts_exist(self):
        """Check if required artifact files exist"""
        if not os.path.exists(self.model_path):
            error_msg = (
                f"Model file not found at {self.model_path}\n"
                "Please run the training pipeline first using:\n"
                "python src/pipeline/train_pipeline.py"
            )
            raise CustomException(error_msg, sys)

    def predict(self, features):
        try:
            
            self.check_artifacts_exist()
            
            print(f"Loading model from: {self.model_path}")
            
            
            model = load_object(self.model_path)
            
    
            preds = model.predict(features)
            return preds
            
        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self, gender: str,
                 race_ethnicity: str,
                 parental_level_of_education: str,
                 lunch: str,
                 test_preparation_course: str,
                 reading_score: int,
                 writing_score: int):
                
                self.gender = gender
                self.race_ethnicity = race_ethnicity
                self.parental_level_of_education = parental_level_of_education
                self.lunch = lunch
                self.test_preparation_course = test_preparation_course
                self.reading_score = reading_score
                self.writing_score = writing_score
    

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)