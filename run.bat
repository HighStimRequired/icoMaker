:: Run the Python script
python icoMaker.py

if %errorlevel% neq 0 (
    echo ERROR: Failed to run icoMaker.py. Please check the script for errors.
    pause
    exit /b
)

echo ========================================
echo Script executed successfully!
echo ========================================
pause