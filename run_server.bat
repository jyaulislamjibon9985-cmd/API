@echo off
REM Smart Industrial Safety Monitoring API - Windows Startup Script

title Industrial Safety API Server

echo.
echo ========================================
echo Industrial Safety Monitoring API
echo Version 1.0.0
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9+ from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Check if dependencies are installed
python -m pip show fastapi >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    python -m pip install -r requirements.txt
)

set "PORT=8000"
if defined API_PORT set "PORT=%API_PORT%"
set "FREE_PORT="
for /l %%P in (%PORT%,1,8010) do (
    netstat -ano | findstr /R /C:":%%P " >nul 2>&1 || (
        set "FREE_PORT=%%P"
        goto :FOUND_PORT
    )
)
if not defined FREE_PORT (
    echo ERROR: Could not find a free port between %PORT% and 8010.
    pause
    exit /b 1
)
:FOUND_PORT
set "PORT=%FREE_PORT%"

echo.
echo Starting server on port %PORT%...
echo.
echo ========================================
echo API is running at: http://127.0.0.1:%PORT%
echo Swagger UI: http://127.0.0.1:%PORT%/docs
echo ReDoc: http://127.0.0.1:%PORT%/redoc
echo ========================================
echo.
echo Press Ctrl+C to stop the server
echo.

python -m uvicorn main:app --reload --host 127.0.0.1 --port %PORT%

pause
