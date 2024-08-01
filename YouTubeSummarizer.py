import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import torch
import gradio as gr
from transformers import pipeline

device = 0 if torch.cuda.is_available() else -1
# Use a pipeline as a high-level helper
text_summary = pipeline("summarization", model="google/bigbird-pegasus-large-pubmed", device=device)

def split_into_chunks(text, max_length=1024):
    sentences = text.split('. ')
    current_chunk = []
    current_length = 0
    chunks = []

    for sentence in sentences:
        sentence_length = len(sentence.split())
        if current_length + sentence_length > max_length:
            chunks.append('. '.join(current_chunk) + '.')
            current_chunk = []
            current_length = 0

        current_chunk.append(sentence)
        current_length += sentence_length

    if current_chunk:
        chunks.append('. '.join(current_chunk) + '.')

    return chunks

def summary(input_text):
    chunks = split_into_chunks(input_text, max_length=1024)
    summaries = []

    for i, chunk in enumerate(chunks):
        # Ensure chunk length is within model limits
        try:
            chunk_summary = text_summary(chunk, max_length=512, min_length=30, do_sample=False)[0]['summary_text']
            summaries.append(chunk_summary)
        except Exception as e:
            summaries.append(f"An error occurred while summarizing chunk {i + 1}: {e}")

    return ' '.join(summaries)

def extract_video_id(url):
    # Regex to extract the video ID from various YouTube URL formats
    regex = r"(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    match = re.search(regex, url)
    if match:
        return match.group(1)
    return None

def get_youtube_transcript(video_url):
    video_id = extract_video_id(video_url)
    if not video_id:
        return "Video ID could not be extracted."

    try:
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Format the transcript into plain text
        formatter = TextFormatter()
        text_transcript = formatter.format_transcript(transcript)
        summary_text = summary(text_transcript)

        return summary_text
    except Exception as e:
        return f"An error occurred: {e}"

gr.close_all()

demo = gr.Interface(fn=get_youtube_transcript,
                    inputs=[gr.Textbox(label="Input YouTube URL to summarize", lines=1)],
                    outputs=[gr.Textbox(label="Summarized text", lines=4)],
                    title="YouTube Script Summarizer",
                    description="This application will summarize the YouTube video script.")
demo.launch(share=True)
