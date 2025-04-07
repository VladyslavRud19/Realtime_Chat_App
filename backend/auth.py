import jwt
from fastapi import FastAPI, HTTPException, Depends  # Додаємо Depends тут
from fastapi.security import OAuth2PasswordRequestForm

SECRET_KEY = "your-secret-key"  # Змініть на безпечний ключ у продакшені
ALGORITHM = "HS256"

def verify_token(token: str) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return None
        return username
    except jwt.PyJWTError:
        return None

app = FastAPI()

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Тут має бути перевірка логіну/пароля, але для прикладу просто повертаємо токен
    token = jwt.encode({"sub": form_data.username}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}