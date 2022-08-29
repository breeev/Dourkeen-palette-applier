from os import system# execute commands
from tkinter import Tk# Window
from tkinter.filedialog import askopenfilename
from PIL import Image# Image object, container
from time import sleep# to wait
system('swatch extract -i wind_chill_swatches.aco -o "coma-separated values because its actually where csv comes from"')
with open('coma-separated values because its actually where csv comes from') as f:palette=f.read()
palette=[tuple(int(j[i:i+2],16)for i in range(0,len(j),4))for j in[i.split(',')[2][1:]for i in palette.splitlines()[1:]]]
t=Tk()
p=Image.open(askopenfilename(parent=t,title='Select a Picture (please)',filetypes=(
   ('Portable Network Graphics','*.png'),
   ('Joint Photographic Experts Group',['*.jpg','*.jpeg']),
   ('Other files','*.*')
))).convert('RGB')
t.destroy()
n=Image.new('RGB',p.size)
nl=[]
print('Working hard...')
rgb=[None,None,None]
for c in range(3):rgb[c]=[i[c] for i in palette]
# color=(254,12,59)
# let the competition BEGIN
for color in p.getdata():
   points=[0 for i in range(len(palette))]
   for i in range(3):
      best=min(rgb[i],key=lambda x:abs(x-color[i]))
      for x,e in enumerate(rgb[i]):
         if e==best:points[x]+=1
   nl.append(palette[points.index(max(points))])
n.putdata(nl)
n.show()
sleep(10)