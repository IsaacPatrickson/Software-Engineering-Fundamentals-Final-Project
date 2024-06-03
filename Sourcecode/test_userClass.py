import pytest
import re
from userClass import *

def testValidateUserName():
    stringTest = "HelloWorld"
    stringTestWithSpace = "Hello World"
    stringTestWithSymbols = "Hello World!!$%^"
    assert validateUserName(re, stringTest) == True
    assert validateUserName(re, stringTestWithSpace) == True
    assert validateUserName(re, stringTestWithSymbols) == False