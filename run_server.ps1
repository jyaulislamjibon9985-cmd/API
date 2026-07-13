# Smart Industrial Safety Monitoring API - PowerShell Startup Script

Write-Host "========================================"
Write-Host "Industrial Safety Monitoring API"
Write-Host "Version 1.0.0"
Write-Host "========================================"

# Ensure Python is available
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    Write-Host "ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.9+ from https://www.python.org/downloads/"
    exit 1
}

# Create virtual environment if it does not exist
if (-not (Test-Path -Path "venv\Scripts\Activate.ps1")) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
}

# Activate virtual environment
Write-Host "Activating virtual environment..."
. .\venv\Scripts\Activate.ps1

# Install dependencies if needed
if (-not (python -m pip show fastapi -ErrorAction SilentlyContinue)) {
    Write-Host "Installing dependencies..."
    python -m pip install -r requirements.txt
}

function Get-FreePort {
    param(
        [int]$StartPort = 8000,
        [int]$EndPort = 8010
    )
    for ($port = $StartPort; $port -le $EndPort; $port++) {
        $listener = [System.Net.Sockets.TcpListener]::new([System.Net.IPAddress]::Parse('127.0.0.1'), $port)
        try {
            $listener.Start()
            $listener.Stop()
            return $port
        } catch {
            continue
        }
    }
    return $null
}

$port = 8000
if ($env:API_PORT) { $port = [int]$env:API_PORT }
$freePort = Get-FreePort -StartPort $port -EndPort 8010
if (-not $freePort) {
    Write-Host "ERROR: Could not find a free port between $port and 8010." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Starting server on port $freePort..."
Write-Host "========================================"
Write-Host "API is running at: http://127.0.0.1:$freePort"
Write-Host "Swagger UI: http://127.0.0.1:$freePort/docs"
Write-Host "ReDoc: http://127.0.0.1:$freePort/redoc"
Write-Host "========================================"
Write-Host "Press Ctrl+C to stop the server"
Write-Host ""

python -m uvicorn main:app --reload --host 127.0.0.1 --port $freePort
