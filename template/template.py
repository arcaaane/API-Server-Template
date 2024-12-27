from flask import Flask, request

# server setup
YOUR_SERVER_NAME = Flask(__name__) # replace "YOUR_SERVER_NAME" with name of choice
on_login_message = "Replace with the message you want to see when you start the server"
version = "version number here"
port_number = 5000 # port number, 5000 is default
host_ip = 0.0.0.0 # change to IP if you plan on doing port-forwarding
# end server setup

@YOUR_SERVER_NAME.route("/")
def home():
    return on_login_message
    
if __name__ == "__main__":
    print(f"Booting {YOUR_SERVER_NAME} on port {port_number")
    YOUR_SERVER_NAME.run(host=host_ip, port=port_number)
    