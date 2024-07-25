#!/usr/bin/env python
"""
This script will add questions fron the specified file.

In the github action, if a question / answer is provided, then
the github action will overwrite this file, with extra data.

Running this script multiple times, will just keep on adding
the same content over and over again.

We also only use Tender 1
"""
import csv

from lib.database import Session, TenderEvent, TenderPartitipant, TenderQuestions

with Session.begin() as session:
    tender = session.query(TenderEvent).first()
    if not tender:
        tender = TenderEvent(
            name="Demo tender",
            description="A tender to demonstrate how AI can be used to evaluate tenders.",
        )
        session.add(tender)

    participant = session.query(TenderPartitipant).first()
    if not participant:
        participant = TenderPartitipant(name="Demo participant", tender=tender)
        session.add(participant)

    if session.dirty:
        session.flush()
        print("Added an initial Tender and/or an initial Participant to the database.")

    with open("questions.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:  # Add the questions to the database
            question = TenderQuestions(tender=tender, **row)
            session.add(question)
            print(f"Added question: {question.question}")

    if session.dirty:
        session.commit()
        print("Added the questions from the file.")
