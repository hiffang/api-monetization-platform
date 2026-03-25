# Contributing to API Monetization Platform

Thank you for your interest in contributing! This guide helps you understand our development process.

## Code Style

We use:
- **Black** for code formatting
- **Flake8** for linting
- **isort** for import sorting

Before committing:
```bash
black .
flake8 .
isort .
```

## Workflow

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature`
3. **Make** your changes
4. **Test** your changes: `pytest`
5. **Commit**: Use clear commit messages
6. **Push** to your fork
7. **Create** a Pull Request

## Commit Messages

Use clear, descriptive messages:

```
feat: Add user authentication endpoint
fix: Resolve database connection timeout  
docs: Update API documentation
refactor: Simplify billing calculation logic
test: Add tests for payment processing
```

## Pull Request Guidelines

- Include a descriptive title
- Reference any related issues: `Fixes #123`
- Describe your changes
- Include test results
- Request review from maintainers

## Testing

All contributions must include tests:

```bash
# Run tests
pytest

# With coverage
pytest --cov

# Specific test
pytest tests/test_health.py -v
```

## Documentation

Update documentation for:
- New endpoints: Add to API docs
- Configuration changes: Update .env.example
- Architecture changes: Update ARCHITECTURE.md

## Questions?

- Open an issue for bugs
- Start a discussion for features
- Check existing issues first

Thank you for contributing!
