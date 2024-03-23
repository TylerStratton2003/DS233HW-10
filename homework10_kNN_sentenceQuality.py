# name 1: Tyler Stratton
# name 2: Daniel Ma
# name 3:
import math

from sklearn.neighbors import NearestNeighbors
import numpy as np
from textblob import TextBlob

import numpy
from sklearn.neighbors import KNeighborsClassifier

class kNNsentenceQuality():
    def __init__(self):
        # do some initialization, optional
        self.data = []
        self.quality = []
        self.y = 0
        self.x = 0
        pass
    
    def trainkNN(self, trainingData):
        # traing a kNN model on the training dataset, your group should find a training dataset with three different qualities
        with open(trainingData, 'r') as file:
            for line in file[1:]:
                # read the data into an array
                self.data.append([item for item in line.split()]) # Add a row of training scores to the back of data

                # add a quality evaluation to the quality list
                self.quality.append(self.evalQuality(self.data[-1])) # Take the last element of data and get the evaluation

            # Prepare a numpy array to give to knn
            # Fill the y values
            self.y = numpy.array(self.quality)
            # Fill the x values
            self.x = numpy.array(self.data)
            
            # train the knn model
            kNNmodel = KNeighborsClassifier(n_neighbors=5, weights='uniform', metric='euclidean')
            kNNmodel.fit(self.x, self.y)
            
            # return the model
            return kNNmodel
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

model = obj.trainkNN(trainingData="trainWord.txt")
s = "DATA 233 is a wonderful class!"

print("The final quality for your input using kNN is " + str(obj.Quality_kNN(s, model)))
