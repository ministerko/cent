import json
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import requests
import uvicorn

app = FastAPI()

app.mount("/templates", StaticFiles(directory="templates"), name="templates")

class RemixRequest(BaseModel):
    model: str
    prompt: str

def get_lyrics(song_title: str) -> str:
    url = f"https://api.lyrics.ovh/v1/Coldplay/{song_title}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('lyrics', 'No lyrics found')
    else:
        return 'Error fetching lyrics'

def remix_lyrics(lyrics: str) -> str:
    gemma_endpoint = "http://127.0.0.1:11434/api/generate"
    payload = {
        "model": "gemma:2b",
        "prompt": f"Remix the following lyrics:\n{lyrics}"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(gemma_endpoint, headers=headers, json=payload)
    
    # Print or log the raw response content
    print("Response Content:", response.text)
    
    if response.status_code == 200:
        try:
            result_text = ''
            # Process each line as a separate JSON object
            for line in response.iter_lines(decode_unicode=True):
                if line.strip():  # Ignore empty lines
                    result = json.loads(line)
                    if result.get('done', False):
                        result_text += result.get('response', '')
                        break
                    result_text += result.get('response', '')
            
            return result_text
        
        except json.JSONDecodeError:
            return 'Error decoding JSON response'
        except requests.RequestException as e:
            return f'Error during request: {e}'
    else:
        return f'Error: Received status code {response.status_code}'
    return 'Remixing failed'

@app.get('/scrape_and_remix')
def scrape_and_remix(song_title: str = Query(..., description="Title of the song to scrape lyrics for")):
    if song_title:
        lyrics = get_lyrics(song_title)
        remixed_lyrics = remix_lyrics(lyrics)
        return {
            'original_lyrics': lyrics,
            'remixed_lyrics': remixed_lyrics
        }
    raise HTTPException(status_code=400, detail="No song title provided")


@app.get('/')
async def read_index():
    return FileResponse('templates/index.html')
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
