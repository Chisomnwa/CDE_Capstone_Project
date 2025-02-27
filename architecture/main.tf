# module "vpc" {
#   source = "./modules/vpc"
# }

# module "ecr" {
#   source = "./modules/ecr"
# }

# module "s3" {
#   source      = "./modules/s3"
#   bucket_name = "travel-agency-bucket"
# }

# module "roles" {
#   source = "./modules/iam_roles"
# }

# data "aws_ssm_parameter" "password" {
#   name = "redshift_password"
# }

# data "aws_ssm_parameter" "username" {
#   name = "redshift_username"
# }

# module "ssm" {
#   source = "./modules/ssm"
# }

# module "redshift" {
#   source                = "./modules/redshift"
#   redshift_subnet_group = module.vpc.subnet_group_id
#   redshift_role_arn     = module.roles.s3_redshift_role_arn # Pointing to the output of the iam_roles
#   username              = data.aws_ssm_parameter.username.value
#   password              = data.aws_ssm_parameter.password.value
#   database_name         = "travel_agency"
#   cluster_identifier    = "travel-agency-cluster" # It must contain only lowercase alphanumeric characters (a-z, 0-9) and hyphens (-).
# }
