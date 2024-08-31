from PIL import Image


im = Image.open("../Images/Railway_station.jpg")
im1=im.getdata()
new_a=[]

for item in im1:
	if item[0] > 100 and item[1] > 100 and item[2] > 100 and item[0] < 230 and item[1] < 230 and item[2] < 230:
		new_a.append((0,100,200))
	else:
		new_a.append(item)
im.putdata(new_a)
im.save(f"Railway_Station_edited2.jpg")
