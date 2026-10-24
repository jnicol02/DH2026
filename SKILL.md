---
name: snap-quiz
description: Converts photos of study notes or whiteboards into study guides and interactive daily practice quizzes using a Python execution pipeline.
---

# Snap & Quiz (Python Backend)

Snap & Quiz turns photos of class notes into structured summaries, daily quiz check-ins, and downloadable 1-page PDF study sheets.

## Setup & Execution
- **Runtime:** Python 3.10+
- **Entry point:** `main.py`
- **Dependencies:** Install via `pip install -r requirements.txt`

## Workflow

### 1. Photo Ingestion & Summarization
- Trigger `main.py` when image attachments are received.
- Parse image content, save extracted concepts to `memory_<user_id>.json`, and send an iMessage-formatted summary.

### 2. Scheduled Daily Quiz
- At the student's chosen time, execute `generate_daily_quiz()`.
- Load weak concepts from persistent memory JSON first (Spaced Repetition).
- Deliver 3 short questions sequentially over SMS.

### 3. Memory & Spaced Repetition Updates
- Process student responses with `record_quiz_result()`.
- If incorrect: Add concept to `weak_concepts`.
- If correct: Promote to `mastered_concepts`.

### 4. PDF Generation (Optional Command)
- When user texts "PDF" or "Study Guide", run `generate_pdf_guide()` and return the generated 1-page PDF document.

## Formatting Rules
- Keep output concise for mobile (iMessage).
- Use clear visual anchors (e.g., 📸, 🎯, ⏰, 📄).
- Zero setup or OAuth login required for the student.
