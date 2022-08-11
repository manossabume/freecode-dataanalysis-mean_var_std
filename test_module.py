import numpy as np

#Create calculate function
def calculate(lis):
    if len(lis) == 9:       
        """a = np.array(lis)
        b = a.reshape(3,3)"""
        
        b = np.array(lis).reshape(3,3)
        c = {
              'mean': [np.mean(b, axis=0).tolist(), np.mean(b,axis=1).tolist(), np.mean(b)],
              'variance': [np.var(b,axis=0).tolist(), np.var(b,axis=1).tolist(), np.var(b)],
              'standard deviation': [np.std(b,axis=0).tolist(), np.std(b,axis=1).tolist(), np.std(b)],
              'max': [np.max(b,axis=0).tolist(), np.max(b,axis=1).tolist(), np.max(b)],
              'min': [np.min(b,axis=0).tolist(), np.min(b,axis=1).tolist(), np.min(b)],
              'sum': [np.sum(b,axis=0).tolist(), np.sum(b,axis=1).tolist(), np.sum(b)]
            }
        return c
    else: 
        print("List must contain nine numbers.")

def main():
    print(calculate([1,2,3,4,5,6,7,8,9]))

if __name__ == "__main__":
    main()
