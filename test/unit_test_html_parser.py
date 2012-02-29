#!/usr/bin/env python

import unittest;
import sys;

sys.path.append("../");

import schedular;


class TestLinkHTMLParser(unittest.TestCase):
  
  def setUp(self):
    self.html_parser_ = schedular.LinkHTMLParser("http://www.google.com/a/b.html?key=value");

  def test_format_absolute_url(self):
    self.assertEqual("http://www.google.com/b/c.html",
          self.html_parser_.format_url("/b/c.html"));

  def test_format_relative_url(self):
    self.assertEqual("http://www.google.com/a/c.html?key=value",
          self.html_parser_.format_url("c.html?key=value"));

if __name__ == "__main__":
  unittest.main();
