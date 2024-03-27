import os
from pytube import YouTube

def download_youtube_videos(urls, output_folder):
    for url in urls:
        yt = YouTube(url)
        title = yt.title.replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_') # Removing special characters from the title
        file_path = os.path.join(output_folder, title + '.mp4')
        yt.streams.filter(only_audio=True).first().download(output_path=output_folder, filename=title)

def rename_to_mp3(output_folder):
    for filename in os.listdir(output_folder):
        if os.path.isfile(os.path.join(output_folder, filename)):
            mp4_file_path = os.path.join(output_folder, filename)
            mp3_file_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.mp3')
            os.rename(mp4_file_path, mp3_file_path)
            print(f"Renamed {filename} to {os.path.splitext(filename)[0] + '.mp3'}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    output_folder = "C:/Users/user/PycharmProjects/youtubedownloader/music"  # Output folder same as script directory

    youtube_urls = []
    while True:
        youtube_url = input("Enter YouTube video URL (type 'download' to start downloading): ")
        if youtube_url.lower() == 'd':
            break
        youtube_urls.append(youtube_url)

    if youtube_urls:
        download_youtube_videos(youtube_urls, output_folder)
        print("Videos downloaded successfully.")
        rename_to_mp3(output_folder)

    else:
        print("No YouTube video URLs provided.")
