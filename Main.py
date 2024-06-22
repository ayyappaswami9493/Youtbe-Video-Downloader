from pytube import YouTube
url=input("Enter your url: ")
my_video=YouTube(url)


print("VIDEO TITTLE: ",my_video.title)

print("THUMbNAIL: ",my_video.thumbnail_url)

"""stream=my_video.streams.all()
for i in stream:
    print(i)
"""
stream=my_video.streams.filter(progressive="True")
video=list(enumerate(stream))
for i in video:
    print(i)

index=int(input("Enter index NUmber which you want: "))
stream[index].download()


#my_video=my_video.streams.get_highest_resolution()
#my_video.download()
print("Successfully downloaded ")