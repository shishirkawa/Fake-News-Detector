#!/usr/bin/env python3
"""
Unified startup script for the Fake News Detection Platform
This script starts the Flask backend server which also serves the frontend
"""

import os
import sys
import subprocess
import webbrowser
import time
import threading
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import flask
        import flask_cors
        print("[OK] Flask and Flask-CORS are installed")
        return True
    except ImportError as e:
        print(f"[ERROR] Missing dependency: {e}")
        print("Please install dependencies by running:")
        print("pip install -r requirements.txt")
        return False

def setup_directories():
    """Create necessary directories"""
    directories = ['Backend/uploads', 'Backend/logs', 'Backend/models', 'Backend/cache']
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"[OK] Created directory: {directory}")

def start_backend_server():
    """Start the Flask backend server"""
    print("\n[STARTING] Fake News Detection Platform...")
    print("=" * 50)
    
    # Change to backend directory
    backend_dir = Path(__file__).parent / "Backend"
    os.chdir(backend_dir)
    
    # Add backend/app to Python path
    sys.path.insert(0, str(backend_dir / "app"))
    
    try:
        # Import and run the Flask app
        from main import create_app
        
        app = create_app()
        
        print(f"[OK] Backend server starting on http://localhost:5000")
        print(f"[OK] Frontend will be served at http://localhost:5000")
        print(f"[OK] API endpoints available at http://localhost:5000/api/")
        print("\n" + "=" * 50)
        print("[READY] Fake News Detection Platform is ready!")
        print("[INFO] Open your browser to: http://localhost:5000")
        print("[INFO] Press Ctrl+C to stop the server")
        print("=" * 50)
        
        # Open browser after a short delay
        def open_browser():
            time.sleep(2)
            webbrowser.open('http://localhost:5000')
        
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        # Run the Flask app
        app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
        
    except ImportError as e:
        print(f"[ERROR] Error importing Flask app: {e}")
        print("Make sure you're in the correct directory and all dependencies are installed")
        return False
    except Exception as e:
        print(f"[ERROR] Error starting server: {e}")
        return False

def main():
    """Main entry point"""
    print("Fake News Detection Platform - Startup Script")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("Backend").exists() or not Path("Frontend").exists():
        print("[ERROR] Backend and Frontend directories not found!")
        print("Please run this script from the root directory of your project")
        return
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Setup directories
    setup_directories()
    
    # Start the server
    start_backend_server()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[STOPPED] Server stopped by user")
        print("Thank you for using Fake News Detection Platform!")
    except Exception as e:
        print(f"\n[ERROR] Unexpected error: {e}")
        print("Please check your setup and try again")
