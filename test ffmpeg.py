from os import system
# system(r'ffmpeg -i file.mp4 "frames/%04d.bmp"')
system(r'ffmpeg -i file.mp4 -i palette.jpg -lavfi paletteuse output.mp4')