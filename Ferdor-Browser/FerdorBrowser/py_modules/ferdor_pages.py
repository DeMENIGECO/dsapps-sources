import os
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QWidget, QVBoxLayout

# Percorsi dei file di configurazione finti
USER_DIR = os.path.expanduser("~/.FerdorBrowser")
CONFIG_FILE = os.path.join(USER_DIR, "FeConfig.cfg")
SETTINGS_FILE = os.path.join(USER_DIR, "FeSettings.cfg")
os.makedirs(USER_DIR, exist_ok=True)

def render_special_page(url: QUrl):
    page_widget = QWidget()
    layout = QVBoxLayout(page_widget)
    layout.setContentsMargins(0,0,0,0)

    webview = QWebEngineView()
    layout.addWidget(webview)

    # ---------------- fe://home ----------------
    if url.toString() == "fe://home":
        html = """
        <html>
        <head>
        <style>
        body { font-family: Arial; padding: 30px; background: #f4f4f9; color: #333; }
        h1 { color: #222; font-size: 32px; }
        a { text-decoration: none; color: #0066cc; font-weight: bold; }
        a:hover { color: #004499; }
        .card { background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.2); margin-top: 20px; }
        </style>
        </head>
        <body>
            <h1>Ferdor Browser Home</h1>
            <div class="card">
                <p>Benvenuto nella home di Ferdor Browser!</p>
                <p><a href="https://demenigeco.github.io/functions/pk">Vai al sito ufficiale</a></p>
            </div>
        </body>
        </html>
        """
        webview.setHtml(html)
        return page_widget

    # ---------------- fe://config ----------------
    elif url.toString() == "fe://config":
        # Assicuriamoci che il file esista
        if not os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "w") as f:
                f.write("\nprivacy_mode=0\nautocomplete=1\n")

        html = """
        <html>
        <head>
        <style>
        body { font-family: Arial; padding: 30px; background: #1e1e2f; color: #e2e8f0; }
        h2 { color: #f0c674; font-size: 28px; }
        .card { background: #2a2a3c; padding: 20px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.3); margin-top: 20px; }
        label { display: block; margin: 10px 0 5px; }
        select, input[type=checkbox] { margin-bottom: 15px; padding: 5px; border-radius: 4px; }
        </style>
        </head>
        <body>
            <h2>Ferdor Browser Config</h2>
            <div class="card">
                <input type="checkbox" >
                <label>Privacy Mode</label>
                <input type="checkbox">
                <label>Autocomplete</label>
                <input type="checkbox" checked>
            </div>
        </body>
        </html>
        """
        webview.setHtml(html)
        return page_widget

    # ---------------- fe://settings ----------------
    elif url.toString() == "fe://settings":
        if not os.path.exists(SETTINGS_FILE):
            with open(SETTINGS_FILE, "w") as f:
                f.write("homepage=fe://home\nsearch_engine=Google., Defalut\napi_key=ferdorai-8dh8sh-38duw98dh93ur8w9-d8udwudyhwd78rd-du8dh8w9f8e-f98fefud94-uuisihfu\nsafe_mode=1\n")

        html = """
        <html>
        <head>
        <style>
        body { font-family: Arial; padding: 30px; background: #f0f4f8; color: #333; }
        h2 { color: #007acc; font-size: 28px; }
        .card { background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.2); margin-top: 20px; }
        label { display: block; margin: 10px 0 5px; }
        input[type=text], input[type=password], select { width: 100%; padding: 8px; margin-bottom: 15px; border-radius: 4px; }
        input[type=checkbox] { margin-right: 10px; }
        </style>
        </head>
        <body>
            <h2>Ferdor Browser Settings</h2>
            <div class="card">
                <label>Homepage</label>
                <input type="text" value="fe://home">
                <label>Search Engine API Key (Ferdor AI)</label>
                <input type="password" value="ferdorai-8dh8sh-38duw98dh93ur8w9-d8udwudyhwd78rd-du8dh8w9f8e-f98fefud94-uuisihfu">
                <label>Search Engine</label>
                <select>
                    <option selected>Google., Defalut</option>
                    <option>Bing.</option>
                    <option>DuckDuckGo</option>
                </select>
                <label><input type="checkbox" checked> Safe Mode</label>
            </div>
        </body>
        </html>
        """
        webview.setHtml(html)
        return page_widget
    

    # ---------------- fe://addons ----------------
    elif url.toString() == "fe://addons":
        webview.load(QUrl("https://demenigeco.github.io/dsapps/program-pages/ferdor-addons/"))
        return page_widget

    # ---------------- Pagina sconosciuta ----------------
    else:
        html = f"""
        <html>
        <head>
        <style>
        body {{ font-family: Arial; padding: 30px; background: #fff0f0; color: #900; }}
        h1 {{ color: #900; font-size: 28px; }}
        </style>
        </head>
        <body>
            <h1>Pagina sconosciuta</h1>
            <p>{url.toString()}</p>
        </body>
        </html>
        """
        webview.setHtml(html)
        return page_widget