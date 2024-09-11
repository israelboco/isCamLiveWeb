from app import create_app, socketio
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user


app = create_app()

if __name__ == '__main__':
    socketio.run(app, debug=True)