from tweetpuller import nltweetpuller

def run_puller():
    _pull_tweets()
  
def _pull_tweets():
    tweets = nltweetpuller.pull()
    if len(tweets) > 0:
      print('Yeeted ' + str(len(tweets)) + ' tweets')