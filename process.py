#!/usr/bin/env python
"""
This module will for the first tender ask the questions that are in the database.
And write any answers back to the database.
"""

from lib.ai import ask_question_to_ai
from lib.database import Session, TenderAnswers, TenderEvent, TenderQuestions

with Session.begin() as session:
    tender = session.query(TenderEvent).first()
    if not tender:
        print("No tender found.")
        exit(1)

    participant = tender.tender_participants[0]

    questions = (
        session.query(TenderQuestions).filter(TenderQuestions.tender == tender).all()
    )
    if not questions:
        print("No questions found.")
        exit(1)

    for question in questions:
        print(
            f"Processing tender: {tender.name}, participant: {participant.name}, "
            f"Question: {question.question}"
        )
        answer = ask_question_to_ai(tender, participant, question)
        if answer:
            # Check if we already have an answer for this question
            existing_answer = (
                session.query(TenderAnswers)
                .filter(TenderAnswers.participant == participant)
                .filter(TenderAnswers.question == question)
                .first()
            )
            # Update the answer if we already have one
            if existing_answer:
                existing_answer.answer = answer
                session.add(existing_answer)
            else:
                # Create a new answer entry
                tender_answer = TenderAnswers(
                    participant=participant, question=question, answer=answer
                )
                session.add(tender_answer)

    if session.dirty:
        session.commit()
        print("Added the answers to the database.")
