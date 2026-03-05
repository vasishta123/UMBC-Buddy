"""Configuration settings for UMBC Buddy chatbot"""

import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # API Configuration
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    ENV: str = os.getenv("ENV", "development")
    
    # API Keys
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    DIALOGFLOW_PROJECT_ID: str = os.getenv("DIALOGFLOW_PROJECT_ID", "")
    DIALOGFLOW_SESSION_ID: str = os.getenv("DIALOGFLOW_SESSION_ID", "")
    SLACK_BOT_TOKEN: Optional[str] = os.getenv("SLACK_BOT_TOKEN")
    SLACK_SIGNING_SECRET: Optional[str] = os.getenv("SLACK_SIGNING_SECRET")
    
    # File Paths
    PDF_PATH: str = os.getenv("PDF_PATH", "data/UMBC_International.pdf")
    DATA_DIR: str = os.getenv("DATA_DIR", "data/")
    MODELS_DIR: str = os.getenv("MODELS_DIR", "models/")
    
    # Model Configuration
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "gpt-4-turbo")
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", 0.7))
    MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", 500))
    
    # Vector Database
    VECTOR_DB_TYPE: str = os.getenv("VECTOR_DB_TYPE", "faiss")
    VECTOR_DB_PATH: str = os.getenv("VECTOR_DB_PATH", "data/vectordb")
    CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", 500))
    CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", 50))
    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE: str = os.getenv("LOG_FILE", "logs/umbc_buddy.log")
    
    # Response Configuration
    CONFIDENCE_THRESHOLD: float = float(os.getenv("CONFIDENCE_THRESHOLD", 0.5))
    MAX_SOURCES: int = int(os.getenv("MAX_SOURCES", 3))
    DEFAULT_RESPONSE: str = "I don't have information about that. Please contact UMBC International Student Services at isss@umbc.edu or call 410-455-2511."
    
    # Cache Configuration
    ENABLE_CACHING: bool = os.getenv("ENABLE_CACHING", "True").lower() == "true"
    CACHE_TTL: int = int(os.getenv("CACHE_TTL", 3600))  # 1 hour
    
    # Rate Limiting
    ENABLE_RATE_LIMITING: bool = os.getenv("ENABLE_RATE_LIMITING", "True").lower() == "true"
    RATE_LIMIT_REQUESTS: int = int(os.getenv("RATE_LIMIT_REQUESTS", 100))
    RATE_LIMIT_WINDOW: int = int(os.getenv("RATE_LIMIT_WINDOW", 3600))
    
    # CORS
    CORS_ORIGINS: list = ["*"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Create settings instance
settings = Settings()
