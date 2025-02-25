variable "vpc_name" {
   default = "travel_agency_vpc"
}

# variable "resource_prefix" {
#   type = string
# }

variable "azs" {
  default = ["af-south-1a", "af-south-1b", "af-south-1c"]
}

# variable "create_route" {
#   type    = bool
#   default = true  # Set to false in environments where the route already exists
# }
