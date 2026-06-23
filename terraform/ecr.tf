resource "aws_ecr_repository" "fastapi" {
  name = "fastapi-prod"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Environment = "prod"
  }
}