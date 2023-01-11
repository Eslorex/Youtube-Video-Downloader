from pytube import YouTube


video_url = input("Enter the URL of the video you want to download: ")


video = YouTube(video_url)


video_stream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()


video_stream.download()
