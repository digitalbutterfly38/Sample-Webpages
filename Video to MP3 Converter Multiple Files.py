from moviepy.editor import VideoFileClip
import os

def extract_audio_from_videos(input_files, output_folder):
    try:
        for input_file in input_files:
            video_clip = VideoFileClip(input_file)
            audio_clip = video_clip.audio
            output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + ".mp3")
            audio_clip.write_audiofile(output_file)
            audio_clip.close()
            video_clip.close()
            print(f"Audio extracted and saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace input_videos with a list of paths to your input video files
    input_videos = ["D:\\Editing\\u1.mp4", "D:\\Editing\\u2.mp4"]
    # Replace output_folder with the desired output folder path
    output_folder = "D:\\Editing\\audio_output"
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    extract_audio_from_videos(input_videos, output_folder)
