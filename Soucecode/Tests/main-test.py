import pytest
from main import conntectToDatabase, compareDatatypes

connection = conntectToDatabase()
cursor = connection.cursor()

def testCompareDatatypes(cursor):
    assert compareDatatypes(cursor, )