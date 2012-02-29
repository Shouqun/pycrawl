#!/usr/bin/python

import urllib2;
import httplib;
import threading;

class URLDatabase:
  
  URL_NEW = 0;
  URL_VISITED = 1;
  URL_QUEUE = 2;

  def __init__(self, site):
    self.queue_urldb_ = [site];
    self.visited_urldb_ = [];
    self.lock_ = threading.Lock();

  def configure(self, key, value):
    pass;

  def get_next_url(self):
    self.lock_.acquire();
    
    url = None;
    if len(self.queue_urldb_) > 0:
      url = self.queue_urldb_.pop();   
    self.lock_.release();
    return url;

  def finish_url(self, url):
    self.lock_.acquire();
    # insert the url to used
    self.visited_urldb_.insert(len(self.visited_urldb_),url);
    self.lock_.release();

  def put_url(self, url):
    self.lock_.acquire();
    # insert url to the queue
    if url not in self.visited_urldb_:
      self.queue_urldb_.insert(len(self.queue_urldb_), url);
    self.lock_.release();

  def put_urls(self, urls):
    self.lock_.acquire();
    # insert urls to the queue
    for url in urls:
      if url not in self.visited_urldb_:
        self.queue_urldb_.insert(len(self.visited_urldb_), url) 
    self.lock_.release();

  def get_url_status(self, url):
    self.lock_.acquire();
    if url in self.queue_urldb_:
      self.lock_.release();
      return URLDatabase.URL_QUEUE;
    elif url in self.visited_urldb_:
      self.lock_.release();
      return URLDatabase.URL_VISITED;
    else:
      self.lock_.release();
      return URLDatabase.URL_NEW;

if __name__ == "__main__":
  print "Start Crawling..."

  urldb = URLDatabase("http://www.sina.com.cn");
  urldb.configure("threads", 1);
  urldb.start();

  urldb.get_next_url();


