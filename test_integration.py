#!/usr/bin/env python3
"""
Integration test script for the Fake News Detection Platform
Tests the connection between frontend and backend
"""

import requests
import json
import time
import subprocess
import sys
from pathlib import Path

def test_api_endpoints():
    """Test the API endpoints to ensure they're working"""
    base_url = "http://localhost:5000"
    
    print("🧪 Testing API Endpoints...")
    print("=" * 40)
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/api/health", timeout=5)
        if response.status_code == 200:
            print("✓ Health endpoint is working")
        else:
            print(f"✗ Health endpoint failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"✗ Health endpoint error: {e}")
        return False
    
    # Test text analysis endpoint
    try:
        test_text = "This is a test news article for fake news detection analysis."
        response = requests.post(
            f"{base_url}/api/analyze/text",
            json={"text": test_text},
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print("✓ Text analysis endpoint is working")
            else:
                print(f"✗ Text analysis failed: {data.get('error', 'Unknown error')}")
                return False
        else:
            print(f"✗ Text analysis endpoint failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"✗ Text analysis error: {e}")
        return False
    
    # Test URL analysis endpoint
    try:
        test_url = "https://example.com"
        response = requests.post(
            f"{base_url}/api/analyze/url",
            json={"url": test_url},
            timeout=10
        )
        if response.status_code == 200:
            print("✓ URL analysis endpoint is working")
        else:
            print(f"✗ URL analysis endpoint failed: {response.status_code}")
            # This might fail if the URL can't be accessed, which is okay for testing
    except requests.exceptions.RequestException as e:
        print(f"⚠ URL analysis error (expected if URL is not accessible): {e}")
    
    print("✓ API endpoints test completed")
    return True

def test_frontend_access():
    """Test if the frontend is accessible"""
    print("\n🌐 Testing Frontend Access...")
    print("=" * 40)
    
    try:
        response = requests.get("http://localhost:5000", timeout=5)
        if response.status_code == 200:
            if "Fake News Detector" in response.text:
                print("✓ Frontend is accessible and serving content")
                return True
            else:
                print("✗ Frontend is accessible but content seems incorrect")
                return False
        else:
            print(f"✗ Frontend access failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"✗ Frontend access error: {e}")
        return False

def check_dependencies():
    """Check if required dependencies are available"""
    print("📦 Checking Dependencies...")
    print("=" * 40)
    
    try:
        import flask
        import flask_cors
        print("✓ Flask and Flask-CORS are available")
        return True
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        return False

def main():
    """Main test function"""
    print("🔍 Fake News Detection Platform - Integration Test")
    print("=" * 60)
    
    # Check dependencies
    if not check_dependencies():
        print("\n❌ Dependencies check failed. Please install requirements:")
        print("pip install -r requirements.txt")
        return False
    
    # Check if server is running
    print("\n🔄 Checking if server is running...")
    try:
        response = requests.get("http://localhost:5000", timeout=2)
        print("✓ Server appears to be running")
    except requests.exceptions.RequestException:
        print("❌ Server is not running. Please start the server first:")
        print("python start_app.py")
        return False
    
    # Test API endpoints
    if not test_api_endpoints():
        print("\n❌ API endpoints test failed")
        return False
    
    # Test frontend access
    if not test_frontend_access():
        print("\n❌ Frontend access test failed")
        return False
    
    print("\n" + "=" * 60)
    print("🎉 All tests passed! Integration is working correctly.")
    print("🚀 You can now use the application at: http://localhost:5000")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⏹ Test interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error during testing: {e}")
        sys.exit(1)
