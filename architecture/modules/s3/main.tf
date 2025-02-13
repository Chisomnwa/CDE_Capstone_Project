# Create an S3 Bucket
resource "aws_s3_bucket" "chisom_travel_agency" {
  bucket = var.bucket_name

  tags = {
    Name        = "CDE Capstone Project bucket"
    Environment = "Dev"
    owner       = "Chisom"
    team        = "Core Data Engineers"
    managed_by  = "Team Leaders"
  }
}


# Enable bucket versioning
resource "aws_s3_bucket_versioning" "chisom_cde_project_versioning" {
  bucket = aws_s3_bucket.chisom_travel_agency.id
  versioning_configuration {
    status = "Enabled"
  }
}