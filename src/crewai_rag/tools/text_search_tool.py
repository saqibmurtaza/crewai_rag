from crewai.tools import BaseTool
from pydantic import Field
from pathlib import Path
import fitz  # PyMuPDF for PDFs
from crewai_rag.file_selector import uploaded_file_path  # ✅ Import file path

class TextSearchTool(BaseTool):
    """A tool to search through uploaded .txt, .md, and .pdf files."""

    name: str = "Text Search Tool"
    description: str = "Search text files for relevant content."
    file_path: Path = Field(default=uploaded_file_path, description="Path to the uploaded study material")

    def load_file(self):
        """Loads content from the uploaded file."""
        if not self.file_path.exists():
            raise FileNotFoundError(f"❌ File not found: {self.file_path}")

        content = ""
        if self.file_path.suffix in [".txt", ".md"]:
            with open(self.file_path, "r", encoding="utf-8") as f:
                content = f.read()
        elif self.file_path.suffix == ".pdf":
            with fitz.open(self.file_path) as doc:
                content = "\n".join(page.get_text("text") for page in doc)

        return content

    def _run(self, query: str):
        """Search for the given query in the uploaded file."""
        self.file_content = self.load_file()
        if query.lower() in self.file_content.lower():
            return "✅ Relevant content found:\n" + self.file_content[:500]  # Show first 500 chars
        else:
            return "❌ No relevant content found."
