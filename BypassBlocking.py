import requests

proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
}

url = "https://www.ralphlauren.nl/en/men/clothing/hoodies-sweatshirts/10204?webcat=men%7Cclothing%7Cmen-clothing-hoodies-sweatshirts"
response = requests.get(url, proxies=proxies)
#In this example, I am using a dictionary to define the proxies for http and https protocols. The IP address 10.10.1.10 is an example of a proxy server and the 3128 and 1080 ports are used for http and https respectively.

