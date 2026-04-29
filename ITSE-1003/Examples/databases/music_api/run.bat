@echo off
python seed.py
python -m uvicorn app.main:app --reload
