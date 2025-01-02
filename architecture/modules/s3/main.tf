# Create a s3 bucket to store the extracted data from the REST API
resource "aws_s3_bucket" "travel_agency_bucket" {
  bucket = var.bucket_name

  tags = {
    Name        = "travel-agency-bucket"
    Environment = "Dev"
    owner       = "Chisom"
    team        = "Core Data Engineers"
    managed_by  = "Mayowa"
  }
}

# Enable bucket versioning
resource "aws_s3_bucket_versioning" "travel_agency_bucket_versioning" {
  bucket = aws_s3_bucket.travel_agency_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

# # Create a backend s3 bucket to store our state file
# resource "aws_s3_bucket" "backend_bucket" {
#   bucket = var.backend_bucket

#   tags = {
#     Name        = "travel-agency-backend-bucket"
#     Environment = "Dev"
#     owner       = "Chisom"
#     team        = "Core Data Engineers"
#     managed_by  = "Mayowa"
#   }
# }

# # Enable bucket versioning
# resource "aws_s3_bucket_versioning" "backend_bucket_versioning" {
#   bucket = aws_s3_bucket.backend_bucket.id
#   versioning_configuration {
#     status = "Enabled"
#   }
# }
