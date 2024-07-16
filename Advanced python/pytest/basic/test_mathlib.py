import mathlib
import pytest
import sys

@pytest.mark.windows
def test_windows_1():
    assert True

@pytest.mark.windows
def test_windows_2():
    assert True

@pytest.mark.mac
def test_mac_1():
    assert True

@pytest.mark.mac
def test_mac_2():
    assert True

# @pytest.mark.skipif(sys.version_info<(3,5),reason="meri marzi")
# def test_calc_total():
#     total=mathlib.calc_total(5,4)
#     assert total==9

# @pytest.mark.skip(reason="meri marzi")
# def test_calc_multiply():
#     total=mathlib.calc_multiply(5,4)
#     assert total==20