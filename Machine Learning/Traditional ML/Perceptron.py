import numpy as np
x = np.array([
    [10, 20, 30, 40, 50],
    [15, 25, 35, 45, 60],
    [12, 28, 33, 49, 57],
    [22, 18, 31, 42, 55],
    [35, 45, 55, 65, 75],
    [40, 10, 20, 30, 90],

    [95, 135, 155, 165, 10],
    [70, 55, 25, 35, 45],
    [65, 75, -85, -95, 10],
    [95, 90, 85, 60, 10],
    [40, 60, 80, 20, 25],
    [55, 45, 35, 25, 15],
    [23, -67, 89, 12, 22],
    [66, -77, 88, 99, 11],
    [15, 25, 45, 75, 10],
    [32, 48, 64, 80, 96],
    [100, 90, 80, 70, 60],
    [55, 44, 33, 22, 11],
    [88, 99, 11, 22, 33],
    [111, 222, 123, 45, 67],
    [5, 10, 15, 20, 25],
    [7, 14, 21, 28, 35]
])

o = np.array([
    [-300, 150, -20, 10, 5],
    [-250, 120, -30, 5, 12],
    [-350, 200, -10, 15, 9],
    [-400, 175, -25, 20, 3],
    [-500, 220, -35, 2, 8],
    [-275, 160, -40, 7, 4],
    [-320, 180, -15, 9, 6],
    [-450, 210, -50, 4, 2],
    [-600, 300, -60, 1, 1],
    [-700, 350, -70, 3, 3],
    [-800, 380, -80, 2, 2],
    [-900, 420, -90, 5, 1],
    [-1000, 450, -100, 6, 4],
    [-650, -330, -65, 8, 7],
    [-550, 280, -55, 3, 9]
])

class model:
    def __init__(self,w=None,verbose=False):
        self.w=w
        self.verbose=verbose
    def perceptron_train(self,x,o):
        misc=-1
        x=np.concatenate((x,np.ones(x.shape[0]).reshape(-1,1)),axis=1)
        o=np.concatenate((o,np.ones(o.shape[0]).reshape(-1,1)),axis=1)

        le=x[0].shape[0]
        w=np.ones(le)
        while True:
            if self.verbose:
                print(w)
            misc = 0
            for z in x:
                if np.dot(w, z) <= 0:
                    w += z
                    misc += 1
            for z in o:
                if np.dot(w, z) >= 0:
                    w -= z
                    misc += 1
            if misc == 0:
                break            
        self.w=w
            


    def perceptron_predict(self,l):
        l=np.array(l)
        l=np.atleast_2d(l)
        l=np.concatenate((np.array(l),np.ones(np.array(l).shape[0]).reshape(-1,1)),axis=1)
        l1=np.dot(l,self.w)
        l2=[]
        for x in l1:
            if x>0:
                l2.append('x')
            else:
                l2.append('o')
        return l2
m1=model()
m1.verbose=True
m1.perceptron_train(x,o)
print(m1.w)
print(m1.perceptron_predict([[1,2,5,4,6]]))