from fastapi import FastAPI

from core.config import settings
from api.api import api

app = FastAPI(title='User API - FastAPI | SQL Model')
app.include_router(router=api, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn
    from dotenv import load_dotenv
    from os import getenv
    
    load_dotenv()
    
    host = getenv('HOST')
    port = getenv('PORT')
    
    uvicorn.run('main:app', port=int(port), host=host, reload=True, log_level='info')

