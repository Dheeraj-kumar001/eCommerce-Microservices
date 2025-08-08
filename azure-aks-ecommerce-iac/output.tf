output "resource_group_name" {
  description = "Name of the resource group created"
  value       = azurerm_resource_group.ecommerce_rg.name
}

output "vnet_name" {
  description = "Name of the virtual network created"
  value       = azurerm_virtual_network.vnet_ecommerce.name
}

output "vnet_id" {
  description = "ID of the virtual network"
  value       = azurerm_virtual_network.vnet_ecommerce.id
}

output "subnet_name" {
  description = "Name of the subnet created"
  value       = azurerm_subnet.subnet_ecommerce.name
}

output "subnet_id" {
  description = "ID of the subnet"
  value       = azurerm_subnet.subnet_ecommerce.id
  }
output "vm_id" {
  value = azurerm_linux_virtual_machine.demo_vm.id
}

output "vm_private_ip" {
  value = azurerm_network_interface.nic.private_ip_address
}

