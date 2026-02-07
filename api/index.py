from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    """Root endpoint - returns a welcome message with 200 status"""
    return jsonify({
        "status": 200,
        "message": "API is running successfully!",
        "endpoints": {
            "root": "/",
            "health": "/health",
            "status": "/status"
        }
    }), 200

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": 200,
        "health": "OK",
        "timestamp": datetime.datetime.utcnow().isoformat()
    }), 200

@app.route('/status')
def status():
    """Status endpoint explicitly returning 200"""
    return jsonify({
        "status_code": 200,
        "message": "Request successful",
        "success": True,
        "data": {
            "service": "Flask API",
            "version": "1.0.0",
            "environment": "production"
        }
    }), 200

@app.route('/api/v1/info')
def api_info():
    """API information endpoint"""
    return jsonify({
        "status": 200,
        "api_name": "Status API",
        "author": "Your Name",
        "description": "A simple Flask API returning 200 status codes",
        "documentation": "Visit / for available endpoints"
    }), 200

# Custom error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "status": 404,
        "error": "Endpoint not found",
        "message": "The requested URL was not found on the server"
    }), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "status": 500,
        "error": "Internal server error",
        "message": "An unexpected error occurred"
    }), 500

if __name__ == "__main__":
    app.run(debug=True)
