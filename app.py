from flask import Flask
from flask import request
import subprocess


app = Flask('pin')
ip_whitelist = ['192.168.50.232']

def valid_ip():
    client = request.remote_addr
    if client in ip_whitelist:
        return True
    else:
        return False


@app.route('/<id>')
def pin_this(id):
    if valid_ip():
        try:
            done = subprocess.run(["ipfs", "pin", "add", id], check=True)
            if not done:
                return "Check file hash"
        except:
            return "An error occurred while trying to pin."

        return 'Successfully pinned'
    else:
        return """<title>404 Not Found</title>
               <h1>Not Found</h1>
               <p>The requested URL was not found on the server.
               If you entered the URL manually please check your
               spelling and try again.</p>""", 404


if __name__ == '__main__':
    app.run(host="0.0.0.0")
