#!/bin/bash

import unittest;
import sys;

sys.path.append("../");

import dbmongo;

class TestDatabaseMongoFunctions(unittest.TestCase):
  
  def setUp(self):
    self.database_ = dbmongo.DatabaseMongo("127.0.0.1", 27017, "unittest", "pages");

  def test_put_page(self):
    self.database_.put_page("http://www.python.org",
                    "abcdefghijkl");

  def test_get_page_from_url(self):
    content = self.database_.get_page_from_url("http://www.python.org");
    self.assertEqual("abcdefghijkl", content);


if __name__ == "__main__":
  unittest.main();
