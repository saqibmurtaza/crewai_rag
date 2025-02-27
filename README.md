crewai-rag-project/
│── src/                      # Source code folder
│   │── __init__.py           # Makes src a Python package
│   │── data_loader.py        # Code to load study material (text, PDFs, etc.)
│   │── vector_store.py       # Code to manage FAISS/ChromaDB
│   │── agents.py             # CrewAI agents & task definitions
│   │── crew_manager.py       # Crew execution logic
│   │── question_generator.py # Code to generate MCQs & short questions
│   │── utils.py              # Helper functions (e.g., text cleaning)
│
│── study_material/           # Folder to store study notes, PDFs, or text files
│── main.py                   # Main script to start the pipeline
│── requirements.txt           # Dependencies list
│── .env                       # API keys & environment variables
│── README.md                  # Documentation for the project
│── chroma_db/                 # ChromaDB storage (if using persistent storage)
│── notebooks/                 # Jupyter notebooks for testing/debugging (optional)
