#import numpy as np
#print np.loadtxt('F:/NYU/Hackathon/output_file')
#dt = []
#print np.genfromtxt('F:/NYU/Hackathon/output_file', dtype=str)
#numpy.save('F:/NYU/Hackathon/outputTest', x)
#y = x.astype(np.float)
#print y

import numpy as np

data = np.genfromtxt('output_file-clean')
print data
np.save('numpy_array.npy',data)