# scaffold-ai

AI-assisted project scaffolder for modern apps.

scaffold-ai creates opinionated project structures (folders + files) for different stacks in seconds, so you can start coding instead of wiring boilerplate.

---

## Features

- 🧱 Project scaffolding from templates  
- 🐍 Simple Python app template (`python-simple-app`)  
- 🌐 Web SPA template with TypeScript (`web-spa-js`)  
- 🔁 Non-destructive by default (`--force` to overwrite)  
- 🧰 Single CLI entrypoint: `scaffold-ai`

Planned features:

- 🧠 AI-powered customization of templates (agentic workflows)  
- 📄 Automatic dev/prod documentation skeletons  
- 🌩 Cloud-native templates (Docker, Kubernetes, Terraform)

---

## Installation

Requirements:

- Python 3.10+  
- Git

Install in editable mode for development:

```bash
git clone https://github.com/WenesLimem/scaffold-ai.git
cd scaffold-ai
pip install -e .
```

After installation, you can run the CLI either as a module or via the console script:

```bash
python -m scaffold_ai.cli --help
# or, if your PATH is configured
scaffold-ai --help
```
