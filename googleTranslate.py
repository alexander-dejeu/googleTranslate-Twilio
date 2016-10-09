"""  PROJECT SPECS + CHALLENGES
1. Create a Python wrapper function for Translate:
    print translate_text) -> translate_text
2. Extended your wrapper function with target language:
    print translate(text, language='XX') -> text in XX language
3. Extended your wrapper function to translate multiple strings:
    print translate([text1, text2, ...], language='XX')
    -> [text1 in XX language, text 2 in XX language, ...]
4. Add Twilio SMS functionality to text the translation to you! """

import httplib2
import urllib
import json
from twilio.rest import TwilioRestClient


GOOGLE_API_KEY = "AIzaSyC0XYY3AWKWKQlQbwm1mzI0-K4_CoFCCrk"
base_url = "https://www.googleapis.com"
path_url = "/language/translate/v2"
param_url = "?key=" + GOOGLE_API_KEY + "&q="
source_lang = "&source=en"

TWILIO_KEY = 'AC6e169e5cc1b4a89d92af1644d112c73d'
TWILIO_SECRET = 'ca03b3be3b074c568dd0739c73671ca5'


def translate_text(text, language):
    text_encoded = urllib.quote_plus(text)
    full_path_url = base_url + path_url
    trans_lang = "&target="+language
    full_url = full_path_url + param_url + text_encoded + source_lang + trans_lang

    http = httplib2.Http()
    response, body = http.request(full_url, "GET")

    try:
        parsed_body = json.loads(body)

    # Bad practice to just "catch" all errors at once...So going to do more
    except json.JSONDecodeError as e:
        print('Issue decoding the json', e)
    except Exception as e:
        print('Translation failed with no json response from Google', e)

    # print 'response:'
    # print 'body type:', type(body)
    # print 'body:', body
    # print 'parsed body' parsed_body
    parsed_body = json.loads(body)
    translatedText2 = parsed_body['data']['translations'][0]['translatedText']
    return translatedText2


def translate_texts(sentences, language):
    translated_list = []
    for sentence in sentences:
        translated_list.append(translate_text(sentence, language))
    return translated_list


tranlated_text = translate_text("Hello whats good fam!", "pt")
client = TwilioRestClient(TWILIO_KEY, TWILIO_SECRET)
client.messages.create(from_='+19783476181', to='+15087367850', body=tranlated_text)
print(translate_texts(["How are you?", "What is your favorite color"], 'de'))
