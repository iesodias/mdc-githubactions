variable "name" {
  type    = string
}
variable "location" {
  type        = string
  description = "Azure Region where all these resources will be provisioned"
  default     = "Central US"
}