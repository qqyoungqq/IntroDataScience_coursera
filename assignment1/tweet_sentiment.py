import sys
import json

#def hw():
#    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}
    
    for line in sent_file:
    	term, score = line.split("\t")
    	scores[term] = int(score)

    for line in tweet_file:
        senti_score = 0.0
        tweetObj = json.loads(line)
        if 'lang' in tweetObj.keys() and tweetObj["lang"]=="en" :
            if 'text' in tweetObj.keys():
                message=tweetObj["text"]
                encoded_message = message.encode('utf-8').split()
                senti_score = cal_entiscore(scores,encoded_message)

        print senti_score

def cal_entiscore(scores,message):
    senti_score = 0.0
    for word in message:
        if word in scores:
            senti_score = senti_score + scores[word]
    return senti_score

if __name__ == '__main__':
    main()