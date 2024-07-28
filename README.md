# Cent Remixer 🎉

## Overview

On Innovation Day, we created an exciting project that fetches song lyrics, passes them to an AI model for remixing, and displays the remixed lyrics on the UI. This project utilizes FastAPI, the Lyrics.ovh API, and the Gemma:2b model hosted on a local machine.

## Features

- 🎶 **Fetch Song Lyrics:** Retrieve song lyrics from the Lyrics.ovh API.
- 🤖 **AI Remix:** Use the Gemma:2b model to remix the fetched lyrics.
- 💻 **User Interface:** Display the remixed lyrics on the UI.

## How It Works

1. **Fetch Lyrics:**
   - The program uses the Lyrics.ovh API to fetch the lyrics of a specified song.

2. **Remix Lyrics:**
   - The fetched lyrics are sent to the Gemma:2b model, which is hosted locally.
   - The model processes the lyrics and generates a remixed version.

3. **Display Remixed Lyrics:**
   - The remixed lyrics are returned and displayed on the UI.

## Installation

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn
- Requests (for API calls)
- [Ollama](https://ollama.com/) with the Gemma:2b model downloaded and running

### Steps

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/ministerko/cent.git
    ```

2. **Navigate to the Project Directory:**

    ```sh
    cd cent
    ```

3. **Install Dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the FastAPI Server:**

    ```sh
    uvicorn main:app --reload
    ```

5. **Download and Run the Gemma:2b Model:**

    - Download the Gemma:2b model from [Ollama](https://ollama.com/).
    - Ensure the model's API is exposed at `127.0.0.1:8000/api/generate`.

## Usage

1. **Access the API:**

    Open your browser and go to `http://localhost:8000/docs` to access the API documentation and test the endpoints.

2. **Fetch and Remix Lyrics:**

    Use the provided endpoints to fetch lyrics of a song and get the remixed version.

## Example

1. **Fetch Lyrics:**

    ```sh
    GET /fetch-lyrics?song=Imagine&artist=John Lennon
    ```

2. **Remix Lyrics:**

    ```sh
    POST /remix-lyrics
    {
      "lyrics": "Imagine there's no heaven..."
    }
    ```

3. **View Remixed Lyrics:**

    The remixed lyrics will be displayed on the UI.

## Acknowledgements

- Thanks to [Lyrics.ovh](https://lyrics.ovh) for providing the API.
- Special thanks to the team for the innovative spirit and collaboration! 🤝

## License

This project is licensed under the MIT License.
