from pytube import YouTube

SAVE_PATH = r"C:\Users\cdelgado\Pictures\Videos"

url = input("Enter the YouTube video link: \n")
print('\n')

try:
    video = YouTube(str(url))
except:
    print("Error Occurred")
    exit("Exiting app")

stream = str(video.streams.filter(progressive=True))
stream = stream[1:]
stream = stream[:-1]
stream_list = stream.split(", ")
print("\nAll available options for downloads:\n")
for i in range(0, len(stream_list)):
    sl = stream_list[i].split(" ")
    print(i+1,") ", sl[1], " and ", sl[3], sep='')
tag = int(input("\nEnter the itag of the stream you would like to download:\t"))
videoStream = video.streams.get_by_itag(tag)
print("\nNow downloading ", video.title, ". Please wait.")
videoStream.download(SAVE_PATH)
print("\nDownload Complete!")
