import hashlib
from pathlib import Path

BANNER_PATH = "assets/banner.txt"

def compute_file_hash(file_path, block_size=65536):
    """Compute SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for block in iter(lambda: f.read(block_size), b""):
            sha256.update(block)
    return sha256.hexdigest()

def load_banner():
    """Load ASCII banner from file."""
    try:
        path = Path(BANNER_PATH)
        if path.exists():
            return path.read_text()
        return "== Directory Snapshot Tool =="
    except Exception:
        return "== Directory Snapshot Tool =="
