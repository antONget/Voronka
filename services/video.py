from pytube import YouTube


def youtube_video(video_link):
    yt = YouTube(video_link)
    video = yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download("./tmp")
    return video
