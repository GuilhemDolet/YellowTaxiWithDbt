terraform {
    required_providers {
        snowflake = {
        source  = "Snowflake-Labs/snowflake"
        version = "~> 0.94"
        }
    }
}

provider "snowflake" {
    account_name  = var.snowflake_account
    organization_name = "DCZUXXS"
    user = var.snowflake_username
    password = var.snowflake_password
    role     = var.snowflake_role
    # region   = var.snowflake_region
}

