#!/bin/bash

echo -e "\n🚀 Running JavaScript tests..."
cd javascript && npm test || exit 1
echo -e "\n=================================="
cd ..

echo -e "\n📘 Running TypeScript tests..."
cd typescript && npm test || exit 1
echo -e "\n=================================="
cd ..

echo -e "\n🐍 Running Python tests..."
cd python && poetry run pytest || exit 1
cd ..

echo -e "\n🦀 Running Rust tests..."
cd rust && cargo test --workspace || exit 1

echo -e "✅ All tests completed!"
