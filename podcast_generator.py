from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model="groq/llama3-8b-8192",
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_podcast_script(transcript):
    podcast_agent = Agent(
        role="Podcast Creator",
        goal="Create a podcast script based on a given transcript",
        backstory=(
            "You are a fun, engaging podcast host who transforms transcripts into "
            "listener-friendly, conversational episodes. Your style is natural, witty, "
            "and insightful."
        ),
        llm=llm,
        verbose=True
    )

    task_desc = (
        f"You will be given a YouTube transcript:\n\n{transcript}\n\n"
        "Convert it into a lively and engaging podcast episode script of 2-3 minutes. "
        "Structure it as a conversation between two hosts named Emma and Mike, discussing key ideas, interesting points, and add some light humor. "
        "End with a teaser for the next episode to keep listeners interested. "
        "Only output the podcast script dialogue, no extra thoughts or commentary."
        "Make sure the two hosts are always Emma and Mike."
    )

    task = Task(
        description=task_desc,
        expected_output=(
            "A dialogue podcast script with two hosts, friendly and informative, "
            "highlighting main ideas and keeping it engaging throughout."
        ),
        agent=podcast_agent
    )

    crew_instance = Crew(agents=[podcast_agent], tasks=[task], verbose=True)
    result = crew_instance.kickoff()

    try:
        if hasattr(result, "tasks_output") and len(result.tasks_output) > 0:
            output = result.tasks_output[0]
            if hasattr(output, "raw"):
                raw_text = output.raw
                if raw_text.lower().startswith("thought:"):
                    lines = raw_text.split("\n")
                    filtered_lines = [line for line in lines if not line.strip().lower().startswith("thought:") and line.strip()]
                    cleaned_text = "\n".join(filtered_lines).strip()
                    return cleaned_text if cleaned_text else raw_text
                else:
                    return raw_text
        return str(result)
    except Exception as e:
        print("Error extracting podcast script:", e)
        return str(result)
