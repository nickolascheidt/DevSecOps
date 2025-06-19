output "instance_public_ip" {
  value = aws_instance.devsecops_instance.public_ip
}

output "instance_public_dns" {
  value = aws_instance.devsecops_instance.public_dns
  description = "DNS público da instância EC2"
}