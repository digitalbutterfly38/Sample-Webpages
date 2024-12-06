
from moviepy.editor import VideoFileClip




def extract_audio_from_video(input_file, output_file):

    try:

        video_clip = VideoFileClip(input_file)

        audio_clip = video_clip.audio

        audio_clip.write_audiofile(output_file)

        audio_clip.close()

        video_clip.close()

        print(f"Audio extracted and saved to {output_file}")

    except Exception as e:

        print(f"An error occurred: {e}")




if __name__ == "__main__":

    # Replace input_video.mp4 with the path to your input video file

    input_video = "D:\\Editing\\u1.mp4"




    # Replace output_audio.wav with the desired output audio file path

    output_audio = "D:\\Editing\\u1.mp3"




    extract_audio_from_video(input_video,output_audio)