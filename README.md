# OpenWebinar Platform

**OpenWebinar** is a generic, self-hostable webinar hosting platform built for high-performance and visual impact.

> **Note:** This project originated as a school assignment ("Svamparnas Värld") to demonstrate modern cloud infrastructure, CI/CD pipelines, and full-stack development. It has since evolved into a reusable platform.

## Architecture

The platform uses a modern, monolithic architecture for simplicity and performance:

- **Backend**: Django (Python) serving an Inertia.js API.
- **Frontend**: Vue.js 3 + Tailwind CSS (bundled via Vite).
- **Infrastructure**: Platform-agnostic IaC using OpenTofu & Ansible (Azure, Proxmox, Docker).

## Documentation

- **[Architecture Overview](docs/deployment/architecture.md)**: High-level system design and topology.
- **[Development Guide](DEVELOPER_GUIDE.md)**: Setup instructions for local development.
- **[Deployment & CI/CD](docs/deployment/ci-cd.md)**: How to deploy to production.
- **[Infrastructure Details](infra/README.md)**: Deep dive into the OpenTofu and Ansible setup.

## Quick Start (Local)

1. **Clone the repo:**
   ```bash
   git clone https://github.com/loopaware/svamparnas-varld.git
   cd svamparnas-varld
   ```

2. **Start the Dockerized Environment:**
   ```bash
   cd infra/opentofu/local
   tofu init && tofu apply
   ```

3. **Configure & Run:**
   ```bash
   ./scripts/ci_local_test.sh
   ```

## License
MIT
