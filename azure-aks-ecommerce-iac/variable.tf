variable "resource_group_name" {
  type = string
  default = "ecommerce_rg"
  description = "Name of the resource group"
}

variable "location" {
  type = string 
  default = " centtalindia"
  description = "Azure region (e.g., centralindia)"
  
}

variable "vnet_name" {
    type = string 
    default = "vnet_ecommerce"
    description = "Name of the Virtual Network"
  
}

variable "subnet-name"{
    type = string 
    default = "subnet_ecommerce"
    description = "Name of the subnet"

}

variable "address_space" {
   type = list(string)
   default     = ["10.0.0.0/16"]
   description = "CIDR block(s) for the virtual network"

}

variable "subnet_prefixes" {
  type        = list(string)
  default     = ["10.0.1.0/24"]
  description = "CIDR block(s) for the subnet"
}

variable "vm_name" {
  type        = string
  default     = "demo_vm"
  description =  "Virtual Machine name"
  }

variable "vm_size" {
  type        = string
  default = "standard_B1s"
  description = "this is Azure VM Size"
}

variable "admin_username" {
  type        = string
  default = "dheeraj"
  description = "this ia Admin Username"
}

variable "ssh_public_key_path" {
  type        = string
  default = "terra-key-vm.pub"
  description = "Path to SSH Public Key file"
}