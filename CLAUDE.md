# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an experimental project for exploring NYC Open Data. Eventually we may create and deploy a data visualization webpage for visualizing NYC OpenData. For now we are just exploring.

## NYC OpenData

Information about NYC OpenData is available at urls like https://data.cityofnewyork.us/City-Government/Evictions/6z8x-wfk4/about_data. The Data is accessible through

**Important**: Never commit the `.env` file or expose API credentials in code.

## Development Setup

This project uses **uv** for Python package management. Run scripts with:
```bash
uv run script.py
```

Add dependencies with:
```bash
uv add package-name
```

## Current Status

The codebase is in initial setup phase.
