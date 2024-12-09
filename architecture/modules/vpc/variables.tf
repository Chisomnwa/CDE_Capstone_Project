variable "VPC_NAME" {}
variable "RESOURCE_PREFIX" {
  
}
variable "azs" {
  default = ["eu-central-1a", "eu-central-1b", "eu-central-1c"]
}
variable "create_route" {
  type    = bool
  default = true  # Set to false in environments where the route already exists
}
