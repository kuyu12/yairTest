import google.generativeai as genai
import urllib3

genai.configure(api_key='AIzaSyDaENsGTWKEJU4IdEkUW7dUezsDXHgxrDc')
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("What is the meaning of life?")

print(response)


print("this is america")