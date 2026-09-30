from .memory import MemoryStore

class Agent:
    def __init__(self, memory: MemoryStore):
        self.memory = memory

    def process(self, session_id: str, message: str):
        history = self.memory.get_history(session_id)

        previous_context = ""
        if history:
            first_user = next(
                (item["content"] for item in history if item.get("role") == "user"),
                None
            )
            if first_user:
                previous_context = (
                    f" I remember your first message was: '{first_user}'."
                )

        reply = f"Received: '{message}'.{previous_context}"

        self.memory.append(session_id, "user", message)
        self.memory.append(session_id, "assistant", reply)

        return reply, len(self.memory.get_history(session_id))
