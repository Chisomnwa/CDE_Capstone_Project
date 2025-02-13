# variable "bucket_name" {
#   default = "cde-project-travel-agency-bucket"
# }

variable "bucket_name" {
  description = "The name of the S3 bucket"
  type        = string
}
