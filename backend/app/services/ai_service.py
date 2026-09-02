import os
from typing import List, Dict

class AIService:
    def __init__(self):
        self.demo_mode = os.getenv("DEMO_MODE", "false").lower() == "true"
        self.api_key = os.getenv("AI_API_KEY")

    async def generate_response(
        self, conversation_id: str, message: str, history: List[Dict], personality: str
    ) -> Dict:
        if self.demo_mode:
            return {
                "generated_response": f"This is a demo response. You asked: '{message}'. Our system is in DEMO_MODE.",
                "confidence": 0.95
            }

        # Real AI implementation would go here (e.g., using OpenAI API)
        return {
            "generated_response": "Real AI generation not yet implemented.",
            "confidence": 0.0
        }
