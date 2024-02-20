from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta  # Add this import
from auth import create_access_token, Token, oauth2_scheme

app = FastAPI()

# Define your secret key and token-related constants
SECRET_KEY = "your_secret_key_here"  # Replace with a secure key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Replace this with your user authentication logic
def authenticate_user(username: str, password: str):
    # Example: Check if username and password are valid
    if username == "user" and password == "password":
        return {"username": username}
    return None

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/secure_data")
async def secure_data(token: str = Depends(oauth2_scheme)):
    # This endpoint is secured; only users with a valid token can access it
    return {"message": "This is secure data!", "token": token}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
