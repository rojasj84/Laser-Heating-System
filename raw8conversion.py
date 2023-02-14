import struct
import matplotlib.pyplot as plt
import numpy as np

#function that takes a file in RAW8 format from 
def convertraw8(filename):
    # Creating empty arrays to store data
    array_size = 90
    wavelength = np.empty(array_size)
    counts = np.empty(array_size)
    c3 = np.empty(array_size)
    c4 = np.empty(array_size)
    
    with open(filename, "rb") as f:
        size = 4
        count = 1778

        # Early part of the file without spectrum information
        for j in range(1,83):
            byte_arr = f.read(size)
            # print(struct.unpack('f', byte_arr))

        # Obtain the wavenlength values
        for j in range(0,array_size):
            byte_arr = f.read(size)
            x = struct.unpack('f', byte_arr)
            wavelength[j] = x[0]
            # print(wavelength[j])

        # Obtain the count values    
        for j in range(0,array_size):
            byte_arr = f.read(size)
            x = struct.unpack('f', byte_arr)
            counts[j] = int(x[0])
            # print(int(x[0]))

        for j in range(0,array_size):
            byte_arr = f.read(size)
            x = struct.unpack('f', byte_arr)
            c3[j] = int(x[0])
            # print(x[0])  
                 
        for j in range(0,array_size):
            byte_arr = f.read(size)
            x = struct.unpack('f', byte_arr)
            c4[j] = int(x[0])
            # print(x[0])      
            
    f.close()

    return(wavelength,counts)

if __name__ == "__main__":  
    #testing conversion
    x,y = convertraw8("test.RAW8")

    # print(x)
    # print(y)

    plt.scatter(x,y)
    plt.show()