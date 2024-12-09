# variable "bucket_name" {
#   default = "cde-project-travel-agency-bucket"
# }

variable "bucket_name" {
  description = "The name of the S3 bucket"
  type        = string
}


# variable "backend_bucket" {
#   description = "The name of the S3 backend bucket"
#   type        = string
# }

variable "backend_bucket" {
  default = "travel-agency-backend-bucket"
}
