resource "aws_key_pair" "devsecops_key" {
  key_name   = var.key_name
  public_key = var.public_key
}

resource "aws_security_group" "devsecops_sg" {
  name        = "devsecops-sg" 
  description = "Permitir acesso a aplicacao web"
  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
    ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "devsecops_instance" {
  ami                    = "ami-0923cbda828605357" # Amazon Linux 2 (sa-east-1)
  instance_type          = var.instance_type
  key_name               = var.key_name
  vpc_security_group_ids = [aws_security_group.devsecops_sg.id]

  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo yum install -y docker
              sudo systemctl start docker
              sudo systemctl enable docker
              EOF

  tags = {
    Name = "DevSecOpsInstance"
  }
}