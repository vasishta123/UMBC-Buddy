"""UMBC Buddy - Chatbot for UMBC International Students

Main FastAPI application for the UMBC Buddy chatbot.
Integrates Dialogflow, OpenAI, and FAISS for intelligent student assistance.
"""

import os
import logging
from typing import Optional
from datetime import datetime

from fastapi import FastAPI, HTTPException, Body, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import uvicorn
from dotenv import load_dotenv

from utils.pdf_processor import PDFProcessor
from utils.embeddings import EmbeddingManager
from utils.dialogflow_client import DialogflowClient
from utils.response_handler import ResponseHandler
from config import settings

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="UMBC Buddy Chatbot",
    description="AI-powered chatbot for UMBC international students",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request/response models
class ChatRequest(BaseModel):
    """Chat request model"""
    query: str = Field(..., min_length=1, max_length=1000, description="User query")
    session_id: Optional[str] = Field(None, description="Session ID for context")
    user_id: Optional[str] = Field(None, description="User identifier")

    class Config:
        schema_extra = {
            "example": {
                "query": "How do I apply for a student visa?",
                "session_id": "session_123",
                "user_id": "user_456"
            }
        }

class ChatResponse(BaseModel):
    """Chat response model"""
    response: str = Field(..., description="Chatbot response")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score")
    sources: Optional[list] = Field(None, description="Source documents")
    timestamp: str = Field(..., description="Response timestamp")
    session_id: Optional[str] = Field(None, description="Session ID")

class HealthResponse(BaseModel):
    """Health check response model"""
    status: str
    timestamp: str
    version: str

# Global instances
pdf_processor = None
embedding_manager = None
dialogflow_client = None
response_handler = None

@app.on_event("startup")
async def startup_event():
    """Initialize components on startup"""
    global pdf_processor, embedding_manager, dialogflow_client, response_handler
    
    try:
        logger.info("Initializing UMBC Buddy chatbot...")
        
        # Initialize PDF processor
        pdf_processor = PDFProcessor(settings.PDF_PATH)
        logger.info("PDF processor initialized")
        
        # Initialize embeddings
        embedding_manager = EmbeddingManager(
            api_key=settings.OPENAI_API_KEY
        )
        logger.info("Embedding manager initialized")
        
        # Initialize Dialogflow client
        dialogflow_client = DialogflowClient(
            project_id=settings.DIALOGFLOW_PROJECT_ID,
            session_id=settings.DIALOGFLOW_SESSION_ID
        )
        logger.info("Dialogflow client initialized")
        
        # Initialize response handler
        response_handler = ResponseHandler()
        logger.info("Response handler initialized")
        
        logger.info("UMBC Buddy chatbot successfully initialized")
        
    except Exception as e:
        logger.error(f"Failed to initialize chatbot: {str(e)}")
        raise

@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    logger.info("Shutting down UMBC Buddy chatbot")

@app.get("/", response_class=JSONResponse)
async def root():
    """Root endpoint"""
    return {
        "message": "UMBC Buddy Chatbot API",
        "version": "1.0.0",
        "docs_url": "/docs",
        "endpoints": {
            "health": "/health",
            "chat": "/chat",
            "docs": "/docs"
        }
    }

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now().isoformat(),
        version="1.0.0"
    )

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Main chat endpoint"""
    try:
        logger.info(f"Received query: {request.query}")
        
        if not embedding_manager or not response_handler:
            raise HTTPException(
                status_code=503,
                detail="Chatbot not fully initialized"
            )
        
        # Process query
        response_text, confidence, sources = await response_handler.generate_response(
            query=request.query,
            embedding_manager=embedding_manager,
            session_id=request.session_id
        )
        
        # Format response
        chat_response = ChatResponse(
            response=response_text,
            confidence=confidence,
            sources=sources,
            timestamp=datetime.now().isoformat(),
            session_id=request.session_id
        )
        
        logger.info(f"Response generated with confidence: {confidence}")
        return chat_response
        
    except Exception as e:
        logger.error(f"Error processing chat request: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Error processing request: {str(e)}"
        )

@app.get("/docs-redirect")
async def docs_redirect():
    """Redirect to Swagger docs"""
    return {"redirect_to": "/docs"}

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info"
    )
