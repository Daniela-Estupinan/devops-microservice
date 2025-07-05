provider "local" {}

resource "local_file" "app_info" {
  content  = "This simulates infra deployment."
  filename = "${path.module}/infra.txt"
}
