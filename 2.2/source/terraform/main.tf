terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  token     = var.yc_token
  cloud_id  = var.yc_cloud_id
  folder_id = var.yc_folder_id
}

resource "yandex_vpc_network" "vpc_network" {
  name = "my-vpc-network"
}

resource "yandex_vpc_subnet" "subnet" {
  name           = "my-subnet"
  network_id     = yandex_vpc_network.vpc_network.id
  zone           = "ru-central1-a"
  v4_cidr_blocks = ["10.0.0.0/24"]
}

# Web-server 1
resource "yandex_compute_instance" "web_1" {
  name        = "web-1"
  zone        = "ru-central1-a"
  hostname    = "web-1"
  resources {
    cores  = 2
    memory = 2
  }
  boot_disk {
    initialize_params {
      image_id = "fd81n0sfjm6d5nq6l05g"
    }
  }
  network_interface {
    subnet_id = yandex_vpc_subnet.subnet.id
    nat       = true
  }
  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_ed25519.pub")}"
  }
}

# Web-server 2
resource "yandex_compute_instance" "web_2" {
  name        = "web-2"
  zone        = "ru-central1-a"
  hostname    = "web-2"
  resources {
    cores  = 2
    memory = 2
  }
  boot_disk {
    initialize_params {
      image_id = "fd81n0sfjm6d5nq6l05g"
    }
  }
  network_interface {
    subnet_id = yandex_vpc_subnet.subnet.id
    nat       = true
  }
  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_ed25519.pub")}"
  }
}

# Haproxy server 1
resource "yandex_compute_instance" "ha_1" {
  name        = "ha-1"
  zone        = "ru-central1-a"
  hostname    = "ha-1"
  resources {
    cores  = 2
    memory = 2
  }
  boot_disk {
    initialize_params {
      image_id = "fd81n0sfjm6d5nq6l05g"
    }
  }
  network_interface {
    subnet_id = yandex_vpc_subnet.subnet.id
    nat       = true
  }
  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_ed25519.pub")}"
  }
}

# Haproxy server 2
resource "yandex_compute_instance" "ha_2" {
  name        = "ha-2"
  zone        = "ru-central1-a"
  hostname    = "ha-2"
  resources {
    cores  = 2
    memory = 2
  }
  boot_disk {
    initialize_params {
      image_id = "fd81n0sfjm6d5nq6l05g"
    }
  }
  network_interface {
    subnet_id = yandex_vpc_subnet.subnet.id
    nat       = true
  }
  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_ed25519.pub")}"
  }
}
