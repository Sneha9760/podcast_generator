from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
import re

def extract_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    return match.group(1) if match else None

def fetch_captions(youtube_url):
    try:
        video_id = extract_video_id(youtube_url)
        if not video_id:
            raise ValueError("Invalid YouTube URL format.")
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry['text'] for entry in transcript])
    except TranscriptsDisabled:
        return "Transcripts are disabled for this video."
    except NoTranscriptFound:
        return "No captions found for this video."
    except Exception as e:
        return f"Error: {str(e)}"
