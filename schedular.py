#!/usr/bin/python

import urllib2;
import httplib;
import threading;
import sys, traceback;

import HTMLParser;

import urldb;

class LinkHTMLParser(HTMLParser.HTMLParser):
  def __init__(self, start_page):
    HTMLParser.HTMLParser.__init__(self);
    self.links_ = [];
    self.start_page_ = start_page;

  def format_url(self, url):
    if url.find('http') != 0:
      if url.find('/') == 0:
        # start with /, find the root directory
        request = urllib2.Request(self.start_page_);
        url = 'http://' + request.get_host() + url;
        return url;
      else:
        # relative url path to start_page
        refer = self.start_page_.rfind('/');
        refer = self.start_page_[0:refer];
        print refer;
        url = refer + "/" + url;
        return url;
    else: 
      return url;

  def handle_starttag(self, tag, attrs):
    if tag == "a":
      for attr in attrs:
        if attr[0] == 'href':
          url = attr[1];   
          url = self.format_url(url);
          self.links_.insert(len(self.links_), url);

  def handle_endtag(self, tag):
    pass;

  def get_links(self):
    return self.links_;


class CrawlerTread(threading.Thread):
  
  def __init__(self, tid, schedular):
    threading.Thread.__init__(self);
    self.tid_ = tid;
    self.schedular_ = schedular;

  def run(self):
    print "Run crawler tread [%d]" % (self.tid_);
    
    while True:
      print "Run";
      if self.schedular_.should_stop_:
        print "Stop thread [%d]" % (self.tid_)
        break;
      #continue to get url and craw the content
      url = self.schedular_.urldb_get_next_url();
      if not url:
        break;
      
      try:
        print "Request... %s" % (url)
        http_request = urllib2.urlopen(url);      

        self.parser_ = LinkHTMLParser(url);
        
        data= http_request.read();
  
        self.parser_.feed(data)
        
        #store to database
        self.schedular_.database_put_page(url, data);

        print self.parser_.links_;
        self.schedular_.urldb_put_urls(self.parser_.links_);
        print "Finish %s" % (url)

      except:
        traceback.print_exc(file=sys.stdout)
        continue;
    

class Schedular:
  
  def __init__(self, tcnt=1, site = "http://www.python.org", database = None):
    self.nthread_ = tcnt;
    self.threads_ = [];
    self.urldb_ = urldb.URLDatabase(site);
    self.should_stop_ = False;
    self.database_ = database;

  def start(self):
    #spawn threads
    for i in range(self.nthread_):
      print "Start thread %d" % (i)
      thread = CrawlerTread(i, self);
      self.threads_.insert(1, thread);
      thread.start();

  def wait_for_finish(self):
    for i in range(len(self.threads_)):
      self.threads_[i].join();

  def stop(self):
    self.should_stop_ = True; 

  def should_stop(self):
    return self.should_stop_;

  # proxy methods for urldb
  def urldb_get_next_url(self):
    return self.urldb_.get_next_url();

  def urldb_put_urls(self, urls):
    self.urldb_.put_urls(urls);

  # proxy methods for database
  def database_put_page(self, url, content):
    if self.database_:
      self.database_.put_page(url, content);


if __name__ == "__main__":
  print "Start Crawling Schedular"


