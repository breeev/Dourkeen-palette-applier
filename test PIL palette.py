from os import system
from PIL import Image
system('swatch extract -i wind_chill_swatches.aco -o "coma-separated values because its actually where csv comes from"')
with open('coma-separated values because its actually where csv comes from') as f:palette=f.read()
palette=''.join([i.split(',')[2][1:]for i in palette.splitlines()[1:]])
palette=[int(palette[i:i+2],16) for i in range(0,len(palette),4)]
print(palette)
p=Image.new('P',(len(palette),1))
p.putpalette(palette)
p.resize((16,16),Image.Resampling.BOX).show()
# Image.open('frames/0001.bmp')