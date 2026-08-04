# EcoTrack ERP - Waste Management & Payroll Platform

EcoTrack ERP is an integrated enterprise resource planning system designed to streamline **hazardous waste tracking**, **Tunisian fiscal compliance**, and **internal employee attendance and payroll management**.

---

## 🎯 Primary Objective

The core goal of EcoTrack ERP is to provide a single, centralized workspace for managing corporate operations, regulatory compliance, and workforce tracking:

1. **Environmental & Hazardous Waste Compliance (BSDD Tracking):**
   - Digitally manage waste manifests (*Bordereau de Suivi des Déchets Dangereux*).
   - Automate tax and invoice calculations based on Tunisian corporate fiscal laws.
   - Instantly generate official legal documentation, including **Invoices (Factures)** and **Certificates of Destruction (Attestations de Destruction)**.

2. **Workforce & Payroll Administration:**
   - Maintain an active directory of staff profiles and assigned privileges.
   - Record daily attendance across monthly calendar matrices.
   - Calculate gross and net weekly wages while managing salary advance ledgers.

3. **Secure Multi-Role Workspace:**
   - Enforce Role-Based Access Control (RBAC) to ensure data confidentiality across operational, HR, and managerial levels.

---

## ✨ Key Features

### 🏢 Waste Tracking & Fiscal Engine
- **Client Directory:** Manages public and private sector clients with unique tax identifiers (*Matricule Fiscale*) and BSDD numbers.
- **Dynamic Fiscal Engine:** 
  - **Rubbish Base Services:** Standard 19% TVA rate.
  - **Separate Transport Billing:** Optional 7% TVA rate.
  - **Sector-Based Taxing:** Automatically applies fiscal stamps (*Timbre Fiscal*) for private sector transactions while waiving them for public institutions.
- **Live Receipt & Attestation Generator:** Built-in modal viewer that dynamically formats and prints official invoices and certificates of destruction.

### 👥 Staff & Master Payroll
- **Interactive Attendance Matrix:** Visual monthly calendar to record daily presence, holidays, and unjustified absences.
- **Automated Wage Calculation:** Real-time computation of weekly gross pay based on individual daily rates.
- **Salary Advances Ledger:** Track, deduct, and log employee advance payments against monthly earnings.

### 🔐 Multi-Tier Security & Navigation
- **Role-Based Access Control (RBAC):** Restricts interface tools into **Read**, **Write**, **Delete**, and **Admin** privilege tiers.
- **Dual Login Portals:** Separate authentication flows for operational staff and HR Master Session key overrides.
- **Light/Dark Mode & Internationalization:** Instant theme switching and full English/French language toggling.

---

## 🛠️ Technical Stack

- **Backend:** Python (Flask framework) & SQLite (`company_erp.db`) for backend database interactions and access control enforcement.
- **Frontend:** Vanilla HTML5, CSS3 (CSS Custom Properties for dynamic theme switching), and JavaScript (ES6+).
- **Client Storage & Syncing:** Localized browser state management (`localStorage`) integrated with server-side form endpoints.

---

## 🚀 Quick Start Guide

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/your-username/ecotrack-erp.git](https://github.com/your-username/ecotrack-erp.git)
   cd ecotrack-erp
