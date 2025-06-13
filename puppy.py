from flask import Flask, render_template_string
import ssl

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>I Miss You</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            text-align: center;
            background-color: #fff5f5;
            padding: 50px;
        }
        h1 {
            color: #ff6b6b;
            font-size: 3em;
            margin-bottom: 20px;
        }
        .gif-container {
            margin: 30px auto;
            max-width: 500px;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .heart {
            color: red;
            font-size: 1.5em;
            display: inline-block;
            transform-origin: center;
            animation: heartbeat 1.5s infinite;
}
        }
        @keyframes heartbeat {
            0% { transform: scale(1); }
            25% { transform: scale(1.1); }
            50% { transform: scale(1); }
            75% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
    </style>
</head>
<body>
    <h1>I <span class="heart">♥</span> Miss You</h1>
    <p>This cute puppy reminds me of you...</p>
    
    <div class="gif-container">
        <img src="https://media.tenor.com/Eltw6rmCSacAAAAj/pixel-dogs.gif" alt="Cute puppy" style="width:100%">
    </div>
    
    <p></p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('cert.pem', 'key.pem')
    
    app.run(host='0.0.0.0', port=8443, ssl_context=context, debug=True)
