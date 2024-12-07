resource "aws_vpc" "chisom_vpc" {
  cidr_block       = "172.16.0.0/16"
}


resource "aws_subnet" "redshift_subnet_a" {
  vpc_id     = aws_vpc.chisom_vpc.id
  cidr_block ="172.16.24.0/24"
 availability_zone = var.azs[0]
  tags = {
    Name = "zone_a"
  }
}



