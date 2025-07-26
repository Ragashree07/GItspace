import pytest
def test_greet1():
    print("Hi Nana")

@pytest.mark.scope
def test_greet2():
    print("Hi sona")

@pytest.mark.skip
def test_inexecute():
    print("Do not execute this case")

@pytest.mark.xfail
def test_noresult():
    print("This is xfailed for a reason")
