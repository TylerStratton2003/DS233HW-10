# name 1: Tyler Stratton
# name 2: Daniel Ma
# name 3:
import math

from sklearn.neighbors import NearestNeighbors
import numpy as np
from textblob import TextBlob


class kNNsentenceQuality():
    def __init__(self):
        # do some initialization, optional
        self.data = []
        self.quality = []
        pass
    
    def trainkNN(self, trainingData, kNNmodel):
        # traing a kNN model on the training dataset, your group should find a training dataset with three different qualities
        with open("trainWord.txt", 'r') as file:
            for line in file[1:]:
                # read the data into an array
                self.data.append([item for item in line.split()])

                # Prepare a numpy array to give to knn
                
        pass
    
    def evalQuality(self, line:list):
        # Given a list of scores
        # return a quality rating
        if line[0] < 0.4:
            return -1 # Low Quality
        elif line[0] < 0.7:
            return 0 # Medium Quality
        else:
            return 1 # High Quality

    def Quality_kNN(self, sentence, kNNmodel):
        # please implement this function to classify the sentence into three different classes: high, low, and medium quality. Using the kNNmodel trained by kNN
        # Input: sentence
        # output: -1 means low quality, 0 means medium quality, 1 means high quality
        # notes: You may reuse your previous homework, and calculate the features for each input sentence, and then use kNN to classify the input sentence
        obj = sentenceQuality()
        sen = obj.calculateScores(sentence)
        predicted_Y = kNNmodel.predict(sen[1])

        return predicted_Y
        pass

class sentenceQuality():
    def __init__(self):
        # do some initialization, optional
        pass

    def calculateScores(self, tweet):
        # please implement this function
        # input: any tweet text
        # output: a list of scores for the tweet, it must include: score for length, score for Polarity, score for Subjectivity, and at least one score of the following:
        # https://en.wikipedia.org/wiki/Automated_readability_index
        # https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
        # https://en.wikipedia.org/wiki/Gunning_fog_index
        # https://en.wikipedia.org/wiki/SMOG
        # https://en.wikipedia.org/wiki/Fry_readability_formula
        # https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index
        # You should implement at least one score

        tweet = TextBlob(tweet)

        # Length
        # come back to this
        wordLength = len(tweet.words)
        length = 1.0
        if wordLength > 11 and wordLength < 16:
            length = 1.0
        else:
            if wordLength > 15:
                num = 2
                inc = 5
                length = length - 0.25
                while (wordLength >= 15 + (inc * num)):
                    num = num + 1
                    length = length - 0.25
                    if (length < 0.0):
                        length = 0.0
            elif wordLength < 12:
                num = 2
                inc = 4
                length = length - 0.25
                while (wordLength <= 12 - (inc * num)):
                    num = num + 1
                    length = length - 0.25
                    if (length < 0.0):
                        length = 0.0

        # Polarity
        polarity = tweet.sentiment.polarity

        # Subjectivity
        subjectivity = tweet.sentiment.subjectivity

        # Readability - we are using the Automated Readability Index
        minScore = 1
        maxDiff = 13
        numWords = len(tweet.words) - 1
        numChars = sum(1 for char in tweet if char.isalnum())
        numSentences = len(tweet.sentences)
        readability = math.ceil((4.71 * (numChars / numWords)) + (0.5 * (numWords / numSentences)) - 21.43)
        readability = round((readability - minScore) / maxDiff, 2) # calculated from a method to normalize scores


        return [length, polarity, subjectivity, readability]
        pass



# this is for testing only
obj = kNNsentenceQuality()
s = "DATA 233 is a wonderful class!"

print("The final quality for your input using kNN is " + str(obj.Quality_kNN(s)))
