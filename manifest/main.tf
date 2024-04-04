terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.7.0"
    }
  }

  backend "azurerm" {
    resource_group_name  = "mdc-rg"
    storage_account_name = "mdcterraform"
    container_name       = "tfstates"
    key                  = "terraform.tfstate"
    use_oidc             = true
  }

}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "my_demo_rg1" {
  location = var.location
  name     = var.name

  tags = {
    "env"  = "test"
    "name" = "storageaccount"
  }
}