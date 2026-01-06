import pandas as pd
from pathlib import Path
from src.core.logging import setup_logging
from src.core.utils import ensure_dir
from src.core.config import RAW_DATA_DIR

logger = setup_logging()

"""
TODO: consider the excel files that have multiple sheets.
We might need to handle them differently, 
perhaps by loading each sheet into a separate DataFrame.
"""

def load_csv(file_path: Path) -> pd.DataFrame:
    """ Load a CSV file into a DataFrame."""
    logger.info(f"Loading data from {file_path}")
    return pd.read_csv(file_path)

def save_raw_data(df: pd.DataFrame, filename: str) -> None:
    """Save raw data to the raw data directory."""
    ensure_dir(RAW_DATA_DIR)
    output_path = RAW_DATA_DIR / filename
    logger.info(f"Data shape: {df.shape}")
    df.to_csv(output_path, index=False)
    logger.info(f"Saved raw data to {output_path}")
