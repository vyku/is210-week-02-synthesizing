#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Lesson 02 task 0333."""


# Import Python libs
import unittest


# Import user libs
import task_03


class Task03TestCase(unittest.TestCase):
    """Task 03 tests"""

    def test_charlie(self):
        """Tests that CHARLIE has a value of 'Brown'"""
        self.assertEquals(task_03.CHARLIE, 'Brown')

    def test_violet(self):
        """Tests that VIOLET has a value of 'Gray'"""
        self.assertEquals(task_03.VIOLET, 'Gray')

    def test_patricia(self):
        """Tests that PATRICIA has a value of 'Reichardt'"""
        self.assertEquals(task_03.PATRICIA, 'Reichardt')

    def test_linus(self):
        """Tests that LINUS has a value of 'van Pelt'"""
        self.assertEquals(task_03.LINUS, 'van Pelt')


if __name__ == '__main__':
    unittest.main()
