# name 1: Tyler Stratton
# name 2: Daniel Ma
# name 3:
import numpy

class kNNsentenceQuality():
    def __init__(self):
        # do some initialization, optional
        self.data = []
        self.quality = []
        self.y
        self.x
        pass
    
    def trainkNN(self, trainingData, kNNmodel):
        # traing a kNN model on the training dataset, your group should find a training dataset with three different qualities
        with open("trainWord.txt", 'r') as file:
            for line in file[1:]:
                # read the data into an array
                self.data.append([item for item in line.split()]) # Add a row of training scores to the back of data
                
                # add a quality evaluation to the quality list
                self.quality.append(self.evalQuality(self.data[-1])) # Take the last element of data and get the evaluation

            # Prepare a numpy array to give to knn
            self.y = numpy.array(self.quality)
                
                
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

        return 0
        pass


# this is for testing only
obj = kNNsentenceQuality()
s = "DATA 233 is a wonderful class!"

print("The final quality for your input using kNN is " + str(obj.Quality_kNN(s)))
