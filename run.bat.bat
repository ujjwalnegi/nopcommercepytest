@echo off 
call venv\scripts\activate
pytest -s -v -m "sanity" --html .\reports\test_report_chrome.html --browser chrome
pause