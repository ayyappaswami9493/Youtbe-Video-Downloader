from pytube import YouTube
from tkinter import *
from moviepy.editor import VideoFileClip

root=Tk() #it's start main window
root.title('YouTube Video Downloader')
root.geometry('550x550+350+110')  #size and location of the window
root.configure(bg='#8E8B8A')
root.resizable(False,False)


def download():
    v_link=link.get('1.0','end')
    video=YouTube(v_link)
    root.title('downloading.....')
    '''
   stream=video.streams.filter(progressive='True',res='720')
    my_video=stream.first()
    my_video.download()
    root.title('Successfully downloaded')
    clip=VideoFileClip(my_video)
    clip.close()'''
    my_video=video.streams.get_highest_resolution()
    my_video.download()
    pass

def audio():
    v_link=link.get('1.0','end')
    video=YouTube(v_link)
    root.title('downloading.....')
    stream=video.streams.filter(mime_type='audio/mp4',abr='128kbps')
    my_video=stream.first()
    my_video.download()
    root.title('Successfully downloaded')
    clip=VideoFileClip(my_video)
    clip.close()


    pass

#image creation
img=PhotoImage(file='a.png')
Label(image=img,bd=1,bg='#8E8B8A').place(x=100,y=30)

#setting white frame in this window
frame=Frame(width='510',height='350')
frame.place(x=20,y=190)

#Labels in frame 
#this is for frame name YouTube Video Downloader
fr=Label(frame,text='YouTube Video Downloader',fg='#E5F520',font=('microsoft yahie UI Light',27,'bold'),bg='#1577B2')
fr.place(x=15,y=30)

f=Label(frame,text='LINK: ',fg='#E5F520',font=('microsoft yahie UI Light',23,'bold'),bg='#1577B2')
f.place(x=15,y=120)

link=Text(frame,bd=1,fg='black',heigh='1',width='22',bg='#DADAD2',font=('microsoft yahie UI Light',23,'bold'))
link.place(x=125,y=123)

b=Button(frame,text='Download',bd='3',width='10',fg='#E5F520',font=('microsoft yahie UI Light',15,'bold'),bg='#1577B2',command=download)
b.place(x=300,y=230)

b2=Button(frame,text='Audio',bd='3',width='10',fg='#E5F520',font=('microsoft yahie UI Light',15,'bold'),bg='#1577B2',command=audio)
b2.place(x=100,y=230)

aa=Label(frame,text='Ayyappa Swami',fg='#52DE5F',font=('microsoft yahie UI Light',10,'bold'),bg='#925AE8')
aa.place(x=200,y=325)

root.mainloop()#it access the events 




