import pytest
from main1 import init_db, add_user, get_user, count_vowels

@pytest.fixture
def db_conn():
    conn = init_db()
    yield conn
    conn.close()

def test_add_or_get_user(db_conn):
    add_user(db_conn, 'Sasha', 30)
    user = get_user(db_conn, 'Sasha')
    assert user == (1, 'Sasha', 30)


def test_only_vowels():
    assert count_vowels('aeiouAEIOU') == 10

def test_no_vowels():
    assert count_vowels('bcdfghjklmnpqrstvwxyz') == 0

def test_mixed_string():
    assert count_vowels('Hello World') == 3
    assert count_vowels('PyThOn Is AwEsOmE') == 7
    assert count_vowels('12345') == 0
    assert count_vowels('') == 0

if __name__ == '__main__':
    pytest.main()
