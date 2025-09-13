from flask import Flask, request, redirect

app = Flask(__name__)

# В реальном проекте лучше хранить коды в базе или Redis
user_codes = {}

@app.route('/oauth2callback')
def oauth2callback():
    code = request.args.get('code')
    state = request.args.get('state')  # state = user_id
    if code and state:
        user_codes[state] = code
        return "✅ Авторизация прошла успешно! Вернитесь в Telegram-бот."
    return "Ошибка авторизации."

def get_code_for_user(user_id):
    return user_codes.pop(str(user_id), None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)