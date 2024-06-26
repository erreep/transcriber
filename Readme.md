# Transcriber App

## Introduction
The Transcriber App is a desktop application that allows users to transcribe MP3 audio files into text using OpenAI's Whisper model. The application offers a user-friendly graphical interface to select files, start transcription, and display the transcribed text.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Installation
To install the Transcriber App, follow these steps:
1. Ensure Python 3.x is installed on your system.
2. Clone this repository or download the source code.
3. Install the required dependencies by running: pip install -r requirements.txt


## Usage
To use the Transcriber App, execute the `main.py` script. The GUI will open where you can:
1. Click the "Browse" button to select an MP3 file.
2. Click the "Transcribe" button to start the transcription process.
3. View the transcribed text in the text area provided.

## Features
- Simple and intuitive graphical user interface.
- Supports transcription of MP3 files.
- Display of transcription directly in the application.

## Dependencies
The project requires the following Python libraries:
- `openai==0.27.8`
- `pydub==0.25.1`
- `python-dotenv==1.0.1`

## Configuration
Ensure that your OpenAI API key is configured correctly in the `.env` file:
OPEN_AI_API=your_openai_api_key_here


## Documentation
The source code is well-commented and structured into separate modules for easy understanding and further development.

## Examples
Here is how you can run the Transcriber App:
python main.py

Follow the GUI prompts to transcribe your MP3 files.

## Troubleshooting
- Ensure all dependencies are correctly installed.
- Check the `.env` file for a valid OpenAI API key.
- Ensure the MP3 file path is correctly entered or selected via the browse dialog.

## Contributors
-

## License
This project is licensed under the MIT License

