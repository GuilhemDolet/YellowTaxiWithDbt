# Création du warehouse
resource "snowflake_warehouse" "nyc_taxi_wh" {
  name            = "NYC_TAXI_WH"
  warehouse_size  = "MEDIUM"
  auto_suspend    = 60
  auto_resume     = true
  initially_suspended = true
}

# Création de la base de données
resource "snowflake_database" "nyc_taxi_db" {
  name = "NYC_TAXI_DB"
}

# Schéma RAW
resource "snowflake_schema" "raw" {
  database = snowflake_database.nyc_taxi_db.name
  name     = "RAW"
}

# Schéma STAGING
resource "snowflake_schema" "staging" {
  database = snowflake_database.nyc_taxi_db.name
  name     = "STAGING"
}

# Schéma FINAL
resource "snowflake_schema" "final" {
  database = snowflake_database.nyc_taxi_db.name
  name     = "FINAL"
}