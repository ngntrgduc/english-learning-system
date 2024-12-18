"""Contain create, read and update database functions on Notion using Notion API"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
VOCAB_DATABASE_ID = os.getenv('VOCAB_DATABASE_ID')

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def create(data: dict):
    url = "https://api.notion.com/v1/pages"
    payload = {"parent": {"database_id": VOCAB_DATABASE_ID}, "properties": data}
    requests.post(url, headers=headers, json=payload)
    pass

def read_database(database_id: str):
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    data = requests.post(url, headers=headers).json()
    return data

def update(page_id: str, data: dict):
    url = f"https://api.notion.com/v1/pages/{page_id}"
    requests.patch(url, json={"properties": data}, headers=headers)
    pass
