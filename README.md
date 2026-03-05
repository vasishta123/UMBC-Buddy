# UMBC Buddy -A Chatbot for UMBC International Students using Dialogflow

## Abstract:
International students face a unique set of challenges when adjusting to life in a new country and pursuing their academic goals. Navigating unfamiliar cultural norms, academic systems, and campus resources can be overwhelming. To address these challenges, we developed an intelligent chatbot using Dialogflow, a natural language processing (NLP) platform, to provide comprehensive support to international students at the University of Maryland, Baltimore County (UMBC). The chatbot leverages the power of OpenAI’s search algorithms to accurately answer user queries related to UMBC, ranging from admissions procedures to student life. A webhook seamlessly integrates Dialogflow with a backend Python script, enabling the chatbot to access and provide real-time information to the students. Additionally, we integrated the chatbot with Slack, a popular messaging platform, allowing students to interact with the chatbot directly within their preferred communication channel.

![image](https://github.com/MANIMADHURIE/UMBC-Buddy/assets/37103568/b2afbf53-96f9-4631-890e-3e2233d4d16f)

## Technologies Used:

We have used the following technologies to develop the UMBC Buddy:

 1) Google Dialogflow
 
 2) Open AI
 
 3) Ngrok
 
 4) Slack

## Methodology:

Chatbot was tailored for UMBC international students, enhancing their experience and support. The official International Student Arrival Guide, sourced from UMBC, served as the primary text corpus for this work, which provided valuable information about admission, arrival details, classes, and services.

Our methodology involved several key steps:

• **Intent Recognition**: Categorized various student inquiries into specific intents to better understand and address their concerns effectively.

• **Entity Recognition**: The chatbot was trained to identify and extract relevant information from user queries, enabling it to provide accurate responses.

• **Knowledge Base Construction**: Compiled a structured repository of UMBC-related information to serve as a foundation for the chatbot's responses.

• **Dialogflow Integration**: Utilized Dialogflow, a natural language understanding platform, to build the chatbot's conversational interface. This involved defining intents, entities, and orchestrating the conversational flow.

• **OpenAI Integration**: By integrating OpenAI's advanced search algorithms, enhanced the chatbot's ability to provide precise and comprehensive responses to user inquiries.

• **Ngrok and Webhook Integration**: Used Ngrok to expose our locally hosted backend code to the internet, allowing Dialogflow to communicate with it via a webhook. This facilitated real-time data transmission between the chatbot and our backend Python script.

## Integration with Slack:

To extend the accessibility of our chatbot to a broader user base, we integrated it seamlessly with the Slack application using Webhook functionality. Users can conveniently access the chatbot by simply downloading the Slack application on their computers or mobile devices. This integration offers users the ability to interact with the chatbot effortlessly with just a single click.
When users input their queries within the Slack application, the system redirects these queries to Dialogflow through the Webhook integration. Subsequently, Dialogflow processes these queries and efficiently delivers the corresponding responses back to the users. This robust integration ensures a
smooth and user-friendly experience, allowing individuals to interact with the chatbot seamlessly within the familiar Slack environment.

**Result for query regarding international grocery stores:** 

![image](https://github.com/MANIMADHURIE/UMBC-Buddy/assets/37103568/944ecec3-f4b4-4692-8e61-bc35cd026084)

## FUTURE ENHANCEMENTS:

This chatbot integration extends beyond its initial scope and can be synergized with the UMBC transit system, thereby offering students real-time updates regarding transit schedules and routes. Additionally, integration with the UMBC International Student and Scholar Services (ISSS) system can enable the tracking of crucial application statuses such as I-20 and Curricular Practical Training (CPT) applications.
Furthermore, this chatbot’s functionality can be expanded to encompass the dissemination of emergency alerts across the campus. This enhanced capability ensures timely and crucial notifications reach students promptly, contributing to campus safety and security measures.

## CONCLUSION:

The integration of this Dialogflow-based chatbot marks a significant transformation in bolstering support for international students at UMBC. Through its provision of personalized assistance available around the clock, this chatbot is set to substantially enhance accessibility, operational efficiency, and the overall student journey. As we persist in refining and broadening its functionalities, we foresee this chatbot evolving into an indispensable asset, not only for international students at UMBC but also for all students. This strategic evolution positions the chatbot as an instrumental tool, promising continuous improvement in student support services and experiences.

## Installation & Setup

### Prerequisites
- Python 3.11+
- pip (Python package manager)
- Docker (optional, for containerized deployment)
- OpenAI API Key
- Google Dialogflow Project ID

### Local Installation

1. **Clone the repository**
```bash
git clone https://github.com/vasishta123/UMBC-Buddy.git
cd UMBC-Buddy
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
```bash
cp .env.example .env
# Edit .env and add your API keys and configuration
```

5. **Place the UMBC International Student Arrival Guide PDF**
```bash
mkdir -p data
# Place UMBC_International.pdf in the data/ directory
```

6. **Run the application**
```bash
python app.py
# Or using uvicorn directly
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`
API documentation: `http://localhost:8000/docs`

### Docker Deployment

1. **Build the Docker image**
```bash
docker build -t umbc-buddy:latest .
```

2. **Run the container**
```bash
docker run -p 8000:8000 \
  -e OPENAI_API_KEY=your-key \
  -e DIALOGFLOW_PROJECT_ID=your-id \
  -v $(pwd)/data:/app/data \
  umbc-buddy:latest
```

## Project Structure

```
UMBC-Buddy/
├── app.py                 # Main FastAPI application
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
├── .env.example         # Environment variables template
├── utils/               # Utility modules
│   ├── pdf_processor.py # PDF text extraction
│   ├── embeddings.py    # OpenAI embeddings
│   ├── dialogflow_client.py  # Dialogflow integration
│   └── response_handler.py   # Response generation
├── data/                # Data directory
│   └── UMBC_International.pdf
├── tests/              # Unit tests
and logs/                # Application logs
```

## API Endpoints

### Health Check
```
GET /health
```

### Chat Endpoint
```
POST /chat
Content-Type: application/json

{
  "query": "How do I apply for a student visa?",
  "session_id": "session_123",
  "user_id": "user_456"
}
```

## Key Features

✅ **Intelligent Query Processing** - Uses OpenAI GPT models for context understanding
✅ **Vector-Based Search** - FAISS for efficient semantic search
✅ **PDF Knowledge Base** - Extracts information from UMBC International Student Guide
✅ **Slack Integration** - Direct access via Slack messaging
✅ **Confidence Scoring** - Returns confidence levels for answers
✅ **Source Citation** - Provides source documents for answers
✅ **Rate Limiting** - Built-in protection against abuse
✅ **Caching** - Improved response times for common queries

## Configuration

All configuration is managed through the `.env` file. Key settings include:

- `OPENAI_API_KEY` - Your OpenAI API key
- `DIALOGFLOW_PROJECT_ID` - Google Dialogflow project ID
- `LLM_MODEL` - Language model (default: gpt-4-turbo)
- `TEMPERATURE` - Model creativity (0-1, default: 0.7)
- `CONFIDENCE_THRESHOLD` - Minimum confidence for responses

## Testing

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=.
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Future Enhancements

- Integration with UMBC Transit system
- ISSS (International Student Services) system integration
- Multi-language support
- Mobile app interface
- Advanced analytics dashboard

## Support

For questions or issues:
- Email: isss@umbc.edu
- Phone: 410-455-2511
- GitHub Issues: [Project Issues](https://github.com/vasishta123/UMBC-Buddy/issues)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- UMBC International Student Services
- Google Dialogflow team
- OpenAI
- All contributors and testers













