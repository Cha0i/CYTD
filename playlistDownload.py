import os
from pytube import Playlist

download_dir = '/app/data'

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

def download_youtube_playlist(playlist_url, output_folder):
    playlist = Playlist(playlist_url)

    for video in playlist.videos:
        title = video.title.replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_') # Removing special characters from the title
        file_path = os.path.join(output_folder, title + '.mp4')
        video.streams.filter(only_audio=True).first().download(output_path=output_folder, filename=title)

def rename_to_mp3(output_folder):
    for filename in os.listdir(output_folder):
        if os.path.isfile(os.path.join(output_folder, filename)):
            mp4_file_path = os.path.join(output_folder, filename)
            mp3_file_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.mp3')
            os.rename(mp4_file_path, mp3_file_path)
            print(f"Renamed {filename} to {os.path.splitext(filename)[0] + '.mp3'}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    output_folder = download_dir
    

    playlist_url = input("Enter YouTube playlist URL: ")

    download_youtube_playlist(playlist_url, output_folder)
    print("Playlist downloaded successfully.")
    rename_to_mp3(output_folder)
