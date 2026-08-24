# Random Chore Assignment Emailer

[![Python: 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Protocol: SMTP](https://img.shields.io/badge/Protocol-Gmail%20SMTP-red.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An automated Python utility that randomly distributes household responsibilities among members and sends individual email notifications via Gmail's SMTP service.

---

> ### ⚠️ Academic Project Context
> This repository documents an undergraduate **Level 1, Term II (1-2)** experimental coursework project developed for a **Python Programming Course**.
> * **Scope**: Designed as an introductory scripting and automation project to explore Python data structures, `smtplib` networking, MIME formatting, and environment configuration.
> * **Status**: Educational proof-of-concept created for coursework demonstration.

---

## Features

* **Randomized Allocation**: Eliminates bias by shuffling tasks from a defined pool and assigning them across members.
* **Automated SMTP Dispatch**: Connects via TLS to `smtp.gmail.com:587` to format and deliver customized plain-text emails.
* **Environment Security**: Uses `python-dotenv` to keep authentication credentials out of the codebase.

---

## Household Pool & Chores

* **Registered Members**: `Dip Paul`, `Elsewear`, `Rudro`, `Emon`, `Shagor`
* **Task Categories**:
  * Wash dishes
  * Take out the trash
  * Vacuum the living room
  * Clean the bathroom
  * Mow the lawn

---

## Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/](https://github.com/)<your-username>/random-chore-assignment-emailer.git
cd random-chore-assignment-emailer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Credentials
1. Create a `.env` file from the provided example:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and fill in your Gmail address and 16-character Google App Password:
   ```env
   SENDER_EMAIL=your_email@gmail.com
   SENDER_APP_PASSWORD=xxxx xxxx xxxx xxxx
   ```
   *(Generate via Google Account $\rightarrow$ Security $\rightarrow$ 2-Step Verification $\rightarrow$ App Passwords).*

---

## Usage

Run the assignment script:
```bash
python main.py
```

### Terminal Output
```text
========================================
    Random Chore Assignment Emailer     
========================================

--- Assigning Chores to Household Members ---
Assigning 'Vacuum the living room' to Dip Paul (dippaul21dp@gmail.com)...
[SUCCESS] Email sent to dippaul21dp@gmail.com
Assigning 'Wash dishes' to Elsewear (elsewear6@gmail.com)...
[SUCCESS] Email sent to elsewear6@gmail.com
```

---

## Authors

* **Dip Paul** - *Department of Biomedical Engineering, CUET*

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
