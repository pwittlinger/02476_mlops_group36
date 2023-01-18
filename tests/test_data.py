import os
import sys

import pytest

from tests import _PATH_DATA


@pytest.mark.skipif(not os.path.exists(_PATH_DATA), reason="Data files not found")
def test_data():
    assert True


# assert that each datapoint has shape [1,28,28] or [728] depending on how you choose to format
# assert that all labels are represented
