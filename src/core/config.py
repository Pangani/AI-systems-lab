from pathlib import Path
import os

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parents[2]

# Environment
ENV = os.getenv("ENV", "development")

# Data directories
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Model artifacts
MODELS_DIR = BASE_DIR / "models"

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
