from tweetpuller import nltweetpuller

import mongo

class TweetPuller(object):
    def run_puller(self):
        self._pull_tweets()

    def _pull_tweets(self):
        self.client = mongo.MongoClient()
        tweets = nltweetpuller.pull()
        if len(tweets) > 0:
            print('Yeeted ' + str(len(tweets)) + ' tweets')
