import pytest
from server import app
import io

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client



# Test 1: Index Route - Website Erfolgreich Laden
def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"User Stories Generator" in response.data



# Test 2: Beliebiger Text Upload
def test_text_upload(client):
    response = client.post('/input/text', data={'text': 'Problembeschreibung X/Y'})
    assert response.status_code == 302
    assert 'Location' in response.headers



# Test 3: Simulieren mit einer test.pdf
def test_file_upload(client):
    data = {
        'file': (io.BytesIO(b"test.pdf"), 'test.pdf')
    }
    response = client.post('/input/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 302
    assert 'Location' in response.headers



# Test 4: Korrektes Löschen von Dateien mit einer test.pdf
def test_file_delete(client):
    response = client.post('/backend/manage/files', data={
        'filename_checkbox': ['test.pdf'],
        'filenamesSelection': 'deleteFile'
    })
    assert response.status_code == 302
    assert 'Location' in response.headers



# Test 5: Löschen von Personas
def test_delete_personas(client):
    response = client.post('/backend/manage/personas', data={
        'persona_checkbox': ['Test Persona'],
        'parsedTextSelection': 'delete'
    })
    assert response.status_code == 302
    assert 'Location' in response.headers



# Test 6: User Story generieren
def test_generate_user_stories(client):
    response = client.get('/backend/llm/generate_text')
    assert response.status_code == 302
    assert 'Location' in response.headers



# Test 7: Löschen von User Stories
def test_manage_user_stories_delete(client):
    response = client.post('/backend/manage/user_stories', data={
        'user_story_checkbox': ['beispiel user Story'],
        'userStorySelection': 'delete'
    })
    assert response.status_code == 302
    assert 'Location' in response.headers


# Test 8: User Story neu generieren
def test__user_stories_regenerate(client):
    response = client.post('/backend/manage/user_stories', data={
        'user_story_checkbox': ['beispiel user story'],
        'userStorySelection': 'regenerate'
    })
    assert response.status_code == 302
    assert 'Location' in response.headers


 # Test 9: Test mit Ungültigem Dateityp
def test_file_upload_invalid_type(client):
    data = {
        'file': (io.BytesIO(b"Dummy content"), 'test.txt')
    }
    response = client.post('/input/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert b"Die Datei wurde nicht hochgeladen" in response.data


# Test 10: Test mit leerem Inhalt
def test_text_upload_empty(client):
    response = client.post('/input/text', data={'text': ''})
    assert response.status_code == 302
    assert 'Location' in response.headers

