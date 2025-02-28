from crewai_rag.crew_setup import crew
import subprocess, os

study_material_path = "./study_material"

# Find all .md, .txt, and .pdf files recursively
all_files = list(study_material_path.rglob("*.md")) + list(study_material_path.rglob("*.txt")) + list(study_material_path.rglob("*.pdf"))
print("📂 Found Files:", [str(f) for f in all_files])

if not os.path.exists(study_material_path):
    try:
        print(f"📂 'study_material' directory not found. Cloning from GitHub...")
        subprocess.run(["git", "clone", "https://github.com/panaversity/learn-modern-ai-python", study_material_path], check=True)
        print(f"✅ Cloned repository into {study_material_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error cloning repository: {e}")



# RUN CREW

result= crew.kickoff()
print(result)