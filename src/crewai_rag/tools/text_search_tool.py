import os
from crewai.tools import BaseTool
from pydantic import Field

class TextSearchTool(BaseTool):
    """A tool to search through .md and .txt files."""

    name: str = "Text Search Tool"  # ✅ Required by CrewAI
    description: str = "Search text files for relevant content."  # ✅ Required by CrewAI
    directory: str = Field(default="./study_material", description="Directory to search in")  # ✅ Fix
    documents: dict = Field(default={}, description="Loaded text documents")  # ✅ Fix

    def __init__(self, directory: str = "./study_material"):
        """
        Initialize the tool with the directory containing study materials.
        
        :param directory: Path where .md and .txt files are stored.
        """
        super().__init__()  # ✅ Correctly initialize BaseTool
        self.directory = directory  # ✅ Ensure directory is stored
        self.documents = self.load_documents()  # ✅ Now explicitly defined

    def load_documents(self) -> dict:
        """Loads text content from all .md and .txt files in the directory."""
        documents = {}
        if not os.path.exists(self.directory):  # ✅ Handle missing directory
            print(f"Warning: Directory {self.directory} does not exist.")
            return documents
        
        for file_name in os.listdir(self.directory):
            if file_name.endswith(".md") or file_name.endswith(".txt"):
                file_path = os.path.join(self.directory, file_name)
                with open(file_path, "r", encoding="utf-8") as file:
                    documents[file_name] = file.read()
        return documents

    def _run(self, query: str):
        """
        Search for a keyword or phrase in loaded documents.
        
        :param query: The search term.
        :return: A dictionary with matching documents and excerpts.
        """
        results = {}
        for file_name, content in self.documents.items():
            if query.lower() in content.lower():
                results[file_name] = content[:500]  # Return first 500 characters as a preview
        return results if results else "No relevant content found."
