variable "snowflake_account" {
  description = "Nom du compte Swnowflake"
  type        = string
}

variable "snowflake_username" {
  description = "user login du compte snowflake"
  type        = string
}

variable "snowflake_password" {
  description = "mot de passe du compte snowflake"
  type        = string
  sensitive   = true
}

variable "snowflake_role" {
  description = "role du compte snowflake"
  type        = string
}

variable "snowflake_region" {
  description = "region du compte snowflake"
  type        = string
  default     = "eu-central-1"
}
