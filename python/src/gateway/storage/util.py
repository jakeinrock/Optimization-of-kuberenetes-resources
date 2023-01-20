import pika, json

def upload(f, fs, channel, access):
    """Upoading movie fle to the storage db.
    When process is finished successfully, sends message with fileID to the video queue.
    """
    try:
        fid = fs.put(f)
    except Exception as err:
        print('#1', err)
        return("Internal server error", 500)

    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"],
    }

    try:
        channel.basic_publish(
            exchange="",
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
    except Exception as err:
        print('#2', err)
        fs.delete(fid)
        return("Internal server error", 500)
