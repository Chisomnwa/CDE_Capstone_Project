locals {
  RESOURCE_PREFIX = "travel_agency"
  VPC_NAME        = "${local.RESOURCE_PREFIX}-vpc"
}

module "vpc" {
  source          = "./modules/vpc"
  RESOURCE_PREFIX = local.RESOURCE_PREFIX
  VPC_NAME        = local.VPC_NAME
}

module "s3" {
  source      = "./modules/s3"
  bucket_name = "${local.RESOURCE_PREFIX}-bucket"
}

module "roles" {
  source     = "./modules/iam_roles"
  redshift_role_arn = module.iam_roles.output.redshift_role_arn
}

module "redshift" {
  source              = "./modules/redshift"
  redshift_subnet_group = module.vpc.subnet_group_id
  redshift_role_arn   = module.roles.redshift_iam_role_arn 
  username            = module.redshift.var.username
  password            = var.password
  database_name       = var.database_name
  cluster_identifier  =  module.redshift.aws_redshift_cluster.travel_agency_cluster
}

#  ecr_name =  "${local.RESOURCE_PREFIX}-ecr"
module "ecr" {
  source   = "./modules/ecr"
  ecr_name =  modules.ecr
}

# module "rds" {
#   source          = "./modules/rds"
#   vpc_name        = "${local.RESOURCE_PREFIX}-vpc"
#   vpc_id          = module.vpc.vpc_id
#   RESOURCE_PREFIX = local.RESOURCE_PREFIX
#   depends_on = [ module.vpc ]
# }