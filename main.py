import os
import json
from typing import List, Dict, Any
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class IaintreadingallatEngine:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.memory_file = f"memory_{user_id}.json"
        self.memory = self._load_memory()

    def _load_memory(self) -> Dict[str, Any]:
        if os.path.exists(self.memory_file):
            with open(self.memory_file, "r") as f:
                return json.load(f)
        return {"weak_concepts": [], "mastered_concepts": [], "quiz_history": []}

    def _save_memory(self):
        with open(self.memory_file, "w") as f:
            json.dump(self.memory, f, indent=2)

    def process_notes_and_summarize(self, image_urls: List[str]) -> str:
        """
        1. Extract text/concepts from images (via Vision Model API).
        2. Format output cleanly for iMessage.
        """
        # Placeholder for Vision LLM response processing
        extracted_topics = ["Krebs Cycle Outputs", "Glycolysis Steps", "ATP Yield"]
        
        summary_msg = (
            "📸 **Notes Processed!**\n\n"
            "Key takeaways:\n"
            "• **Glycolysis**: Net 2 ATP + 2 NADH\n"
            "• **Krebs Cycle**: Produces 2 ATP, 6 NADH, 2 FADH2\n"
            "• **Location**: Mitochondrial matrix\n\n"
            "⏰ Reply with a time (e.g., '8 AM') to schedule your daily 3-question quiz!"
        )
        return summary_msg

    def generate_daily_quiz(self) -> List[Dict[str, str]]:
        """
        Prioritizes concepts in weak_concepts memory.
        """
        questions = []
        # Prioritize missed items from self.memory["weak_concepts"]
        if "Krebs Cycle Outputs" in self.memory["weak_concepts"]:
            questions.append({
                "id": "q1",
                "question": "What is the net ATP yield per glucose molecule in the Krebs cycle?",
                "answer": "2 ATP"
            })
        else:
            questions.append({
                "id": "q1",
                "question": "Where does the Krebs cycle take place in eukaryotic cells?",
                "answer": "Mitochondrial matrix"
            })
        return questions

    def record_quiz_result(self, question_id: str, concept: str, is_correct: bool) -> str:
        """
        Updates long-term memory based on performance.
        """
        if not is_correct:
            if concept not in self.memory["weak_concepts"]:
                self.memory["weak_concepts"].append(concept)
            feedback = f"❌ Not quite. Concept '{concept}' added to your review deck for tomorrow!"
        else:
            if concept in self.memory["weak_concepts"]:
                self.memory["weak_concepts"].remove(concept)
                self.memory["mastered_concepts"].append(concept)
            feedback = "🎯 Spot on! Mastered."
            
        self._save_memory()
        return feedback

    def generate_pdf_guide(self, filename: str = "study_guide.pdf") -> str:
        """
        Generates a 1-page PDF summary guide.
        """
        c = canvas.Canvas(filename, pagesize=letter)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 750, "Snap & Quiz — Quick Study Sheet")
        c.setFont("Helvetica", 12)
        c.drawString(100, 720, "1. Glycolysis: Break down of glucose into pyruvate.")
        c.drawString(100, 700, "2. Krebs Cycle: Matrix reaction yielding electron carriers.")
        c.save()
        return filename

if __name__ == "__main__":
    # Quick execution check
    engine = SnapQuizEngine(user_id="student_123")
    print(engine.process_notes_and_summarize([]))
