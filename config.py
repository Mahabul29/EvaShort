import os

# Koyeb automatically sets the PORT environment variable. Fallback to 8000 for local testing.
PORT = int(os.environ.get("PORT", 8000))
HOST = "0.0.0.0"

