# Smart Industrial Safety Monitoring API - PowerShell Offline Startup Script

Write-Host "========================================"
Write-Host "Industrial Safety Monitoring API (Offline)"
Write-Host "Version 1.0.0"
Write-Host "========================================"

# Ensure Python is available
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    Write-Host "ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "This offline startup requires Python 3.9+ installed locally."
    exit 1
}

# Ensure virtual environment exists
if (-not (Test-Path -Path "venv\Scripts\Activate.ps1")) {
    Write-Host "ERROR: Virtual environment not found." -ForegroundColor Red
    Write-Host "Create it first with an internet connection using:"
    Write-Host "python -m venv venv"
    Write-Host "python -m pip install -r requirements.txt"
    exit 1
}

# Activate virtual environment
Write-Host "Activating virtual environment..."
. .\venv\Scripts\Activate.ps1

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
Write-Host "Starting offline server on port $freePort..."
Write-Host "========================================"
Write-Host "API is running at: http://127.0.0.1:$freePort"
Write-Host "Swagger UI: http://127.0.0.1:$freePort/docs"
Write-Host "ReDoc: http://127.0.0.1:$freePort/redoc"
Write-Host "========================================"
Write-Host "Press Ctrl+C to stop the server"
Write-Host ""

python -m uvicorn main:app --host 127.0.0.1 --port $freePort
