import requests
from utils.read_email import get_download_link
from dataclasses import dataclass
import os, random

@dataclass
class User:
    name: str
    password: str
    gmail_pass: str

def get_video(user: str) -> str:
    """Getting random video from folder videos."""
    file = random.choice(os.listdir('videos'))
    print(f'{user} has randomly draw a {file}')
    return f'videos/{file}'


def login(user: str, password: str) -> str:
    """Generating token for user."""
    url = 'http://mp3converter.com/login'
    res = requests.post(url,auth=(user, password))

    return res.text

# Uploading movie to the server.
def upload_movie(token: str, video: str, user:str):
    """Generating token for user."""
    url = 'http://mp3converter.com/upload'
    movie = open(video, 'rb')

    requests.post(
        url,
        headers={'Authorization': f'Bearer {token}'},
        files={'file': movie}
        )

    print(f'{user} has uploaded a {video} to the server.')

def download_mp3(user:str, token: str, file_id: str):
    """Downloading movie from server already converted to mp3."""
    url = 'http://mp3converter.com/download'
    res = requests.get(
        url,
        headers={'Authorization': f'Bearer {token}'},
        params={'fid': file_id}
        )

    with open(f'mp3s/{user}_{file_id}.mp3', 'wb') as f:
        f.write(res.content)

def test_flow(user: str, password: str, g_pass: str):
    """Starting a test flow for given user."""
    u = User(user, password, g_pass)
    token = login(u.name, u.password)
    upload_movie(token, get_video(user), user)

    download_link = None

    while download_link is None:
        download_link = get_download_link(u.name, u.gmail_pass)

    download_mp3(u.name, token, download_link)
    print(f'{user} has successfully downloaded the file.')
