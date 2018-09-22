from PIL import Image
import os

image_size = (1280, 720)

for file_name in os.listdir("."):
    if file_name.endswith(".png") or file_name.endswith(".jpg"):
        Image.open(file_name).crop((0, 80, 2560, 1520)).resize(image_size).save("new/" + file_name)

input("Press Enter to continue.")
for i in range(2, 5):
    folder_name = str(i)
    file_names = list(filter(lambda x: x.endswith(".png") or x.endswith(".jpg"), os.listdir(folder_name)))
    for j in range(0, len(file_names), i):
        images = list(map(Image.open, map(lambda x: folder_name + '/' + x, file_names[j:j+i])))
        new_image = Image.new('RGB', (image_size[0], image_size[1]*i))
        y_offset = 0
        for image in images:
            new_image.paste(image, (0, y_offset))
            y_offset += image_size[1]
        new_image.save("new/" + folder_name + " " + file_names[j])
