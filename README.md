# Nebula AI - Intelligent Code Review Assistant
An intelligent code review assistant powered by Google Gemini 1.5 Flash. Nebula AI detects bugs, security vulnerabilities, and performance bottlenecks in real-time. Built with Django &amp; Vanilla JS.

**Nebula AI** is a SaaS-ready tool designed to enhance code quality by leveraging the power of Large Language Models. Unlike standard linters, Nebula uses **Google Gemini 1.5 Flash** to understand context, identify logic errors, and suggest Big-O performance optimizations.

### Key Features
* **Hybrid Architecture:** Guest access with session carryover logic (convert guests to users seamlessly).
* **Deep Analysis:** Goes beyond syntax to find Security (SQLi/XSS) and Logic bugs.
* **Privacy First:** Code is processed in memory and never stored on disk.
* **Nebula UI:** A custom Glassmorphism design system using Tailwind CSS.

### Tech Stack
* **Backend:** Python, Django
* **AI Engine:** Google GenAI (Gemini 1.5 Flash)
* **Frontend:** HTML5, Tailwind CSS, Vanilla JS
* **Database:** SQLite (Dev) / PostgreSQL (Prod)
