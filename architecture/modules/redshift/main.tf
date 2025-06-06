resource "aws_redshift_cluster" "travel_agency_cluster" {
  cluster_identifier        = var.cluster_identifier
  database_name             = var.database_name
  master_username           = var.username
  master_password           = var.password
  node_type                 = "dc2.large"
  cluster_type              = "multi"
  number_of_nodes           = 2
  cluster_subnet_group_name = var.redshift_subnet_group
  iam_roles                 = [var.redshift_role_arn]
  skip_final_snapshot       = true
}
