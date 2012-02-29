import pymongo


class DatabaseMongo:
  
  def __init__(self, host, port, database, table):
    self.connection_ = pymongo.Connection(host, port);
    self.database_ = self.connection_[database];
    self.table_ = self.database_[table];

  def put_page(self, link, content):
    item = {"url": link,
            "content": content};
    self.table_.insert(item);

  def get_page_from_url(self, link):
    query = {"url": link};
    item = self.table_.find_one(query);
    if not item:
      return None;
    return item["content"];

