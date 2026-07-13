#!/bin/bash
# Smart Industrial Safety Monitoring API - Offline Startup Script

echo ""
echo "========================================"
echo "Industrial Safety Monitoring API (Offline)"
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
    echo "This offline startup requires Python 3.9+ installed locally."
    exit 1
fi

# Ensure virtual environment exists
if [ ! -d "venv" ]; then
    echo "ERROR: Virtual environment not found."
    echo "Create it first with an internet connection using:"
    echo "  $PYTHON_CMD -m venv venv"
    echo "  $PYTHON_CMD -m pip install -r requirements.txt"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

PORT=8000
if [ -n "$API_PORT" ]; then
    PORT=$API_PORT
fi

find_free_port() {
    local start_port=$1
    local max_port=8010
    for p in $(seq "$start_port" "$max_port"); do
        if ! python -c "import socket,sys; s=socket.socket(); result=s.connect_ex(('127.0.0.1', int(sys.argv[1]))); s.close(); print(result)" "$p" | grep -q '^0$'; then
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
echo "Starting offline server on port $PORT..."
echo ""
echo "========================================"
echo "API is running at: http://127.0.0.1:$PORT"
echo "Swagger UI: http://127.0.0.1:$PORT/docs"
echo "ReDoc: http://127.0.0.1:$PORT/redoc"
echo "========================================"
echo "Press Ctrl+C to stop the server"
echo ""

python -m uvicorn main:app --host 127.0.0.1 --port "$PORT"
