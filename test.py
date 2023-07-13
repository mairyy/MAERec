import pickle
import copy
import numpy as np
from scipy.sparse import csr_matrix, coo_matrix, dok_matrix
import scipy.sparse as sp

path = './datasets/clothings/seq'

def load_adj(filename):
      count = 0
      with open(filename, 'rb') as fs:
        print(pickle.load(fs))
        count += 1
        if count > 10: 
          fs.close()
          # ret = (pickle.load(fs) != 0).astype(np.float32)
      # if type(ret) != coo_matrix:
      #     ret = sp.coo_matrix(ret)
      # return ret
load_adj(path)
# print(a)