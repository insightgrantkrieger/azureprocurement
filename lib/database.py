from typing import List

from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    sessionmaker,
)

from .config import config

if config.local:
    engine_url = "sqlite:///tender.db"
else:
    engine_url = URL.create(
        "mssql+pyodbc",
        query={
            "odbc_connect": "Driver={ODBC Driver 18 for SQL Server};"
            "Server=tcp:eql-ai-sandbox-sql.database.windows.net,1433;"
            "Database=eqlaisandboxdb01;"
            f"Uid={config.db_user};"
            f"Pwd={config.db_pass};"
            "Encrypt=yes;"
            "TrustServerCertificate=no;"
            "Connection Timeout=30;"
        },
    )

engine = create_engine(
    engine_url,
    echo=config.debug,
)

Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class TenderEvent(Base):
    """Describe the tender we are looking at."""

    __tablename__ = "tender_event"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()

    tender_participants: Mapped[List["TenderPartitipant"]] = relationship(
        back_populates="tender"
    )
    tender_questions: Mapped[List["TenderQuestions"]] = relationship(
        back_populates="tender"
    )


class TenderPartitipant(Base):
    """Describe the tender we are looking at."""

    __tablename__ = "tender_participant"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()

    tender_id: Mapped[int] = mapped_column(ForeignKey("tender_event.id"))
    tender: Mapped[TenderEvent] = relationship(back_populates="tender_participants")


class TenderQuestions(Base):
    """
    This is where we store the questions we want to ask during the tender,
    and any system prompts.
    """

    __tablename__ = "tender_questions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    question: Mapped[str] = mapped_column()  # Human readable question
    ai_ask: Mapped[str] = mapped_column()  # AI prompt
    system_prompt: Mapped[str] = mapped_column()  # System prompt for AI
    ai_search: Mapped[str] = (
        mapped_column()
    )  # AI search term to search in the documents

    tender_id = mapped_column(ForeignKey("tender_event.id"))
    tender: Mapped[TenderEvent] = relationship(back_populates="tender_questions")
    answers: Mapped[List["TenderAnswers"]] = relationship(back_populates="question")


class TenderAnswers(Base):
    """
    Here we collect the answers of the various tender runs.
    """

    __tablename__ = "tender_answers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    answer: Mapped[str] = mapped_column()

    question_id = mapped_column(ForeignKey("tender_questions.id"))
    question: Mapped[TenderQuestions] = relationship(back_populates="answers")
    participant_id = mapped_column(ForeignKey("tender_participant.id"))
    participant: Mapped[TenderPartitipant] = relationship()
