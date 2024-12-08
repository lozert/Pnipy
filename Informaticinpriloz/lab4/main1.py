from pydantic import BaseModel
from datetime import datetime
from typing import List
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
import os

# Создание экземпляра FastAPI
app = FastAPI()

# Механизм авторизации через токен
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Модели данных
class NoteCreate(BaseModel):
    text: str

class NoteInfo(BaseModel):
    created_at: datetime
    update_at: datetime

class NoteText(BaseModel):
    id: int
    text: str

class NoteID(BaseModel):
    id: int

class NoteList(BaseModel):
    notes: List[int]

notes_dir = "notes"

if not os.path.exists(notes_dir):
    os.makedirs(notes_dir)

# Заглушка для проверки токена
def verify_token(token: str = Depends(oauth2_scheme)):
    if token != "mysecrettoken":
        raise HTTPException(status_code=403, detail="Invalid token")
    return token

# Создание заметки
@app.post("/notes/", response_model=NoteID, dependencies=[Depends(verify_token)])
def create_note(text: NoteCreate):
    note_id = len(os.listdir(notes_dir)) + 1
    
    # Пытаемся записать заметку в файл
    try:
        with open(f"{notes_dir}/{note_id}.txt", "w") as file:
            file.write(text.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error writing note: {e}")
    
    # Возвращаем id созданной заметки
    return NoteID(id=note_id)

# Чтение заметки по ID
@app.get("/notes/{note_id}", response_model=NoteText, dependencies=[Depends(verify_token)])
def read_note(id: int):
    try:
        with open(f"{notes_dir}/{id}.txt", "r") as file:
            text = file.read()
        return NoteText(id=id, text=text)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Note not found")

# Изменение информации о заметке (время создания и последнего изменения)
@app.get("/notes/modify/{datatime_id}", response_model=NoteInfo, dependencies=[Depends(verify_token)])
def modify(id: int):
    try:
        file_stat = os.stat(f"{notes_dir}/{id.id}.txt")        
        last_modified = datetime.fromtimestamp(file_stat.st_mtime)

        try:
            creation_time = datetime.fromtimestamp(file_stat.st_ctime)
        except AttributeError:
            creation_time = None  
        
        return NoteInfo(created_at=creation_time, update_at=last_modified)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Note not found")


# Обновление текста заметки
@app.post("/notes/update/", response_model=NoteText, dependencies=[Depends(verify_token)])
def update_note(id: int, note: NoteCreate):  # Используем Pydantic модель для текста
    text = note.text
    
    try:
        with open(f"{notes_dir}/{id}.txt", "w") as file:
            file.write(text)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error writing note: {e}")
    
    return NoteText(id=id, text=text)

# Удаление заметки
@app.delete("/notes/{note_id}", response_model=NoteID, dependencies=[Depends(verify_token)])
def delete_note(note_id: int):
    try:
        os.remove(f"{notes_dir}/{note_id}.txt")
        return NoteID(id=note_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Note not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting note: {e}")

# Получение списка всех ID заметок
@app.get("/notes/", response_model=NoteList, dependencies=[Depends(verify_token)])
def list_notes():
    try:
        # Получаем все файлы в папке notes и извлекаем ID из их имен
        note_ids = [int(filename.split('.')[0]) for filename in os.listdir(notes_dir) if filename.endswith(".txt")]
        return NoteList(notes=note_ids)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching note list: {e}")

# Заглушка для получения токена
@app.post("/token")
def get_token():
    # Здесь должен быть механизм выдачи токена (например, через логин и пароль)
    return {"access_token": "mysecrettoken", "token_type": "bearer"}
