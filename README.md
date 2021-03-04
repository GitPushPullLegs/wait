# wait

A library to wait for websites to load, files to download, a method to return, etc...

## Installation:
`pip install git+https://github.com/GitPushPullLegs/wait.git`

## Quickstart:
***Waiting for any function to return***
```python
from wait import Wait
from random import randrange

def function_that_needs_to_return():
    if randrange(10) == 2:
        return "It's 2!"

result = Wait(timeout=60, poll_frequency=1.5).until(function_that_needs_to_return) 
print(result)
```

***Waiting for a download to complete***
```python
from wait import BrowserWait
from selenium import webdriver

# A random selenium chrome driver.
driver_path = 'path_to_chrome_driver'
driver = webdriver.Chrome(executable_path=driver_path)

file_path = BrowserWait(driver=driver).until_file_downloaded()

print(file_path)  # The file path to the downloaded file.
```