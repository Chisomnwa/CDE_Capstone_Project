terraform {
  backend "s3" {
    bucket = "travel-agency-backend-bucket"
    key    = "travel-agency/dev/terraform.tfstate" # You define this path yourself. It's like a folder structure.
    region = "af-south-1"
  }
}
