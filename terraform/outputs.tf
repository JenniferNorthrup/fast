output "cluster_name" {
  value = module.eks.cluster_name
}

output "ecr_url" {
  value = aws_ecr_repository.fastapi.repository_url
}

output "postgres_endpoint" {
  value = aws_db_instance.postgres.address
}

output "redis_endpoint" {
  value = aws_elasticache_cluster.redis.cache_nodes[0].address
}
