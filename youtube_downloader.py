import yt_dlp
import os

# Step 1: Create output folder
output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Folder '{output_folder}' created.")
else:
    print(f"Folder '{output_folder}' already exists.")

# Step 2: Ask for YouTube URL
url = input("Enter YouTube video URL: ")

# Step 3: Ask for download type
print("\nDownload options:")
print("1. Best quality video + audio (type 'best')")
print("2. Specific resolution (1080p/720p/360p)")
print("3. Audio only (MP3)")
choice = input("Enter your choice: ").lower()

ydl_opts = {
    'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
}

if choice == "best":
    ydl_opts['format'] = 'bestvideo+bestaudio/best'
elif choice in ["1080p", "720p", "360p"]:
    # Attempt to download requested resolution; fallback to best if unavailable
    ydl_opts['format'] = f'bestvideo[height<={choice[:-1]}]+bestaudio/best'
elif choice in ["audio", "mp3"]:
    ydl_opts['format'] = 'bestaudio/best'
    ydl_opts['postprocessors'] = [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
else:
    print("Invalid choice! Defaulting to best quality video + audio.")
    ydl_opts['format'] = 'bestvideo+bestaudio/best'

# Step 4: Download
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download completed!")
