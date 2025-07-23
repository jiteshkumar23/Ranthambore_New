import pychromedevtools

chrome = pychromedevtools.ChromeInterface()
chrome.Page.navigate(url="https://example.com", _timeout=5)
chrome.Runtime.evaluate(expression="alert('Hello from PyCharm!')")