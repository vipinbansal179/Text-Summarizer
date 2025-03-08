import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(filepath: Path) -> ConfigBox:
    """
    Read a yaml file from the given filepath.

    Args:
    filepath (Path): The path to the yaml file.

    Raises:
    ValueError: If the file is empty.
    e: empty file

    Returns:
    ConfigBox: A ConfigBox object.
    """

    try:
        with open(filepath, "r") as f:
            content = yaml.safe_load(f)
            logger.info(f"yaml file :{filepath} read successfully")
            return ConfigBox(content)
    except BoxValueError:
       raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbos=True):
   """
   Create list of directories
   
   Args:
    path_to_directories (list): list of directories to be created
    ignore_logs (bool,optional): ignore if multiple dirs is to be created. Defaults to True.
    verbos (bool,optional): print logs. Defaults to True.
   """
   for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbos:
            logger.info(f"Created directory: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of the file in the given path.

    Args:
    path (Path): The path to the file.

    Returns:
    str: The size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"