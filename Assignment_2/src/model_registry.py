import mlflow
from mlflow.tracking import MlflowClient

def manage_registry():
    client = MlflowClient()
    model_name = "WineQualityClassifier"
    
    print(f"Fetching registered model versions for: {model_name}")
    try:
        latest_versions = client.get_latest_versions(model_name)
        for version in latest_versions:
            print(f"Version: {version.version}, Stage: {version.current_stage}, RunID: {version.run_id}")
            
        if latest_versions:
            target_version = latest_versions[-1].version
            print(f"Transitioning version {target_version} to Production...")
            client.transition_model_version_stage(
                name=model_name,
                version=target_version,
                stage="Production",
                archive_existing_versions=True
            )
            print(f"Version {target_version} is now in Production.")
    except Exception as e:
        print(f"Registry operation notice: {e}")

if __name__ == "__main__":
    manage_registry()
