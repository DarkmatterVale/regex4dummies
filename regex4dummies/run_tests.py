# Importing regex4dummies
from regex4dummies import regex4dummies
from regex4dummies import Toolkit
from tests import main_tests

# Running tests
tester = main_tests()
tester.run_tests( regex4dummies(), Toolkit() )
