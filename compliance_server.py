from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory log of compliance reports (replace with database if needed)
compliance_logs = []

@app.route('/api/report', methods=['POST'])
def receive_report():
    data = request.json
    if not data:
        return jsonify({'error': 'Invalid request'}), 400

    # Add a timestamp to the log entry
    data['received_at'] = datetime.utcnow().isoformat()
    
    # Store the log entry (in-memory for now)
    compliance_logs.append(data)
    
    return jsonify({'status': 'Report received'}), 200

@app.route('/logs', methods=['GET'])
def get_logs():
    # Return the compliance logs (in-memory)
    return jsonify(compliance_logs), 200

if __name__ == '__main__':
    app.run(debug=True)

