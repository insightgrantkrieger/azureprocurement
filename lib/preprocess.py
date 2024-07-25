"""
Define the actual preprocessing functions here.
"""

import csv
from pathlib import Path

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


class Preprocessor:
    def __init__(self, input_path: str, output_path: str, respondend_id: int):
        self.input_path = input_path
        self.output_path = output_path
        self.respondend_id = respondend_id
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=lambda x: len(x),
            is_separator_regex=False,
        )
        self.fieldnames = [
            "metadata_storage_name",
            "ResponseID",
            "Page",
            "Chunk",
            "content",
        ]

    def cloud_output(self):
        """
        Remove any data in the output directory.
        """
        [
            filename.unlink()
            for filename in Path(self.output_path).glob("*")
            if filename.is_file()  # only remove files
        ]

    def preprocess(self):
        """
        Preprocess the data.
        """
        self.cloud_output()

        # Now process the files
        for filename in Path(self.input_path).glob("*.pdf"):
            self.process_file(filename)

    def get_output_filename(self, filename: Path) -> Path:
        """
        Get the output filename.
        """
        return Path(self.output_path) / filename.with_suffix(".csv").name

    def process_file(self, filename: Path):
        """
        Process the file.
        """
        result_filename = self.get_output_filename(filename)
        print(f"Reading file: {filename}")

        loader = PyPDFLoader(filename)
        chunks = self.text_splitter.split_documents(loader.load())

        with open(result_filename, "w") as output:
            writer = csv.DictWriter(output, fieldnames=self.fieldnames)

            writer.writeheader()
            for chunk_id, chunk in enumerate(chunks):
                writer.writerow(
                    {
                        "metadata_storage_name": filename.name,
                        "ResponseID": self.respondend_id,
                        "Page": chunk.metadata.get("page", 0),
                        "Chunk": chunk_id,
                        "content": chunk.page_content,
                    }
                )

        print(f"Writing file: {result_filename}")
