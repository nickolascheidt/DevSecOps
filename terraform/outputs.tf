output "instance_public_ip" {
  value = aws_instance.devsecops_instance.public_ip
}