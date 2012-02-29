#!/usr/bin/python

import schedular;
import signal;
import sys;

import dbmongo;

g_schedular = None;

def sig_int_handler(signum, frame):
  print "SIGINT caught... to exit"
  if g_schedular:
    g_schedular.stop();
  sys.exit();

if __name__ == "__main__":
  print "Start Task..."

  signal.signal(signal.SIGINT, sig_int_handler);

  database = dbmongo.DatabaseMongo("127.0.0.1", 27017, "pagedb", "pages");
  
  g_schedular = schedular.Schedular(2, "http://www.python.org", database);
  
  g_schedular.start();
  
  g_schedular.wait_for_finish();
