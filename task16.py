"""
b'\xff\xfef\x00e\x00r\x00m\x00a\x00' bu bytes datasını UTF-16 ilə decode edib, ekranda göstərin.
"""

data = b'\xff\xfef\x00e\x00r\x00m\x00a\x00'
decoded_data = data.decode('utf-16')
print(decoded_data)
