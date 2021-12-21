from main import socket_manager as sio


@sio.on('join')
async def handle_join(sid, *args, **kwargs):
    await sio.emit('lobby', 'User joined')
    print('connect ', sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


# TODO: Create helper functions to send NEW_EVENT, SCORE_UPDATE, PERIOD_UPDATE, STATUS_UPDATE
#  and then use them from event_manager.
# def send_new_event_message(event_data):
# def send_score_update(home, away):
