import os
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        client = request.form.get("client")
        issue = request.form.get("issue")
        priority = request.form.get("priority")

        # Format the ticket
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = (
            f"=== Support Ticket ===\n"
            f"Client   : {client}\n"
            f"Issue    : {issue}\n"
            f"Priority : {priority}\n"
            f"Logged At: {timestamp}\n\n"
        )

        # Save the ticket
        filename = datetime.now().strftime("ticket_log_%Y%m%d.txt")
        filepath = os.path.join("output", "logs", filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, "a") as f:
            f.write(log_entry)

        return render_template("index.html", success=True, log=log_entry)

    return render_template("index.html", success=False)
    
@app.route("/tickets")
def view_tickets():
    log_dir = os.path.join("output", "logs")
    all_logs = []

    if os.path.exists(log_dir):
        for filename in sorted(os.listdir(log_dir)):
            filepath = os.path.join(log_dir, filename)
            with open(filepath, "r") as f:
                content = f.read()
                all_logs.append((filename, content))

    return render_template("tickets.html", logs=all_logs)

if __name__ == "__main__":
    app.run(debug=True)
