from dotenv import load_dotenv
import os
import cloudinary

load_dotenv()

class Config:
    MONGODB_SETTINGS = {
        'host': os.getenv("DB_URL")
    }
    UPLOAD_FOLDER = 'public/uploads'
    cloudinary.config(
        cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
        api_key=os.getenv('CLOUDINARY_API_KEY'),
        api_secret=os.getenv('CLOUDINARY_API_SECRET')
    )
