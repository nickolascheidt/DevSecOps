variable "aws_region" {
  description = "Região da AWS"
  default     = "sa-east-1"
}

variable "instance_type" {
  description = "Tipo da instância EC2"
  default     = "t2.micro"
}

variable "key_name" {
  description = "Nome do par de chaves"
  default     = "devsecops_key"
}

variable "public_key" {
  description = "Chave publica SSH para provisionar EC2"
  type = string
}