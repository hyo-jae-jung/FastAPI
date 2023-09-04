from beanie import Document
from pydantic import BaseModel, EmailStr


class User(Document):
    email: EmailStr
    password: str
    
    class Settings:
        name = "users"
    
    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!"
            }
        }


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    

if __name__ == "__main__":
    
    example = {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": [{   
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
                }],
            }
    
    print(User(**example))
    