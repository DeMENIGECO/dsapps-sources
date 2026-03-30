from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QTextEdit, QPushButton
from PySide6.QtCore import Qt
import requests
from bs4 import BeautifulSoup

class MiniAI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("✨ Ferdor AI")
        self.resize(500, 400)

        layout = QVBoxLayout(self)
        self.query_input = QLineEdit(self)
        self.query_input.setPlaceholderText("Scrivi qui la tua domanda...")
        layout.addWidget(self.query_input)

        self.result_area = QTextEdit(self)
        self.result_area.setReadOnly(True)
        layout.addWidget(self.result_area)

        search_btn = QPushButton("Cerca", self)
        search_btn.clicked.connect(self.search)
        layout.addWidget(search_btn)

    def search(self):
        query = self.query_input.text().strip()
        if not query:
            return

        # Cerca sul web con Google (semplice fetch)
        try:
            url = f"https://www.google.com/search?q={query.replace(' ','+')}"
            headers = {"User-Agent": "Mozilla/5.0"}
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.text, "html.parser")
            results = []

            for g in soup.select(".tF2Cxc"):
                title = g.select_one(".DKV0Md").get_text() if g.select_one(".DKV0Md") else ""
                link = g.select_one(".yuRUbf a")["href"] if g.select_one(".yuRUbf a") else ""
                snippet = g.select_one(".VwiC3b").get_text() if g.select_one(".VwiC3b") else ""
                results.append(f"{title}\n{link}\n{snippet}\n\n")
            
            self.result_area.setPlainText("\n".join(results[:5]))
        except Exception as e:
            self.result_area.setPlainText(f"Errore nella ricerca: {e}")