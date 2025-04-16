import pytube
link=input("Paste Youtubbe video url Here: ")
yt= pytube.Youtube(link)
yt.streams.first().download()
print("video Has Been Download!")