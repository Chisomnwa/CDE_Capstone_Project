resource "aws_redshift_cluster" "travel_agency_cluster" {
  cluster_identifier = "tf-redshift-cluster"
  database_name      = "mydb"
  master_username    = "exampleuser"
  master_password    = "Mustbe8characters"
  node_type          = "dc2.large"
  cluster_type       = "multi"
  number_of_nodes = 2
  cluster_subnet_group_name = var.redshift_subnet_group
  iam_roles = [var.redshift_role_arn]
  skip_final_snapshot = true
}
