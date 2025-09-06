# src/pipeline/train_pipeline.py
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.utils import save_object
from src.exception import CustomException

def train_model():
    try:
        print("Starting training pipeline...")
        
        data = pd.DataFrame({
            'gender': ['male', 'female', 'male', 'female', 'male'],
            'race_ethnicity': ['group A', 'group B', 'group C', 'group D', 'group E'],
            'parental_level_of_education': ['high school', 'bachelor', 'master', 'high school', 'bachelor'],
            'lunch': ['standard', 'free/reduced', 'standard', 'free/reduced', 'standard'],
            'test_preparation_course': ['none', 'completed', 'none', 'completed', 'none'],
            'reading_score': [72, 90, 85, 60, 78],
            'writing_score': [74, 88, 82, 58, 76],
            'math_score': [70, 92, 80, 55, 75]  
        })
        
        
        X = data.drop('math_score', axis=1)  
        y = data['math_score']
        
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        
        categorical_features = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
        numerical_features = ['reading_score', 'writing_score']
        

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numerical_features),
                ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
            ])
        
        
        print("Training model...")
        model = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', LinearRegression())
        ])
        
        model.fit(X_train, y_train)
        
        
        save_object('artifacts/model.pkl', model)
        
        print("Training completed successfully!")
        print("Model saved as: artifacts/model.pkl")
        
        
        test_score = model.score(X_test, y_test)
        print(f"Model test score: {test_score:.4f}")
        
    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    train_model()