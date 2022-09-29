import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
 
def word_feats(words):
    return dict([(word, True) for word in words])

def getSentimentAnalysis(sentence):
    positive_vocab = [ 'love','awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)' ]
    negative_vocab = [ 'bad', 'terrible','useless', 'hate', 'violation' ]
    neutral_vocab = [ 'movie','the','sound','was','is','actors','did','know','words','not' ]
         
    positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
    negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
    neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]
         
    train_set = negative_features + positive_features + neutral_features
         
    classifier = NaiveBayesClassifier.train(train_set) 
         
    # Predict
    neg = 0
    pos = 0
    
    sentence = sentence.lower()
    words = sentence.split(' ')
    for word in words:
        classResult = classifier.classify( word_feats(word))
        if classResult == 'neg':
            neg = neg + 1
        if classResult == 'pos':
            pos = pos + 1

    res = []
    res.append(str(float(pos)/len(words)))
    res.append(str(float(neg)/len(words)))
    return res
    

# if __name__ == '__main__':
    # res = getSentimentAnalysis("Redmi 6A has lag problems. This phone is hanging and lags while using YouTube and browser.Redmi 5A is far better than Redmi 6A. I am regretting on my decision for buying this phone. Not satisfied.")
    # print('Positive: ' + res[0])
    # print('Negative: ' + res[1])
