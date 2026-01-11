from flask import Flask, request, jsonify
import json
import sys

app = Flask(__name__)

def log_request():
    log_data = {
        "method": request.method,
        "path": request.path,
        "full_path": request.full_path,
        "remote_addr": request.remote_addr,
        "headers": dict(request.headers),
        "query_params": request.args.to_dict(flat=False),
        "body_raw": request.get_data(as_text=True),
        "json_body": None,
        "form_body": request.form.to_dict(flat=False)
    }

    # Try to parse JSON body safely
    try:
        log_data["json_body"] = request.get_json(silent=True)
    except Exception:
        pass

    print("==== INCOMING REQUEST ====")
    print(json.dumps(log_data, indent=2))
    print("==========================")
    sys.stdout.flush()


# Catch ALL paths, ALL methods
@app.route("/", defaults={"path": ""}, methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"])
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"])
def catch_all(path):
    log_request()

    return jsonify({
        "status": "ok",
        "message": "Request received and logged",
        "path": request.path
    }), 200


if __name__ == "__main__":
    # Render provides PORT automatically
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
