output "cluster_name" {
  value = google_container_cluster.primary.name
}

output "cluster_location" {
  value = google_container_cluster.primary.location
}

output "artifact_registry_repository" {
  value = google_artifact_registry_repository.build_info.name
}


output "github_actions_service_account" {
  value = google_service_account.github_actions.email
}

output "github_workload_identity_provider" {
  value = google_iam_workload_identity_pool_provider.github.name
}