# Fake News Detection Platform

A comprehensive AI-powered web application for detecting and analyzing fake news using advanced machine learning techniques and multiple verification sources.

## 🚀 Features

- **Text Analysis**: Analyze news articles by pasting text content
- **URL Analysis**: Extract and analyze content from news article URLs
- **Image Analysis**: Upload images with text for OCR-based analysis
- **Real-time Processing**: Fast analysis with confidence scoring
- **Source Verification**: Cross-reference with multiple fact-checking databases
- **Detailed Reports**: Comprehensive analysis with evidence and sources
- **Modern UI**: Responsive design with intuitive user interface

## 🛠️ Technology Stack

### Backend
- **Flask**: Web framework for Python
- **SQLAlchemy**: Database ORM
- **Flask-CORS**: Cross-origin resource sharing
- **BeautifulSoup**: Web scraping and content extraction
- **Pillow**: Image processing
- **Tesseract**: OCR for image text extraction
- **NLTK**: Natural language processing
- **Scikit-learn**: Machine learning models

### Frontend
- **HTML5**: Modern semantic markup
- **CSS3**: Responsive design with animations
- **Vanilla JavaScript**: Interactive functionality
- **Font Awesome**: Icons and UI elements

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd Hackops
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Tesseract OCR** (for image analysis)
   
   **Windows:**
   - Download from: https://github.com/UB-Mannheim/tesseract/wiki
   - Install and add to PATH
   
   **macOS:**
   ```bash
   brew install tesseract
   ```
   
   **Linux (Ubuntu/Debian):**
   ```bash
   sudo apt-get install tesseract-ocr
   ```

## 🚀 Quick Start

### Option 1: Using the Unified Startup Script (Recommended)

Simply run the startup script which will handle everything:

```bash
python start_app.py
```

This will:
- Check dependencies
- Create necessary directories
- Start the Flask backend server
- Serve the frontend
- Open your browser automatically

### Option 2: Manual Setup

1. **Start the Backend Server**
   ```bash
   cd Backend
   python run.py
   ```

2. **Access the Application**
   - Open your browser and go to: `http://localhost:5000`
   - The Flask server will serve both the API and frontend

## 📁 Project Structure

```
Hackops/
├── Backend/                 # Flask backend application
│   ├── app/                # Main application code
│   │   ├── api/           # API endpoints
│   │   ├── models/        # Database models and ML models
│   │   ├── services/      # Business logic services
│   │   ├── utils/         # Utility functions
│   │   ├── config.py      # Configuration settings
│   │   └── main.py        # Flask application factory
│   ├── requirements.txt   # Python dependencies
│   └── run.py            # Backend startup script
├── Frontend/              # Frontend application
│   ├── assets/           # CSS, JS, and other assets
│   ├── components/       # Reusable components
│   ├── pages/           # Page-specific scripts
│   └── index.html       # Main HTML file
├── requirements.txt      # Root dependencies file
├── start_app.py         # Unified startup script
└── README.md           # This file
```

## 🔌 API Endpoints

The backend provides the following API endpoints:

- `POST /api/analyze/text` - Analyze text content
- `POST /api/analyze/url` - Analyze content from URL
- `POST /api/analyze/image` - Analyze image with OCR
- `GET /api/health` - Health check endpoint
- `POST /api/sources/verify` - Verify external sources

### Example API Usage

**Analyze Text:**
```bash
curl -X POST http://localhost:5000/api/analyze/text \
  -H "Content-Type: application/json" \
  -d '{"text": "Your news article text here"}'
```

**Analyze URL:**
```bash
curl -X POST http://localhost:5000/api/analyze/url \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/news-article"}'
```

## 🎯 How to Use

1. **Text Analysis**
   - Select "Text Input" tab
   - Paste your news article text
   - Click "Analyze News"

2. **URL Analysis**
   - Select "URL Input" tab
   - Enter the news article URL
   - Click "Fetch Content" to extract text
   - Click "Analyze News"

3. **Image Analysis**
   - Select "Image Upload" tab
   - Upload an image containing text
   - Click "Analyze News"

4. **View Results**
   - Review the verdict and confidence score
   - Check detailed metrics (factual accuracy, source reliability, etc.)
   - Examine sources and evidence
   - Download or share the report

## ⚙️ Configuration

The application can be configured through environment variables:

- `FLASK_ENV`: Set to 'development' or 'production'
- `SECRET_KEY`: Flask secret key for sessions
- `DATABASE_URL`: Database connection string
- `FACT_CHECK_API_KEY`: API key for fact-checking services
- `UPLOAD_FOLDER`: Directory for file uploads

## 🔧 Development

### Running in Development Mode

```bash
# Set environment variables
export FLASK_ENV=development
export FLASK_DEBUG=True

# Start the application
python start_app.py
```

### Testing the API

```bash
# Test health endpoint
curl http://localhost:5000/api/health

# Test text analysis
curl -X POST http://localhost:5000/api/analyze/text \
  -H "Content-Type: application/json" \
  -d '{"text": "Sample news text for testing"}'
```

## 🐛 Troubleshooting

### Common Issues

1. **"Module not found" errors**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`

2. **Tesseract OCR not working**
   - Install Tesseract and ensure it's in your PATH
   - For Windows, download from the official GitHub repository

3. **CORS errors in browser**
   - The application is configured with CORS for localhost
   - If accessing from a different domain, update CORS settings in `Backend/app/main.py`

4. **Port already in use**
   - Change the port in `start_app.py` or kill the process using port 5000

### Logs

Check the logs in the `Backend/logs/` directory for detailed error information.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Fact-checking databases and APIs
- Open source ML libraries
- Font Awesome for icons
- Google Fonts for typography

## 📞 Support

For support and questions:
- Create an issue in the repository
- Check the troubleshooting section
- Review the API documentation

---

**Happy Fake News Detection!** 🛡️
