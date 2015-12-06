# Importing regex4dummies
from regex4dummies import regex4dummies
from toolkit import Toolkit
from tests import MainTests

# Running tests
tester = MainTests()
tester.run_tests(regex4dummies(), Toolkit())
