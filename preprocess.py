#!/usr/bin/env python
"""
This script will do pre-processinf of the data.

The goal of the pre-processing has a similar goal as pre-processing
of embedding data in the RAG pattern.

Except in this case, we don't use a pre-trained model, but we will
upload the data to an AI search service from Azure.
"""
from pathlib import Path

from lib.preprocess import Preprocessor


def get_valid_parh(goal: str) -> str:
    """
    Get a valid path for the 'goal'.
    """
    valid_path = None
    while not valid_path:
        path = input(f"Please provide a path to the {goal}: ")
        # Check that the user didn't just press enter
        if not path:
            print("Invalid path.")
            continue
        if not Path(path).exists():
            print("Path does not exist.")
            continue
        valid_path = path
    return valid_path


if __name__ == "__main__":

    input_path = get_valid_parh("input data")
    output_path = get_valid_parh("output data (This directory will be emptied!)")

    preprocessor = Preprocessor(input_path, output_path, respondend_id=1)
    preprocessor.preprocess()

    print("Pre-processing done.")
