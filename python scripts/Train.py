import math

class Train:
    def __init__(self):
        self.state = []
        self.data = []

    def build(self, initstate):
        self.state = initstate

    def train(self, data):
        if len(self.state)!=len(data):
            print("Warning, possible mismatch of data length: State=", len(self.state), " Data=", len(data))

        error = []
        for i in range(len(data)):
             err = self.state[i] - data[i]
             error.append(err)

        for j in range(len(self.state)):
            if error[j] < 0:
                if (self.state[j] - math.sqrt(abs(error[j]))) <= 0:
                    self.state[j] = 0
                else:
                    self.state[j] = self.state[j] - math.sqrt(abs(error[j]))
            elif error[j] > 0:
                self.state[j] = self.state[j] + math.sqrt(abs(error[j]))
            else:
                next

    def reportstate(self):
        return(self.state)
