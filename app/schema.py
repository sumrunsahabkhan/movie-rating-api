from pydantic import BaseModel

class RatingRequest(BaseModel):
    User_Id: int
    Movie_Name: int
    Genre: int

class RatingResponse(BaseModel):
    predicted_rating: float
