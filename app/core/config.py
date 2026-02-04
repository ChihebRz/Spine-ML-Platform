from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Spine ML Platform"
    MODEL_PATH: str = "ml/artifacts/model.pth"
    SCALER_PATH: str = "ml/artifacts/scaler.pkl"

settings = Settings()
