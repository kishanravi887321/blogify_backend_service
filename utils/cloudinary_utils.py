import  cloudinary
import  os
from python_dotenv import load_dotenv
load_dotenv()
cloudinary.config(
    cloud_name=os.getenv('CLOUD_NAME'),
    api_key=os.getenv('API_KEY'),
    api_secret=os.getenv('API_SECRET')
)   
DEFAULt_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
