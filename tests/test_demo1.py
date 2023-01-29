import pytest

@pytest.fixture()
def setup():
    print(" ### once before every test method ### ")

def test_method_11(setup):
    print("test_demo1 >>> test_method_11")

def test_method_12(setup):
    print("test_demo1 >>> test_method_12")

def test_method_13(setup):
    print("test_demo1 >>> test_method_13")

def test_method_14(setup):
    print("test_demo1 >>> test_method_14")

def test_method_15(setup):
    print("test_demo1 >>> test_method_15")