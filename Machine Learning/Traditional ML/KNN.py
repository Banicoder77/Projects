import numpy as np
class KNN:
    def __init__(self,trainin,trainout):
        self.trainin=trainin
        self.trainout=trainout
    def euclid(self,l1):
        a=self.trainin-l1
        b=a**2
        return np.sqrt(np.sum(b,axis=1))
    def manhattan(self,l1):
        a=self.trainin-l1
        b=np.abs(a)
        return np.sum(b,axis=1)
    def highpow(self,l1,pow):
        a=np.abs(self.trainin-l1)
        b=a**pow
        return np.sum(b,axis=1)**(1/pow)
    def predict(self,knn,weightfn,l1,pow=None):
        if weightfn==self.euclid or weightfn==self.manhattan:
            dist = weightfn(l1)
        else:
            dist=weightfn(l1,pow)
        idx = np.argsort(dist)
        feight=1/((np.sort(dist))[:knn]+1e-9)
        total=np.sum(feight)
        feight/=total

        neighbors = idx[:knn]
        trainout=self.trainout[neighbors]
        return np.sum(trainout*feight)
    def vote(self,knn,weightfn,l1,pow=None):
        if weightfn==self.euclid or weightfn==self.manhattan:
            dist = weightfn(l1)
        else:
            dist=weightfn(l1,pow)
        idx = np.argsort(dist)
        neighbors = idx[:knn]
        trainout=self.trainout[neighbors]
        vals, counts = np.unique(trainout, return_counts=True)
        return vals[np.argmax(counts)]
trainin = np.array([
    [750,   1,  5],
    [800,   1, 10],
    [900,   2,  7],
    [1000,  2,  5],
    [1100,  2, 15],
    [1200,  3, 10],
    [1300,  3, 20],
    [1400,  3, 12],
    [1500,  4, 18],
    [1600,  4, 25]
], dtype=float)


trainout = np.array([
    35.0,
    38.0,
    45.0,
    50.0,
    52.0,
    60.0,
    62.0,
    65.0,
    70.0,
    75.0
])


k1=KNN(trainin,trainout)

test_point = np.array([1150, 2, 12])  # new house

print(k1.predict(3,k1.euclid,test_point))