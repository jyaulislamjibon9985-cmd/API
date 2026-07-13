@echo off
REM Smart Industrial Safety Monitoring API - Windows Offline Startup Script

title Industrial Safety API Server (Offline)

echo.
echo ========================================
echo Industrial Safety Monitoring API (Offline)
echo Version 1.0.0
echo ========================================
echo.

REM Ensure Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo This offline startup requires Python 3.9+ installed locally.
    pause
    exit /b 1
)

REM Ensure virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found.
    echo Create it first with an internet connection using:
    echo python -m venv venv
    echo then install dependencies with:
    echo python -m pip install -r requirements.txt
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

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
echo Starting offline server on port %PORT%...
echo.
echo ========================================
echo API is running at: http://127.0.0.1:%PORT%
echo Swagger UI: http://127.0.0.1:%PORT%/docs
echo ReDoc: http://127.0.0.1:%PORT%/redoc
echo ========================================
echo.
echo Press Ctrl+C to stop the server
echo.

python -m uvicorn main:app --host 127.0.0.1 --port %PORT%

pause
