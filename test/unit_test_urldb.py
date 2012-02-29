#!/usr/bin/python

import unittest;
import sys;

sys.path.append("../");

import urldb;


class TestURLDatabaseFunctions(unittest.TestCase):
  
  def setUp(self):
    self.urldb = urldb.URLDatabase("http://www.sina.com.cn");

  def test_get_next_url(self):
    url = self.urldb.get_next_url();
    self.assertEqual(url, "http://www.sina.com.cn");
  
  def test_finish_url(self):
    self.urldb.finish_url("http://www.a.cn/visited.html");
    self.assertEqual(self.urldb.get_url_status(
                        "http://www.a.cn/visited.html"),  
                     urldb.URLDatabase.URL_VISITED);

  def test_put_url(self):
    self.urldb.put_url("http://www.a.cn/queue.html");
    self.assertEqual(self.urldb.get_url_status(
                        "http://www.a.cn/queue.html"),
                      urldb.URLDatabase.URL_QUEUE);


if __name__ == "__main__":
  unittest.main();

