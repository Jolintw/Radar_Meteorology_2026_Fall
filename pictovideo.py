from PIL import Image
from pathlib import Path
from datetime import datetime as dd

image_folder = Path('./pic')
video_name = 'output_moviepy.gif'
fps = 1

images = list(image_folder.glob("*"))
# images = [str(image) for image in images]
# print(images)
times = []
for image in images:
    filename = image.parts[-1]
    # times.append(dd.strptime(filename[9:21], "%Y%m%d%H%M"))
    times.append(dd.strptime(filename[12:24], "%Y%m%d%H%M"))
images = [x for _, x in sorted(zip(times, images))]
images = [Image.open(str(img)) for img in images]
images[0].save(video_name, save_all=True, append_images=images[1:], optimize=False, duration=100, loop=1)
