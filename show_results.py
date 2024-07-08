#!/usr/bin/env python
"""
Simple helper that will output a table with the results of the tender.
"""
import rich
from rich import box
from rich.table import Table

from lib.database import Session, TenderAnswers, TenderEvent

with Session.begin() as session:
    for tender in session.query(TenderEvent).all():
        table = Table(box=box.SQUARE, show_lines=True)
        table.title = f"{tender.name} - {tender.description}"
        table.add_column("Participant")
        table.add_column("Question")
        table.add_column("Answer")

        for participant in tender.tender_participants:
            for question in tender.tender_questions:
                answer = (
                    session.query(TenderAnswers)
                    .filter(TenderAnswers.participant == participant)
                    .filter(TenderAnswers.question == question)
                    .first()
                )
                table.add_row(
                    participant.name, question.question, answer.answer if answer else ""
                )

    rich.print(table)
