# 🎓 Hybrid Student ERP & Analytics System

Welcome to my **Semester 2 milestone project**! This repository features an enterprise-grade Student ERP (Enterprise Resource Planning) system. The project transitions away from traditional command-line scripts by marrying clean backend architecture with a highly responsive, modern data dashboard.

This is part of my ongoing commitment to build a practical, real-world application at the conclusion of every academic semester.

---

## 🚀 The Semester Project Journey
* **Semester 1:** Movie Ticket Booking & Dynamic Seat Layout System (Built in **C**)
* **Semester 2 (This Project):** Institutional Student ERP & Analytics Dashboard (Built in **Python**)

---

## 🛠️ System Architecture & Core Features

This application utilizes a clean **Separation of Concerns**, splitting tracking responsibilities between pure Object-Oriented Programming (OOP) and high-performance data processing:

### 1. 🏛️ Institute Overview & Analytics (Powered by Pandas)
* **Bird's-Eye Metrics:** Automatically computes institutional health data including total enrollment, average global CGPA, and total outstanding dues.
* **Independent Branch Roster (`getlist`):** Dynamically filters and displays full student data based on user-selected branches.
* **Branch Toppers Tracker (`gettoppers`):** Leverages advanced Pandas sorting algorithms to instantly extract and isolate the top 5 academic performers in any given branch.

### 2. 🗂️ Student Management Portal (Powered by OOP)
* **Runtime Object Initialization:** Converts static spreadsheet datasets (`.xlsx`) into active Python `Student` class objects at application runtime.
* **Dynamic Transaction Engine:** Features localized class methods that process secure fee payments, modify student ledger states, and instantly push updated data updates back to the UI.

---

## 💻 Tech Stack Used

* **Language:** Python 3.13
* **Data Analysis Framework:** Pandas (utilizing `openpyxl` for Excel stream compilation)
* **Frontend Interface UI:** Streamlit Web Framework

---

