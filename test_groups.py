import pytest

@pytest.mark.signup
@pytest.mark.regression
def test_signup_valid():
    assert True

@pytest.mark.login
def test_login_valid():
    assert True
