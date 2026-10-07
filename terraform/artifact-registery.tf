resource "google_artifact_registry_repository" "build_info" {
  location      = var.region
  repository_id = "build-info"
  description   = "Docker repository for Build Info API"
  format        = "DOCKER"

  depends_on = [
    google_project_service.required_apis
  ]
}