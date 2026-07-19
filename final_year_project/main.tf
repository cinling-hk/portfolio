# =============================================
# main.tf — instantiate EC2 firewall（t2.micro + Ubuntu）
# =============================================

# Provide basic information(TF.file and AWS provider)
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Connect to AWS
provider "aws" {
  region = "ap-east-1"   # Hong Kong Region 
}

# Auto update to newest image: Ubuntu 22.04 LTS 
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]   # Ubuntu Offical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  filter {
    name   = "architecture"
    values = ["x86_64"]
  }

}

# Instantiate EC2 
resource "aws_instance" "fyp_firewall" {
  ami           = data.aws_ami.ubuntu.id     # newest Ubuntu
  instance_type = "t3.micro"                 # free tier instance
  key_name      = "fyp-key"                 # Key-pair name

  # Storage setting
  root_block_device {
    volume_size           = 16
    volume_type           = "gp3"            
    delete_on_termination = true             # delete harddisk on termination
  }

  # Instance name in AWS Console
  tags = {
    Name = "fyp_firewall"
  }

  # Auto public IP (for SSH)
  associate_public_ip_address = true
}