rem comments in bat file using rem

rem chrome
pytest -s -v -m "sanity" --html=./Reports/report_chrome.html testCases/ --browser chrome
pytest -s -v -m "sanity and regression" --html=./Reports/report_chrome.html testCases/ --browser chrome
pytest -s -v -m "sanity or regression" --html=./Reports/report_chrome.html testCases/ --browser chrome
pytest -s -v -m "regression" --html=./Reports/report_chrome.html testCases/ --browser chrome

rem Firefox
pytest -s -v -m "sanity" --html=./Reports/report_firefox.html testCases/ --browser firefox
pytest -s -v -m "sanity and regression" --html=./Reports/report_firefox.html testCases/ --browser firefox
pytest -s -v -m "sanity or regression" --html=./Reports/report_firefox.html testCases/ --browser firefox
pytest -s -v -m "regression" --html=./Reports/report_firefox.html testCases/ --browser firefox

rem Edge
pytest -s -v -m "sanity" --html=./Reports/report_edge.html testCases/ --browser edge
pytest -s -v -m "sanity and regression" --html=./Reports/report_edge.html testCases/ --browser edge
pytest -s -v -m "sanity or regression" --html=./Reports/report_edge.html testCases/ --browser edge
pytest -s -v -m "regression" --html=./Reports/report_edge.html testCases/ --browser edge