# -*- coding: utf-8 -*-
import logging
from os.path import exists
from pathlib import Path

import click
import pandas as pd
from dotenv import find_dotenv, load_dotenv

from notebooks.utility_functions import text_processing


@click.command()
@click.argument("input_filepath", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path())
def main(input_filepath, output_filepath):
    """Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info("making final data set from raw data")
    file_check = checkForFile(
        input_filepath=input_filepath, output_filepath=output_filepath
    )
    if not file_check[0]:
        raise FileNotFoundError("File does not exists at input path")

    data_ = pd.read_csv(input_filepath)

    if "article" not in data_.columns.values:
        raise KeyError("Key not found. Please check the data and try again.")
    data_["article"] = data_["article"].apply(text_processing)
    data_.to_csv(output_filepath)
    file_check = checkForFile(
        input_filepath=input_filepath, output_filepath=output_filepath
    )

    if not file_check[1]:
        raise FileNotFoundError(
            "Something has gone wrong. File does not exist at output destination"
        )


def checkForFile(input_filepath: str, output_filepath: str):

    return [exists(input_filepath), exists(output_filepath)]


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
