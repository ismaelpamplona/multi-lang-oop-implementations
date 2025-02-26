# Multi-Language OOP Implementations

This repository contains **object-oriented programming (OOP) implementations** in multiple languages (**Python, JavaScript, TypeScript, and Rust**) for **training**. Each language has its own isolated environment with unit tests.

## 📁 Project Structure

The repository is organized as follows:

- **🚀 `javascript/`** → JavaScript implementations (using Jest for testing)
- **📘 `typescript/`** → TypeScript implementations (using Jest for testing)
- **🐍 `python/`** → Python implementations (using Poetry & pytest)
- **🦀 `rust/`** → Rust implementations (using Cargo)

## Setup Instructions

### JavaScript

**Requirements:** Node.js (LTS recommended)

1. Navigate to the `js/` directory:

   ```bash
   cd js
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Run tests:
   ```bash
   npm test
   ```

### TypeScript

**Requirements:** Node.js, TypeScript

1. Navigate to the `ts/` directory:

   ```bash
   cd ts
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Run tests:

   ```bash
   npm test
   ```

### Python

**Requirements:** Python 3, Poetry

1. Navigate to the `python/` directory:

   ```bash
   cd python
   ```

2. Install dependencies:

   ```bash
   poetry install
   ```

3. Run tests:

   ```bash
   poetry run pytest
   ```

### Rust

**Requirements:** Rust (via `rustup`)

1. Navigate to the `rust/` directory:

   ```bash
   cd rust
   ```

2. Run tests:

   ```bash
   cargo test --workspace
   ```

## Run All Tests with One Command

You can execute all tests across **all languages** using the `run_tests.sh` script:

1. Make it executable (only needed once):

   ```bash
   chmod +x run_tests.sh
   ```

2. Run all tests:

   ```bash
   ./run_tests.sh
   ```

This will sequentially run tests for **JavaScript, TypeScript, Python, and Rust**.

## License

This project is licensed under the **MIT License**.

## Contributing

Contributions are welcome! If you'd like to add **new OOP implementations**, improve existing code, or enhance documentation, feel free to **submit a pull request**.

1. Fork the repository
2. Create a new branch (`feature/my-new-class`)
3. Commit your changes
4. Open a PR!

## About This Project

This repository is designed for **job interview preparation** with a focus on **OOP concepts across multiple languages**. It serves as a **learning and reference resource** for anyone wanting to compare OOP implementations across **Python, JavaScript, TypeScript, and Rust**.

Happy coding! 🚀
