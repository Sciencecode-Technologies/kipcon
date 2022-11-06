import pytest
from ptive.pcore import Bety

@pytest.mark.test1
def test_crossf():
    bety = Bety()
    assert round(bety.cross(), 2) == 1.52
