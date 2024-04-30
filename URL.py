#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten_url(self, long_url):
        """
        Shorten a long URL by generating a unique hash.
        """
        # Generate MD5 hash of the long URL
        hash_object = hashlib.md5(long_url.encode())
        hash_hex = hash_object.hexdigest()

        # Take the first 8 characters of the hash as the short URL
        short_url = hash_hex[:8]

        # Store the mapping between the short URL and the long URL
        self.url_map[short_url] = long_url

        return short_url

    def expand_url(self, short_url):
        """
        Expand a short URL to its original long URL.
        """
        return self.url_map.get(short_url, "Short URL not found")

# Example usage:
url_shortener = URLShortener()

long_url = "https://www.example.com/some/long/url"
short_url = url_shortener.shorten_url(long_url)
print("Short URL:", short_url)

original_url = url_shortener.expand_url(short_url)
print("Original URL:", original_url)


# In[ ]:




