import os
import cv2


path = "C:/Users/dell/Downloads/PRO-C105-Project-Images-main (1)/PRO-C105-Project-Images-main"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height,width,layers = frame.shape 
size = (width,height)
print(size)

out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'),0.8, size)
# for loop
for i in range(0,count):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print("done")
