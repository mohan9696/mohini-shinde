import pytest
@pytest.mark.parametrize('username','password','msg','user_data'):
def test_valid (username,password,msg):
    assert 'valid'==msg
