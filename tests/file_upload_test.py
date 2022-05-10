def test_uploading_file(client):
    file = "music.csv"
    data = {
        'music': (open(file, 'rb'), file)
    }
    response = client.post('/songs/upload', data=data)
    assert response.status_code == 400


