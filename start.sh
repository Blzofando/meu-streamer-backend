#!/usr/bin/env bash
set -e

echo "🚀 Iniciando servidor..."
exec uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
