# YouTube Video Transcript Summarizer

This project summarizes YouTube video transcripts using the `google/bigbird-pegasus-large-pubmed` model from Hugging Face. The application uses Gradio for a web-based interface to input YouTube URLs and display the summarized text.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Model](#model)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/youtube-transcript-summarizer.git
    cd youtube-transcript-summarizer
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python app.py
    ```

2. Open the Gradio interface in your browser. Input the YouTube video URL you want to summarize.

3. The application will fetch the transcript, split it into manageable chunks, and summarize each chunk using the `google/bigbird-pegasus-large-pubmed` model.

## Features

- Extracts and summarizes YouTube video transcripts.
- Handles long transcripts by splitting them into smaller chunks.
- Uses the `google/bigbird-pegasus-large-pubmed` model for high-quality summarization.
- Provides a user-friendly web interface using Gradio.

## Model

The project uses the `google/bigbird-pegasus-large-pubmed` model from Hugging Face. This model supports long sequence lengths, making it suitable for processing lengthy YouTube transcripts.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Hugging Face Transformers](https://github.com/huggingface/transformers)
- [Gradio](https://github.com/gradio-app/gradio)
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)


### requirements

```plaintext
transformers
torch
gradio
youtube-transcript-api
```
