from pytube import YouTube

SAVE_PATH = r"C:\Users\cdelgado\Pictures\Videos"

n = int(input("How many videos would you like to download? "))
urls = []
print("\nPaste one link per line: ")

for i in range(0, n):
    temp = input()
    urls.append(temp)

for i in range(0, n):
    url = urls[i]
    yt = YouTube(url)
    print("\nVideo Details for video ", i+1)
    print("\nVideo Title:\t", yt.title)
    print("\nVideo Length:\t", yt.length, "seconds")
    stream = str(yt.streams.filter(progressive=True))
    stream = stream[1:]
    stream = stream[:-1]
    stream_list = stream.split(", ")
    print("\nAll available options for downloads:\n")
    for i in range(0, len(stream_list)):
        sl = stream_list[i].split(" ")
        print(i+1,") ", sl[1], " and ", sl[3], sep='')
    tag = int(input("\nEnter the itag of the stream you would like to download:\t"))
    ys = yt.streams.get_by_itag(tag)
    print("\nDownloading... Please wait")
    ys.download(SAVE_PATH)
    print("\nDownload Complete!")