import os
from pathlib import Path

project_name = "us_visa"
list_of_files = [
    Path(f"{project_name}/__init__.py"),
    Path(f"{project_name}/components/__init__.py"),
    Path(f"{project_name}/components/data_ingestion.py"),
    Path(f"{project_name}/components/data_validation.py"),
    Path(f"{project_name}/components/data_transformation.py"),
    Path(f"{project_name}/components/model_trainer.py"),
    Path(f"{project_name}/components/model_evaluation.py"),
    Path(f"{project_name}/components/model_pusher.py"),
    Path(f"{project_name}/configuration/__init__.py"),
    Path(f"{project_name}/constants/__init__.py"),
    Path(f"{project_name}/entity/__init__.py"),
    Path(f"{project_name}/entity/config_entity.py"),
    Path(f"{project_name}/entity/artifact_entity.py"),
    Path(f"{project_name}/exception/__init__.py"),
    Path(f"{project_name}/logger/__init__.py"),
    Path(f"{project_name}/pipline/__init__.py"),
    Path(f"{project_name}/pipline/training_pipeline.py"),
    Path(f"{project_name}/pipline/prediction_pipeline.py"),
    Path(f"{project_name}/utils/__init__.py"),
    Path(f"{project_name}/utils/main_utils.py"),
    Path("app.py"),
    Path("requirements.txt"),
    Path("Dockerfile"),
    Path(".dockerignore"),
    Path("demo.py"),
    Path("setup.py"),
    Path("config/model.yaml"),
    Path("config/schema.yaml"),
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")

