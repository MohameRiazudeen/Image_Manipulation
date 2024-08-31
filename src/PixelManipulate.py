from PIL import Image

# create an instance of Image object
im = Image.open("../Images/Railway_station.jpg")

'''
get 3 bands RGB colors pixels data, return a list of RGB tuples :
[(134,56,67),...]
'''

im1=im.getdata()

#new array
new_a=[]

# Compare RGB value through each tuples
# and append new RGB values
for item in im1:
	if item[0] > 100 and item[1] > 100 and item[2] > 100 and item[0] < 230 and item[1] < 230 and item[2] < 230:
		new_a.append((0,100,200))
	else:
		new_a.append(item)

# put pixels data to image object
im.putdata(new_a)
im.save(f"Railway_Station_edited2.jpg")
