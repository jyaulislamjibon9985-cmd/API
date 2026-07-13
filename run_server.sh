#!/bin/bash
# Smart Industrial Safety Monitoring API - Linux/macOS Startup Script

echo ""
echo "========================================"
echo "Industrial Safety Monitoring API"
echo "Version 1.0.0"
echo "========================================"
echo ""

# Determine which Python command is available
PYTHON_CMD=python3
if ! command -v "$PYTHON_CMD" > /dev/null 2>&1; then
    PYTHON_CMD=python
fi

if ! command -v "$PYTHON_CMD" > /dev/null 2>&1; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.9+ from https://www.python.org/downloads/"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$($PYTHON_CMD -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "Python version: $PYTHON_VERSION"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    $PYTHON_CMD -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Check if dependencies are installed
if ! python -m pip show fastapi > /dev/null 2>&1; then
    echo "Installing dependencies..."
    python -m pip install -r requirements.txt
fi

PORT=8000
if [ -n "$API_PORT" ]; then
    PORT=$API_PORT
fi

find_free_port() {
    local start_port=$1
    local max_port=8010
    for p in $(seq "$start_port" "$max_port"); do
        if ! python -c "import socket; s=socket.socket(); result=s.connect_ex(('127.0.0.1',$p)); s.close(); print(result)" | grep -q '^0$'; then
            echo "$p"
            return 0
        fi
    done
    return 1
}

FREE_PORT=$(find_free_port "$PORT")
if [ -z "$FREE_PORT" ]; then
    echo "ERROR: Could not find a free port between $PORT and 8010."
    exit 1
fi

PORT=$FREE_PORT

echo ""
echo "Starting server on port $PORT..."
echo ""
echo "========================================"
echo "API is running at: http://127.0.0.1:$PORT"
echo "Swagger UI: http://127.0.0.1:$PORT/docs"
echo "ReDoc: http://127.0.0.1:$PORT/redoc"
echo "========================================"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python -m uvicorn main:app --reload --host 127.0.0.1 --port "$PORT"
