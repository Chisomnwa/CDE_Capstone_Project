output "vpc_id" {
  value = aws_vpc.chisom_vpc.id
}

output "subnet_group_id" {
  value = aws_redshift_subnet_group.redshift_subnet_group.id
}

