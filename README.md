# (NinjaV3) Ninja reCAPTCHA V3 Bypass


#### Author: 70L0-0J0

# Description

The Ninja reCAPTCHA V3 Bypass module provides an automated solution for interacting with Google's reCAPTCHA V3 system. Designed with flexibility in mind, this tool allows you to bypass reCAPTCHA validation by obtaining the necessary tokens via both synchronous and asynchronous methods. It simplifies the process of token extraction by enabling the configuration of request parameters either manually or by parsing them directly from a URL.

Whether you are working with proxy servers, customizing user-agent strings, or needing to efficiently handle reCAPTCHA requests in high-performance environments, this module is designed to meet a variety of use cases. It integrates easily with any Python project requiring reCAPTCHA bypass functionality and supports both blocking and non-blocking execution modes.

This tool is particularly valuable for developers looking to automate reCAPTCHA V3 interactions in environments where manual verification is impractical or needs to be circumvented.

# Features

 1. Synchronous and Asynchronous Support: Provides both blocking (synchronous) and non-blocking (asynchronous) methods to retrieve reCAPTCHA tokens, allowing flexibility in various programming environments.

 2. URL Parameter Extraction: Automatically extracts key parameters such as ar, k, co, hl, and cb from a URL, simplifying the token request setup.

 3. Proxy Support: Easily integrate with proxy servers by passing proxy configurations, enabling anonymous or region-specific requests.

 4. Customizable User-Agent: Allows custom user-agent strings to simulate requests from various browsers or devices, improving versatility for different testing and automation scenarios.

 5. Retry Mechanism: Includes a built-in retry mechanism for handling potential network failures, ensuring reliability when obtaining tokens.

 6. HTML Parsing: Leverages BeautifulSoup for HTML parsing to accurately retrieve the initial reCAPTCHA tokens from the server response.

 7. Easy Integration: Compatible with any Python-based project, allowing seamless integration into scripts or larger applications that need to bypass reCAPTCHA V3.

 8. Lightweight and Efficient: The module is designed to be lightweight, ensuring minimal overhead while maintaining efficient performance for automated tasks.

# Installation

```bash
pip install RecaptchaV3Ninja
```
# Usage Examples

## 1: Sync reCAPTCHA V3 Token Retrieval Using URL with Query Parameters

This example demonstrates how to use the Ninja reCAPTCHA V3 Bypass module to retrieve a reCAPTCHA token by initializing with a URL that contains all necessary query parameters for the reCAPTCHA request.


```python
# Sync and url example

from recaptchav3ninja import Ninja

# URL containing query parameters for reCAPTCHA
# This URL includes pre-defined values for 'ar', 'k', 'co', 'hl', 'v', 'size', and 'cb'.
url = "https://www.example.com/recaptcha?ar=1&k=your_site_key&co=US&hl=en&v=v_value&size=invisible&cb=callback_value"

# Initialize the 'Add' class with the URL.
# The class will automatically extract and apply the parameters from the provided URL.
add_instance = Ninja.Sync()
data = add_instance.Add(
    url=url
)

# Run the sync method to send the request and retrieve the reCAPTCHA token.
# The function will combine the initial and verification tokens to return the final reCAPTCHA token.
token = add_instance.run(data)

# Output the obtained reCAPTCHA token to the console.
print("reCAPTCHA token:", token)

```
## 2: Async reCAPTCHA V3 Token Retrieval Using URL with Query Parameters

This example demonstrates how to use the asynchronous methods of the Ninja reCAPTCHA V3 Bypass module to retrieve a reCAPTCHA token by initializing with a URL that contains all necessary query parameters for the reCAPTCHA request.

```python
import asyncio
from recaptchav3ninja import Ninja

async def main():
    # URL containing query parameters for reCAPTCHA
    # This URL includes pre-defined values for 'ar', 'k', 'co', 'hl', 'v', 'size', and 'cb'.
    url = "https://www.example.com/recaptcha?ar=1&k=your_site_key&co=US&hl=en&v=v_value&size=invisible&cb=callback_value"

    # Initialize the 'Add' class within the 'Ninja.Async' class.
    # This prepares the instance for asynchronous reCAPTCHA token retrieval.
    add_instance = Ninja.Async()
    
    # Create an 'Add' instance with the specified URL.
    # The 'Add' class will extract and apply the parameters from the provided URL.
    dt = add_instance.Add(url=url)
    
    # Run the asynchronous method 'run' to send the request and retrieve the reCAPTCHA token.
    # This function handles the reCAPTCHA validation process asynchronously and returns the final token.
    token = await add_instance.run(dt)
    
    # Output the obtained reCAPTCHA token to the console.
    print("reCAPTCHA token:", token)

# Execute the asynchronous main function.
asyncio.run(main())

```
## 3: Using Custom Parameters for Synchronous reCAPTCHA V3 Token Retrieval

This example demonstrates how to use the synchronous methods of the Ninja reCAPTCHA V3 Bypass module to retrieve a reCAPTCHA token by initializing with specific parameters. This is useful when you need to specify each parameter individually rather than extracting them from a URL.
 
```python
from recaptchav3ninja import Ninja

add_instance = Ninja.Sync()
data = add_instance.Add(
    ar=1, 
    k="your_site_key", 
    co="US", 
    hl="en", 
    v="v_value", 
    cb="callback_value"
)
# Run the sync method to obtain the reCAPTCHA token
token = add_instance.run(data)

# Print the resulting token
print("reCAPTCHA token:", token)

```
## 4: Using Custom Parameters for Asynchronous reCAPTCHA V3 Token Retrieval

This example demonstrates how to use the Asynchronous methods of the Ninja reCAPTCHA V3 Bypass module to retrieve a reCAPTCHA token by initializing with specific parameters. This is useful when you need to specify each parameter individually rather than extracting them from a URL.

```python
import asyncio
from recaptchav3ninja import Ninja

async def main():

    add_instance = Ninja.Async()
    
    # Create an 'Add' instance with the specified parameters.
    # The 'Add' class will extract and apply the parameters provided.
    dt = add_instance.Add(ar='Your_ar', k='your_k', co='your_co',  hl='your_hl',v='your_v', size='your size (invisible)', cb='your_cb')
    
    # Run the asynchronous method 'run' to send the request and retrieve the reCAPTCHA token.
    # This function handles the reCAPTCHA validation process asynchronously and returns the final token.
    token = await add_instance.run(dt)
    
    # Output the obtained reCAPTCHA token to the console.
    print("reCAPTCHA token:", token)

# Execute the asynchronous main function.
asyncio.run(main())

```
# License

MIT License

Copyright (c) 2024 70L0-0j0

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
