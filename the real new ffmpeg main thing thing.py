from os import system
from PIL import Image
from tkinter.simpledialog import askinteger
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import Button, IntVar, Label, Radiobutton, Tk
t=Tk()
vidin=askopenfilename(parent=t,title='Select a Video',filetypes=(('MPEG-4 Part 14','*.mp4'),))
swatch=askopenfilename(parent=t,title='Select a Swatch',filetypes=(('Adobe COlor file','*.aco'),))
vidout=asksaveasfilename(parent=t,title='Save Video As...',filetypes=(('MPEG-4 Part 14','*.mp4'),))
dithermodes=['bayer','heckbert','floyd_steinberg','sierra2','sierra2_4a']
desc=[
   'Ordered 8x8 bayer dithering (deterministic)',
   'Dithering as defined by Paul Heckbert in 1982 (simple error diffusion).\nNote: this dithering is sometimes considered "wrong" and is included as a reference.',
   'Floyd and Steingberg dithering (error diffusion)',
   'Frankie Sierra dithering v2 (error diffusion)',
   'Frankie Sierra dithering v2 "Lite" (error diffusion)'
]
def ok(e=None):
   global bayer
   bayer=None
   if v.get()==0:bayer=askinteger('Bayer scale (0-5)','Enter a Bayer scale:\nA low value means more visible pattern for less banding, and higher value means less visible pattern at the cost of more banding.',parent=t,minvalue=0,maxvalue=5,initialvalue=0)
   t.destroy()
v=IntVar()
for i,d in enumerate(dithermodes):
   Radiobutton(t,text=d,variable=v,value=i).pack(side='top',anchor='w')
   Label(t,text=desc[i]).pack(side='top',anchor='e')
Button(t,text='OK',command=ok).pack(side='top',anchor='center')
t.mainloop()
if not vidout.endswith('.mp4'):vidout+='.mp4'
system('swatch extract -i "'+swatch+'" -o "coma-separated values because its actually where csv comes from"')
with open('coma-separated values because its actually where csv comes from') as f:palette=f.read()
palette=[tuple(int(j[i:i+2],16)for i in range(0,len(j),4))for j in[i.split(',')[2][1:]for i in palette.splitlines()[1:]]]
print(palette)
p=Image.new('RGB',(len(palette),1))
p.putdata(palette)
p.resize((16,16),Image.Resampling.BOX).save('palette.png')
system(f'ffmpeg -i "{vidin}" -i palette.png -lavfi paletteuse=dither={dithermodes[v.get()]}{("bayer_scale="+str(bayer))*bayer} "{vidout}"')