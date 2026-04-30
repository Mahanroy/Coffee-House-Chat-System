from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_socketio import SocketIO, join_room, leave_room, emit
from datetime import datetime
import secrets
import socket

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
socketio = SocketIO(app, cors_allowed_origins="*")

# In-memory storage for rooms
# Format: {'room_name': {'password': 'pass', 'members': 0}}
rooms = {}


# Get local IP address
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Doesn't need to actually connect
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        action = request.form.get('action')
        room = request.form.get('room')
        password = request.form.get('password')

        if not name:
            flash("Please enter a name.", "error")
            return render_template('index.html', name=name, room=room)

        if action == "create":
            if not room:
                flash("Please enter a room name.", "error")
                return render_template('index.html', name=name, room=room)

            if room in rooms:
                flash("Room already exists. Try joining instead.", "error")
                return render_template('index.html', name=name, room=room)

            rooms[room] = {
                'password': password,
                'members': 0
            }

            session['room'] = room
            session['name'] = name
            return redirect(url_for('chat'))

        elif action == "join":
            if not room:
                flash("Please enter a room name.", "error")
                return render_template('index.html', name=name, room=room)

            if room not in rooms:
                flash("Room does not exist.", "error")
                return render_template('index.html', name=name, room=room)

            room_data = rooms[room]

            # Verify password if one is set
            if room_data['password'] and room_data['password'] != password:
                flash("Incorrect password.", "error")
                return render_template('index.html', name=name, room=room)

            session['room'] = room
            session['name'] = name
            return redirect(url_for('chat'))

    return render_template('index.html')


@app.route('/chat')
def chat():
    room = session.get('room')
    name = session.get('name')

    if room is None or name is None or room not in rooms:
        return redirect(url_for('index'))

    return render_template('chat.html', room=room, name=name)


@socketio.on('connect')
def connect(auth):
    room = session.get('room')
    name = session.get('name')

    if not room or not name:
        return

    if room not in rooms:
        leave_room(room)
        return

    join_room(room)

    emit(
        'message',
        {
            'name': 'System',
            'message': f'{name} has entered the room.',
            'timestamp': datetime.now().strftime('%H:%M')
        },
        to=room
    )

    rooms[room]['members'] += 1

    emit(
        'room_info',
        {
            'members': rooms[room]['members'],
            'room': room
        },
        to=room
    )


@socketio.on('disconnect')
def disconnect():
    room = session.get('room')
    name = session.get('name')

    leave_room(room)

    if room in rooms:
        rooms[room]['members'] -= 1

        if rooms[room]['members'] <= 0:
            del rooms[room]
        else:
            emit(
                'message',
                {
                    'name': 'System',
                    'message': f'{name} has left the room.',
                    'timestamp': datetime.now().strftime('%H:%M')
                },
                to=room
            )

            emit(
                'room_info',
                {
                    'members': rooms[room]['members'],
                    'room': room
                },
                to=room
            )


@socketio.on('message')
def message(data):
    room = session.get('room')

    if room not in rooms:
        return

    content = data.get('data')

    emit(
        'message',
        {
            'name': session.get('name'),
            'message': content,
            'timestamp': datetime.now().strftime('%H:%M')
        },
        to=room
    )


if __name__ == '__main__':
    local_ip = get_local_ip()

    print(f"Flask Chat Server running → http://localhost:5000")
    print(f"Access from same Wi-Fi → http://{local_ip}:5000")

    socketio.run(
        app,
        host='0.0.0.0',
        port=5000,
        debug=True
    )