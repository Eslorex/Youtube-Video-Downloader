from pytube import YouTube

# Prompt the user for the URL of the video they want to download
video_url = input("Enter the URL of the video you want to download: ")

# Create a YouTube object using the URL
video = YouTube(video_url)

# Get the first video stream with the highest available resolution and frame rate
video_stream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

# Download the video to the current directory
video_stream.download()