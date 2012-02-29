#!/usr/bin/env python

import unittest;
import sys;

sys.path.append("../");

import schedular;

class TestSchedularFunctions(unittest.TestCase):

  def setUp(self):
    self.schedular_ = schedular.Schedular(1);

  def test_start(self):
    self.schedular_.start()

  def test_stop(self):
    self.schedular_.stop();


if __name__ == "__main__":
  unittest.main();
