# define reusable resources
locals {
  resource_prefix = "travel_agency"
  vpc_name        = "${local.resource_prefix}-vpc"
}

module "vpc" {
  source          = "./modules/vpc"
  resource_prefix = local.resource_prefix
  vpc_name        = local.vpc_name
}

module "s3" {
  source      = "./modules/s3"
  bucket_name = "${local.resource_prefix}-bucket"
}

module "roles" {
  source            = "./modules/iam_roles"
  redshift_role_arn = "${local.resource_prefix}-role"
}

module "redshift" {
  source                = "./modules/redshift"
  redshift_subnet_group = module.vpc.subnet_group_id
  redshift_role_arn     = module.iam_roles.redshift_iam_role_arn
  username              = var.username
  password              = var.password
  database_name         = var.database_name
  cluster_identifier    = var.cluster_identifier
}

module "ecr" {
  source = "./modules/ecr"
}

