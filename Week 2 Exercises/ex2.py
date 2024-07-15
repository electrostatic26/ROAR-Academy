from matplotlib import image
from matplotlib import pyplot
import os

# Read an image file
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna.bmp'
data = image.imread(filename)

file2 = path + '/' + "china.png"
data2 = image.imread(file2)

# Display image information
print('Image type is: ', type(data))
print('Image shape is: ', data.shape)
print('Image type is: ', type(data2))
print('Image shape is: ', data2.shape)

# Add some color boundaries to modify an image array
plot_data = data.copy()

plot_data2 = data2.copy()


#322 length, 402 width



for width in range(402):
    for height in range(322):
        plot_data[height][512-402+width] = [
            int(255*plot_data2[height][width][0]),
            int(255*plot_data2[height][width][1]),
            int(255*plot_data2[height][width][2])
            ]
        
        #plot_data[511-height][width] = [22]

# Write the modified images
image.imsave(path+'/'+'lenna-mod.jpg', plot_data)
image.imsave(path+'/'+'chinaflag.jpg', plot_data)


# use pyplot to plot the image
pyplot.imshow(plot_data)
pyplot.show()

#pyplot.imshow(plot_data2)
#pyplot.show()