from PIL import Image

im = Image.open("../Images/Railway_station.jpg")
im1=im.getdata()

#list all the tuple RGB color value in an array "pixelsData"
pixelsData=list(im1)

# create a new file and write pixels value in it to analyse, file size is big
f=open("./pixelData.txt","w")
f.write(f"{pixelsData}")
f.close()
