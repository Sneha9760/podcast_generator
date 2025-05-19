# 🎙️ YouTube to Podcast Generator

A complete pipeline that transforms any YouTube video into an engaging podcast episode. It fetches the transcript, converts it into a lively script between two fictional hosts (Emma and Mike), and generates an audio file with dual voice synthesis.


## 📦 Features

* 🎬 **YouTube Transcript Extraction**
  Fetches both manual and auto-generated captions.

* ✍️ **Podcast Script Generation**
  Uses [CrewAI](https://docs.crewai.com/) and [Groq LLaMA 3](https://groq.com/) to create a fun, conversational script between two hosts: *Emma* and *Mike*.

* 🔊 **Dual-Voice Audio Synthesis**
  Converts the podcast script into an audio file using two system voices with `pyttsx3`.


## 🛠️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/youtube-to-podcast.git
cd youtube-to-podcast
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```


## 🚀 How to Use

### Option 1: From Command Line

```bash
python main.py
```

* Paste the YouTube video URL when prompted.
* The script will:

  * Fetch captions
  * Generate a podcast script
  * Synthesize dual-voice audio
  * Save the output as `podcast.wav`



## 🧠 Project Structure

```
├── main.py                  # Main entry point
├── podcast_generator.py     # Handles LLM podcast script creation
├── audio_generator.py       # Generates audio using pyttsx3
├── utils.py                 # Helper for extracting video ID and transcripts
├── requirements.txt         # All required dependencies
└── .env                     # Your API key for Groq (not included in repo)
```



## 🎤 Sample Output

* Dialogue podcast script with Emma and Mike
* Natural, witty, and insightful tone
* Audio output: `podcast.wav`



## 🧰 Requirements

* Python 3.8+
* Packages:

  * `crewai`
  * `langchain_groq`
  * `pyttsx3`
  * `pydub`
  * `youtube-transcript-api`
  * `python-dotenv`
  * `pytube`
  * `requests`

Install them with:

```bash
pip install -r requirements.txt
```


## 📌 Notes

* Ensure you have at least **two TTS voices** installed on your OS.
* `pyttsx3` uses system voices (e.g., Microsoft David, Zira on Windows or macOS voices).


## 🙌 Acknowledgments

* [Groq](https://groq.com/) for blazing-fast inference
* [CrewAI](https://crewai.com/) for multi-agent orchestration
* [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/) for caption extraction


## 📄 License

MIT License. Feel free to use, modify, and share!

