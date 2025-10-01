from app import create_app
import os

app = create_app()

if __name__ == "__main__":
    # Use the PORT environment variable provided by Render
    port = int(os.environ.get("PORT", 5000))
    # Bind to 0.0.0.0 so the port is reachable
    app.run(host="0.0.0.0", port=port, debug=False)
