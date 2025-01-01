# terraform {
#   backend "s3" {
#     bucket = var.backend_bucket
#     key    = "path/to/my/key"
#     region = "eu-central-1"
#   }
# }

# Create a backend bucket for storing state file
terraform {
  backend "s3" {
    bucket  = "chisomnwa-travel-agency-backend-bucket"
    key     = "terraform.tfstate"
    region  = "eu-central-1"
    encrypt = true
  }
}
