# -*- coding: utf-8 -*-

import unittest
from ..utils.Helper_validate import Validate, RegType


class ValidateHelperTestCase(unittest.TestCase):
    def test_validate_check_APP(self):
        self.assertTrue(Validate.check("app", reg_type=RegType.APP))
        self.assertFalse(Validate.check("abpp", reg_type=RegType.APP))
