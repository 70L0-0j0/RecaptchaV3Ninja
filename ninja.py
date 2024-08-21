import aiohttp
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, urlencode
import ssl
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Functions:
    @staticmethod
    def _url_ext(url: str = str) -> str:
        """
        Extracts query parameters from a given URL and returns them as a dictionary.

        Args:
            url (str): The URL from which to extract the parameters.

        Returns:
            dict: A dictionary with query parameters and their values.
        """
        parsed_url = urlparse(url)    
        query_params = parse_qs(parsed_url.query)    
        params_dict = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}    
        return params_dict
    

    """ Sync Handler for get captcha Token """
    class SyncV3:
        """
    Class to handle interactions with Google's reCAPTCHA service.

    Attributes:
        url (str): Base URL for the request.
        params (dict): Parameters for the request.
        headers (dict): HTTP headers for the request.
        proxies (dict, optional): Proxy configuration for the request.

    Methods:
        _get_i_token(): Retrieves the initial token from the HTML response.
        _get_v_token(initial_token): Retrieves the verification token using the initial token.
        _get_token(): Combines the initial token and verification token to obtain the final token.
    """
        def __init__(self, ar: int = None, k: str = None, co: str = None, hl: str = "en", v: str = None, size: str = "invisible", cb: str = None, url: str = None, proxy=None, user_agent: str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Avast/126.0.0.0'):
            """
        Initializes the SyncV3 instance.

        Args:
            ar (int, optional): Parameter 'ar' for the request.
            k (str, optional): Parameter 'k' for the request.
            co (str, optional): Parameter 'co' for the request.
            hl (str, optional): Parameter 'hl' for the request (default is "en").
            v (str, optional): Parameter 'v' for the request.
            size (str, optional): Parameter 'size' for the request (default is "invisible").
            cb (str, optional): Parameter 'cb' for the request.
            url (str, optional): URL to extract parameters from (overrides individual parameters).
            proxy (dict, optional): Proxy configuration for the request.
            user_agent (str, optional): User-Agent header for the request (default is a common browser User-Agent).
        """
            self.url = "https://www.google.com/recaptcha/api2/anchor"

            params = Functions._url_ext(url) if url else None
            self.params = {
            "ar": params.get("ar") if params else ar,
            "k": params.get("k") if params else k,
            "co": params.get("co") if params else co,
            "hl": params.get("hl") if params else hl,
            "v": params.get("v") if params else v,
            "size": params.get("size") if params else size,
            "cb": params.get("cb") if params else cb
        }
            self.headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.6",
                "cache-control": "no-cache",
                "dnt": "1",
                "pragma": "no-cache",
                "priority": "u=0, i",
                "sec-ch-ua": "Not)A;Brand\";v=\"99\", \"Brave\";v=\"127\", \"Chromium\";v=\"127",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "Windows",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "sec-gpc": "1",
                "upgrade-insecure-requests": "1",
                "user-agent": user_agent
            }        
            self.proxies = proxy

        def _get_i_token(self):
            """
            Retrieves the initial token from the HTML response by sending a GET request.

            Returns:
                str: The initial token if found; otherwise, None.
            """
            
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    r = requests.get(self.url, params=self.params, headers=self.headers, proxies=self.proxies, verify=False)
                    if r.status_code == 200:
                        token_input = BeautifulSoup(r.text, 'html.parser').find('input', {'id': 'recaptcha-token'})
                        return token_input['value'] if token_input and token_input.get('value') else attempt + 1
                except requests.RequestException as e:
                    print(f"Attempt {attempt + 1} failed with error: {e}")
                except:
                    attempt += 1
            return None

        def _get_v_token(self, initial_token):
            """
            Retrieves the verification token using the initial token by sending a POST request.

            Args:
                initial_token (str): The initial token obtained from the HTML response.

            Returns:
                str: The verification token response if successful; otherwise, None.
            """
            post_url = "https://www.google.com/recaptcha/api2/reload"
            post_params = {
                "k": self.params['k']
            }
            post_data = {
                "v": self.params['v'],
                "reason": "q",
                "c": initial_token,
                "k": self.params['k'],
                "co": self.params['co'],
                "hl": self.params['hl']
            }
            post_headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.7",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded",
                "dnt": "1",
                "pragma": "no-cache",
                "priority": "u=1, i",
                "sec-ch-ua": "Not)A;Brand\";v=\"99\", \"Brave\";v=\"127\", \"Chromium\";v=\"127",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "Windows",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "sec-gpc": "1",
                "user-agent": self.headers['user-agent']
            }

            max_retries = 3
            for attempt in range(max_retries):
                try:
                    r = requests.post(post_url, params=post_params, data=post_data, headers=post_headers, proxies=self.proxies, verify=False)
                    return r.text if r.status_code == 200 else attempt + 1
                except requests.RequestException as e:
                    attempt += 1
            return None


        def _get_token(self):
            """
            Obtains the final token by combining the initial and verification tokens.

            Returns:
                str: The final token if successful; otherwise, None.
            """
            initial_token = self._get_i_token()
            if initial_token:
                verification_token = self._get_v_token(initial_token)
                return verification_token.split('rresp')[1].split('"')[2] if verification_token else None
            return None

    """ Async Handler for captcha Token """
    class AsyncV3:
        """
        Asynchronous class to handle interactions with Google's reCAPTCHA service.

        Attributes:
            url (str): Base URL for the request.
            params (dict): Parameters for the request.
            headers (dict): HTTP headers for the request.
            proxies (dict, optional): Proxy configuration for the request.

        Methods:
            _get_i_token(): Asynchronously retrieves the initial token from the HTML response.
            _get_v_token(initial_token): Asynchronously retrieves the verification token using the initial token.
            _get_token(): Combines the initial token and verification token to obtain the final token asynchronously.
        """
        def __init__(self, ar: int = None, k: str = None, co: str = None, hl: str = "en", v: str = None, size: str = "invisible", cb: str = None, url: str = None, proxy=None, user_agent: str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Avast/126.0.0.0'):
            """
            Initializes the AsyncV3 instance.

            Args:
                ar (int, optional): Parameter 'ar' for the request.
                k (str, optional): Parameter 'k' for the request.
                co (str, optional): Parameter 'co' for the request.
                hl (str, optional): Parameter 'hl' for the request (default is "en").
                v (str, optional): Parameter 'v' for the request.
                size (str, optional): Parameter 'size' for the request (default is "invisible").
                cb (str, optional): Parameter 'cb' for the request.
                url (str, optional): URL to extract parameters from (overrides individual parameters).
                proxy (dict, optional): Proxy configuration for the request.
                user_agent (str, optional): User-Agent header for the request (default is a common browser User-Agent).
            """
            self.url = "https://www.google.com/recaptcha/api2/anchor"
            
            params = Functions._url_ext(url) if url else None
            self.params = {
                "ar": params.get("ar") if params else ar,
                "k": params.get("k") if params else k,
                "co": params.get("co") if params else co,
                "hl": params.get("hl") if params else hl,
                "v": params.get("v") if params else v,
                "size": params.get("size") if params else size,
                "cb": params.get("cb") if params else cb
            }
            
            self.headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.6",
                "cache-control": "no-cache",
                "dnt": "1",
                "pragma": "no-cache",
                "priority": "u=0, i",
                "sec-ch-ua": "Not)A;Brand\";v=\"99\", \"Brave\";v=\"127\", \"Chromium\";v=\"127",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "Windows",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "sec-gpc": "1",
                "upgrade-insecure-requests": "1",
                "user-agent": user_agent
            }
            self.proxies = proxy

        async def _get_i_token(self, session):
            """
            Asynchronously retrieves the initial token from the HTML response by sending a GET request.

            Returns:
                str: The initial token if found; otherwise, None.
            """
            async with session.get(self.url, params=self.params, headers=self.headers, proxy=self.proxies) as response:
                if response.status == 200:
                    text = await response.text()
                    soup = BeautifulSoup(text, 'html.parser')
                    token_input = soup.find('input', {'id': 'recaptcha-token'})
                    if token_input and token_input.get('value'):
                        return token_input['value']
            return None

        async def _get_v_token(self, initial_token, session):
            """
            Asynchronously retrieves the verification token using the initial token by sending a POST request.

            Args:
                initial_token (str): The initial token obtained from the HTML response.

            Returns:
                str: The verification token response if successful; otherwise, None.
            """
            post_url = "https://www.google.com/recaptcha/api2/reload"
            post_params = {
                "k": self.params['k']
            }
            post_data = {
                "v": self.params['v'],
                "reason": "q",
                "c": initial_token,
                "k": self.params['k'],
                "co": self.params['co'],
                "hl": self.params['hl']
            }
            post_headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.7",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded",
                "dnt": "1",
                "pragma": "no-cache",
                "priority": "u=1, i",
                "sec-ch-ua": "Not)A;Brand\";v=\"99\", \"Brave\";v=\"127\", \"Chromium\";v=\"127",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "Windows",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "sec-gpc": "1",
                "user-agent": self.headers['user-agent']
            }
            async with session.post(post_url, params=post_params, data=post_data, headers=post_headers, proxy=self.proxies) as response:
                if response.status == 200:
                    return await response.text()
            return None

        async def _get_token(self):
            """
            Obtains the final token by combining the initial and verification tokens asynchronously.

            Returns:
                str: The final token if successful; otherwise, None.
            """
            
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE

            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
                
                initial_token = await self._get_i_token(session)
                if initial_token:
                    verification_token = await self._get_v_token(initial_token, session)
                    return verification_token.split('rresp')[1].split('"')[2] if verification_token else None
            return None
