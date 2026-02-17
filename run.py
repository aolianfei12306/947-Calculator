"""
Run script for 947 Calculator with optional ngrok support
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def run_streamlit_local():
    """Run streamlit locally without ngrok"""
    print("🚀 Starting 947 Calculator locally...")
    print("📍 Local URL: http://localhost:8501")
    print("Press Ctrl+C to stop the server\n")
    
    # Run streamlit
    subprocess.run([
        sys.executable, "-m", "streamlit", "run", 
        "app.py",
        "--server.headless", "true"
    ])

def run_streamlit_with_ngrok(ngrok_token=None):
    """Run streamlit with ngrok for public access"""
    try:
        from pyngrok import ngrok, conf
        
        # Set ngrok token if provided
        if ngrok_token:
            conf.get_default().auth_token = ngrok_token
            print(f"✅ Ngrok token configured")
        
        # Start streamlit in background
        print("🚀 Starting 947 Calculator with ngrok...")
        
        # Set up ngrok tunnel
        port = 8501
        public_url = ngrok.connect(port, bind_tls=True)
        
        print(f"\n{'='*60}")
        print(f"✅ 947 Calculator is now running!")
        print(f"{'='*60}")
        print(f"📍 Local URL:  http://localhost:{port}")
        print(f"🌐 Public URL: {public_url}")
        print(f"{'='*60}")
        print("\nPress Ctrl+C to stop the server\n")
        
        # Start streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run",
            "app.py",
            "--server.headless", "true",
            "--server.port", str(port)
        ])
        
    except ImportError:
        print("❌ Error: pyngrok is not installed!")
        print("Please install it using: pip install pyngrok")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error starting ngrok: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure you have a valid ngrok token")
        print("2. Set token using: ngrok config add-authtoken YOUR_TOKEN")
        print("3. Or pass token via --token parameter")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Run 947 Calculator with optional ngrok support"
    )
    parser.add_argument(
        "--ngrok",
        action="store_true",
        help="Enable ngrok for public access"
    )
    parser.add_argument(
        "--token",
        type=str,
        help="Ngrok authentication token"
    )
    
    args = parser.parse_args()
    
    # Check if app.py exists
    if not Path("app.py").exists():
        print("❌ Error: app.py not found!")
        print("Please run this script from the project root directory.")
        sys.exit(1)
    
    # Run with or without ngrok
    if args.ngrok:
        run_streamlit_with_ngrok(args.token)
    else:
        run_streamlit_local()

if __name__ == "__main__":
    main()
