resource "aws_elasticache_subnet_group" "redis" {
  name       = "fastapi-redis-subnets"
  subnet_ids = module.vpc.private_subnets
}
resource "aws_security_group" "redis" {
  name   = "redis-sg"
  vpc_id = module.vpc.vpc_id

  ingress {
    from_port   = 6379
    to_port     = 6379
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"]
  }
}
resource "aws_elasticache_cluster" "redis" {
  cluster_id           = "fastapi-redis"
  engine               = "redis"
  node_type            = "cache.t3.micro"
  num_cache_nodes      = 1
  parameter_group_name = "default.redis7"

  subnet_group_name = aws_elasticache_subnet_group.redis.name
  security_group_ids = [aws_security_group.redis.id]
}