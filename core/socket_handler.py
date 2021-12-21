from fastapi_socketio import SocketManager
from core.server import app

'''
Socket room handling is defined here.
How should our backend communicate with our frontend?
1. Frontend will join NEW_EVENT room to listen for incoming messages announcing events. 
2. Frontend will first read stored events using /events GET, and join rooms defined by id of every event.
3. Frontend gets STATUS_UPDATE, PERIOD_UPDATE, SCORE_UPDATE, REMOVE_EVENT messages in event room.
4. When REMOVE_EVENT message is received frontend will leave the event room.
'''

socket_manager = SocketManager(app=app,
                               async_mode="asgi",
                               cors_allowed_origins="*")


@socket_manager.on('join')
def handle_join_room(sid, room_name, *args, **kwargs):
    print(f'Score tracker {sid} entered room {room_name}.')
    socket_manager.enter_room(sid=sid, room=room_name)


@socket_manager.on('leave')
def handle_leave_room(sid, room_name, *args, **kwargs):
    print(f'Score tracker {sid} left the room {room_name}.')
    socket_manager.leave_room(sid=sid, room=room_name)


# TODO: Create helper functions to send NEW_EVENT, SCORE_UPDATE, PERIOD_UPDATE, STATUS_UPDATE, REMOVE_EVENT
#  and then use them from event_manager.

# def send_new_event_message(event_data):
# def send_score_update(event_data):
