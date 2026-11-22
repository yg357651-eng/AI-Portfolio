
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Portfolio API",
    description="Backend API for my AI Engineering Portfolio",
    version="1.0.0"
)

# Allow our local frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Portfolio API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AI Portfolio Backend"
    }


@app.get("/api/v1/portfolio")
def get_portfolio():
    return {
        "name": "AI Engineer",
        "role": "Artificial Intelligence and Data Science Student",
        "description": "Building intelligent systems and AI-powered applications.",
        "technologies": [
            "Python",
            "Machine Learning",
            "Artificial Intelligence",
            "FastAPI",
            "RAG"
        ],
        "projects": [
            {
                "name": "Smart Study Hub",
                "status": "In Development"
            }
        ]
    }
