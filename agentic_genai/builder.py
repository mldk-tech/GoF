class PromptBuilder:
    def __init__(self):
        self.parts = []

    def add(self, text: str) -> "PromptBuilder":
        self.parts.append(text)
        return self

    def build(self) -> str:
        return "\n".join(self.parts)
