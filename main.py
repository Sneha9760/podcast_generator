from podcast_generator import generate_podcast_script
from youtube_transcript_api import YouTubeTranscriptApi
import re
from audio_generator import generate_dual_voice_audio  

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

def fetch_transcript(video_url):
    video_id_match = re.search(r"v=([a-zA-Z0-9_-]+)", video_url)
    if not video_id_match:
        raise ValueError("Invalid YouTube URL.")
    video_id = video_id_match.group(1)
    
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([entry['text'] for entry in transcript_list])
        print("Captions fetched successfully.")
        return transcript_text
    except NoTranscriptFound:
        print("No manual transcript found. Trying auto-generated transcript...")
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'], generated=True)
            transcript_text = " ".join([entry['text'] for entry in transcript_list])
            print("Auto-generated captions fetched successfully.")
            return transcript_text
        except Exception as e2:
            print("Error fetching auto-generated captions:", e2)
            return None
    except TranscriptsDisabled:
        print("Transcripts are disabled for this video.")
        return None
    except Exception as e:
        print("Error fetching captions:", e)
        return None


def main():
    video_url = input("Enter YouTube video URL: ").strip()
    transcript = fetch_transcript(video_url)
    if not transcript:
        print("Failed to fetch captions. Exiting.")
        return
    
    print("\nGenerating podcast script...\n")
    script = generate_podcast_script(transcript)
    print("--- Podcast Script ---\n")
    print(script)

    if script:
        print("\nGenerating audio file with two voices...")
        generate_dual_voice_audio(script, output_filename="podcast.wav")
        print("Audio file saved as podcast.wav")

if __name__ == "__main__":
    main()
