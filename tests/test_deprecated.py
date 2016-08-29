# -*- coding: utf-8 -*-

import warnings
from unittest import TestCase

from tests import deprecated_function, function


class DeprecatedTest(TestCase):

    def test_should_warn_deprecated_function(self):
        with warnings.catch_warnings(record=True) as warns:
            warnings.simplefilter("always")
            deprecated_function()
            self.assertEqual(len(warns), 1)
            warn = warns[0]
            self.assertTrue(issubclass(warn.category, DeprecationWarning))
            self.assertTrue("deprecated" in str(warn.message))

    def test_should_not_warn_non_deprecated_function(self):
        with warnings.catch_warnings(record=True) as warns:
            warnings.simplefilter("always")
            function()
            self.assertEqual(len(warns), 0)
