import sys

class Logger():
    def __init__(self, text, resp):
        self.text = text
        self.resp = resp
        
    def log_default(self):
        sys.stdout.write(f"[*] {self.text} -> {self.resp}\n")
        sys.stdout.flush()
        
    def log_success(self):
        sys.stdout.write(f"[$] {self.text} -> {self.resp}\n")
        sys.stdout.flush()
        
    def log_error(self):
        sys.stdout.write(f"[!] {self.text} -> {self.resp}\n")
        sys.stdout.flush()