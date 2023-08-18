from anticaptchaofficial.imagecaptcha import *
import requests
import base64


def find_between(s, start, end):
    return (s.split(start))[1].split(end)[0]


response = requests.get("https://www.chebanca.it/public/conto-premier/aprilo-subito#")
base64str = find_between(response.text, 'data:image/png;base64,', '"')


# save base64 image to a temporary file
with open("tmp.file", "wb") as file:
    file.write(base64.urlsafe_b64decode(base64str))


solver = imagecaptcha()
solver.set_verbose(1)
solver.set_key("53e9ab51ge7111eebb8f7d7282d6bb")
captcha_text = solver.solve_and_return_solution("tmp.file")

if captcha_text != 0:
    print("captcha text "+captcha_text)
elif 'ERROR_ZERO_BALANCE' in str(solver.error_code):
    print("sem saldo")
else:
    print("task finished with error "+solver.error_code)