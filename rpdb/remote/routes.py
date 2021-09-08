from flask import request, jsonify
from remote import app


# Counts the number of characters in a message sent to the
# /count path
@app.route('/count', methods=["POST"])
def add_note():

    data = request.get_json(force=True)
    msg = data.get('message')

    import rpdb; rpdb.set_trace()

    if not msg:
         return jsonify({"Error": "No message in Request"}), 400

    no_spaces = msg.strip()
    no_spaces = no_spaces.replace(" ", "")
    num_chars = len(no_spaces)

    # NOTE: The error is in this function. Developer set max to
    # 10, but message doesn't show that
    max = 10
    if num_chars > max:
        return jsonify({"Error": "Message tooooo long!"}), 400

    return jsonify({"Number of Characters:": len(num_chars)}), 200