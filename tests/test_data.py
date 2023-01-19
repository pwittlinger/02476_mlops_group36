import os

import pandas as pd
import pytest

from tests import _PATH_DATA


@pytest.mark.skipif(not os.path.exists(_PATH_DATA), reason="Data files not found")
def test_data():
    # load the trianing data
    raw_ = "/raw/"
    assert os.path.exists(_PATH_DATA + raw_ + "train.csv")
    train_data = pd.read_csv(_PATH_DATA + raw_ + "train.csv")

    assert train_data.shape[1] == 3
    assert train_data.columns.values == ["id", "article", "highlights"]
