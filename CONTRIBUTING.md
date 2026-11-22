# Contributing Guidelines

Thank you for contributing to the **Dynamic Graph Coloring Based Exam Timetabling and Seating Plan Generator** project!

## 1. Development Workflow
We follow the Scrum framework and GitHub Flow:
1. **Fork or Branch:** Create a feature branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Commit Conventions:** Follow Conventional Commits:
   - `feat:` New feature or capability
   - `fix:` Bug fix or invariant correction
   - `test:` Unit or integration tests
   - `docs:` Documentation updates
   - `ci:` CI/CD pipeline changes
   - `refactor:` Code refactoring without behavioral alterations
3. **Run Tests:** Ensure all tests pass before opening a Pull Request:
   ```bash
   cd backend
   pytest -v
   ```
4. **Pull Request:** Open a PR targeting `main` with description and acceptance verification details.

## 2. Coding Standards
- Python backend follows **PEP 8** style guidelines with type annotations.
- Frontend adheres to modern HTML5 and Tailwind CSS utility conventions.
- All algorithms must include formal verification tests confirming no two adjacent vertices share the same color.
