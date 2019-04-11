import pymongo

CREDS_PATH = "creds.txt"
MLAB_BASE_URL = "mongodb://{username}:{password}@ds131676.mlab.com:31676/nltweets"


class MongoClient(object):
    def _set_credentials(self, creds_path):
        with open(creds_path, "r") as f:
            contents = f.read()
            keys = contents.split("\n")
            self.db_username = keys[4]
            self.db_password = keys[5]
        self.url = MLAB_BASE_URL.format(username=db_username, password=db_password)
    
    def insert_many(self, key, data):
        self._set_credentials(CREDS_PATH)
        client = pymongo.MongoClient(MLAB_URL)
        db = client.get_default_database()
        db[key].insert_many(data)
        client.close()
