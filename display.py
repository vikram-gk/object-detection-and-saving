import pickle
import matplotlib.pyplot as plt
file = open('data.pkl', 'rb')
for i in range(100):
    image = pickle.load(file)
    plt.imshow(image)
    plt.show()
file.close()
