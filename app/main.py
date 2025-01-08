from fastapi import FastAPI
from app.routes import text_tools, random_tools, utility_tools, date_tools

app = FastAPI(
    title="ToolBox API",
    description="An advanced API offering utilities for text, random data, and much more!",
    version="1.0"
)

# Include routes
app.include_router(text_tools.router, prefix="/text-tools", tags=["Text Tools"])
app.include_router(random_tools.router, prefix="/random-tools", tags=["Random Tools"])
app.include_router(utility_tools.router, prefix="/utility-tools", tags=["Utility Tools"])
app.include_router(date_tools.router, prefix="/date-tools", tags=["Date and Time Tools"])

@app.get("/")
def root():
    return {"message": "Welcome to the ToolBox API! Made by Nayan Das"}
