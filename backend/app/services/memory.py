import json
from pathlib import Path
from threading import Lock
from typing import Dict, List

class MemoryStore:
    def __init__(self, filename: str = "data/memory.json"):
        self.path = Path(filename)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.lock = Lock()
        if not self.path.exists():
            self.path.write_text("{}", encoding="utf-8")

    def _load(self) -> Dict[str, List[dict]]:
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save(self, data: Dict[str, List[dict]]) -> None:
        self.path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

    def get_history(self, session_id: str) -> List[dict]:
        with self.lock:
            return self._load().get(session_id, [])

    def append(self, session_id: str, role: str, content: str) -> None:
        with self.lock:
            data = self._load()
            data.setdefault(session_id, []).append(
                {"role": role, "content": content}
            )
            self._save(data)
