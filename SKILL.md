---
name: snap-quiz
description: Turns photos of class notes, whiteboards or slides into clean notes and a daily 3-question pop quiz that brings back what the student got wrong. Use whenever a student sends a photo of notes, lecture slides or a whiteboard, even with no text, says "quiz me on this", has an exam coming and a pile of note photos, or wants daily practice questions. Unlike a study plan, this builds questions from the student's own notes and repeats missed ones.
---

# Snap & Quiz

Snap notes, check the concepts, quiz, come back to the weak spots. This Skill uses only Cubbie's built-in
capabilities. It has no scripts and needs no sign-in.

## When to use

- "Here are my bio notes, quiz me" (with one or more photos)
- "Midterm Thursday, can you turn these whiteboard pics into practice questions?"
- "Quiz me every morning on my CHEM notes"
- "Make me a study sheet from these"
- A photo of lecture slides, notes or a whiteboard sent with no text at all
- Notes pasted as text, or a PDF of notes

When several photos arrive one after another, treat them as one set of notes and reply once.

Do not use it to answer graded homework, take-home exams or quizzes the student is currently taking. If the photos look
like a graded assignment, offer to explain the concepts and quiz them on similar practice questions instead.

## 1. Read the notes

1. Read every photo, PDF, document or pasted text the student sent with Cubbie's ability to read files and images.
   If a photo is too blurry to read, say which one ("Photo 2 is too blurry") and ask for a clearer shot; keep going
   with the rest. Never guess what an unreadable photo says.
2. Name the course or topic from the content and keep going without waiting ("📸 Looks like OOAD + Bloom's
   Taxonomy."). If the student corrects it, use their name for it from then on.
3. Pull out 5 to 15 key concepts: a term, a definition, a formula, a process step or a date. If the notes have fewer,
   use what is there; do not pad. Use only what is in the notes; do not add facts that are not there. If something on
   the page seems wrong, flag it rather than fix it. If the student asks for extra background, say which parts are
   not from their notes.

## 2. Send the clean notes

Text a short summary: the topic, then up to 5 key concepts as a dash list, and invite the student to correct anything
read wrong. If there are more than 5 concepts, make a one-page PDF study sheet (concepts, definitions, 3 sample
questions), send it, and say it's there. The student never has to open the PDF to start a quiz.

## 3. Remember the concepts

Save to Cubbie's memory, under "Snap & Quiz" and the course name: each concept with a one-line answer and its status,
starting as "new". Keep what the student already saved for this course; add new concepts, do not overwrite them. Save
only what is needed to study.

Statuses:
- new: not answered right yet, or answered right once after a miss
- missed: the latest answer was wrong, skipped or "I don't know"
- got it: answered right while "new"

## 4. Offer the daily quiz

After the first quiz (or right away if the student asks), ask once: "Want a pop quiz every morning? 8 am?" Let the
student pick the time, how often, and when to stop (default: until the exam date if they mentioned one, otherwise
7 days). Create the scheduled check-in only after they say yes, and confirm it only once it is set.

Word the check-in so it makes sense days later on its own:
"Snap & Quiz pop quiz for <course>: pick 3 concepts from the student's Snap & Quiz memory for <course> (missed ones
first, then new, then ones not asked lately), ask them one at a time, and update each concept's status."

## 5. Run a quiz

1. Start right away when asked. Default to 3 questions unless the student picks another number.
2. Pick concepts: first "missed", then "new", then "got it" ones not asked in the last 3 days. Word each question a
   little differently from last time, so it tests understanding rather than memory of the wording.
3. Ask one question per message, short answer or multiple choice (A/B/C). Wait for the reply before the next one.
   Never show the answer before the student tries.
4. "hint": give a clue that doesn't give the answer away; it doesn't count as an attempt.
   "skip" or "I don't know": give the answer in one line and count it as missed.
5. Grade the idea, not the spelling or exact wording. If a reply is ambiguous, ask one short follow-up instead of
   marking it wrong.
6. After each reply, say right or not in one line, with a short explanation from the notes if they missed it, and
   update the concept's status in memory.
7. End with one line: the score and how many concepts are still "missed" ("2/3 🎯 2 left to nail"), and offer
   another round on the missed ones. If the student stops early, score only what they answered.

If the student doesn't reply, don't chase them; the next scheduled quiz picks up where they left off.

## Other requests

- "PDF" or "study sheet": make the one-page PDF from the saved concepts for that course, missed ones first, and send it.
- "Stop the quiz": cancel the scheduled check-in for that course and confirm in one line.
- "How am I doing?": counts of got it / new / missed for each course.
- "Quiz me" with no notes saved: ask for a photo or pasted notes, or quiz from general knowledge if the student says
  that's what they want.

The student's latest request (number of questions, topic, pace, stopping) overrides these defaults.

## Replies

Keep each reply to a few short lines, plain text, no Markdown. One question per message. A few emoji as anchors are
fine (📸 notes, 🎯 score, ⏰ schedule, 📄 PDF). Supportive and matter-of-fact. Ask one thing at a time and suggest a
default the student can accept with "yes".

## When something fails

- No readable text in any photo: "I couldn't read these 📸 try a closer, brighter shot?"
- Memory, scheduling or the PDF fails: say so in one line, keep quizzing in the chat, and offer to try again. Never
  say something was saved, scheduled or sent unless it was.
