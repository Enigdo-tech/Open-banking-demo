from datetime import datetime, timedelta
import random
from typing import List, Dict, Any

class PersonaGenerator:
    """
    Enhanced PersonaGenerator with 7-account, 3-institution model.
    Simulates realistic fragmented financial life across multiple banks.
    """
    
    def __init__(self):
        self.personas = {
            "stabilizer": self._generate_stabilizer,
            "hustler": self._generate_hustler,
            "builder": self._generate_builder
        }

    def get_persona_data(self, persona_type: str) -> Dict[str, Any]:
        generator = self.personas.get(persona_type.lower())
        if not generator:
            raise ValueError(f"Persona {persona_type} not found")
        return generator()

    def _generate_stabilizer(self):
        """
        Persona A: The "Stabilizer" (9-5 Worker)
        Sarah Jenkins - $90k salary, stable income, optimizing wealth
        """
        return {
            "profile": {
                "id": "p_stabilizer",
                "name": "Sarah Jenkins",
                "type": "Personal",
                "segment": "Stabilizer",
                "income_annual": 90000,
                "occupation": "Marketing Manager"
            },
            "institutions": [
                {
                    "id": "inst_bigbank",
                    "name": "Bank 1",
                    "type": "Big Bank",
                    "logo": "🏦"
                },
                {
                    "id": "inst_digital",
                    "name": "Bank 2",
                    "type": "Digital Bank",
                    "logo": "🍊"
                },
                {
                    "id": "inst_fintech",
                    "name": "Fintech 1",
                    "type": "Fintech",
                    "logo": "📈"
                }
            ],
            "accounts": [
                # Institution A: Big Bank (TD)
                {
                    "id": "acc_1",
                    "institution_id": "inst_bigbank",
                    "institution_name": "Bank 1",
                    "type": "CHECKING",
                    "balance": 3200.00,
                    "currency": "CAD",
                    "label": "Primary Chequing",
                    "account_number": "****1234",
                    "purpose": "Payroll, Bill Payments"
                },
                {
                    "id": "acc_2",
                    "institution_id": "inst_bigbank",
                    "institution_name": "Bank 1",
                    "type": "SAVINGS",
                    "balance": 15000.00,
                    "currency": "CAD",
                    "label": "High-Interest Savings",
                    "account_number": "****5678",
                    "interest_rate": 4.0,
                    "purpose": "Emergency Fund"
                },
                {
                    "id": "acc_3",
                    "institution_id": "inst_bigbank",
                    "institution_name": "Bank 1",
                    "type": "INVESTMENT",
                    "balance": 45000.00,
                    "currency": "CAD",
                    "label": "RRSP Mutual Funds",
                    "account_number": "****9012",
                    "mer": 2.3,
                    "purpose": "Retirement"
                },
                # Institution B: Digital Bank (Bank 2)
                {
                    "id": "acc_4",
                    "institution_id": "inst_digital",
                    "institution_name": "Bank 2",
                    "type": "CHECKING",
                    "balance": 1850.00,
                    "currency": "CAD",
                    "label": "Daily Spending",
                    "account_number": "****3456",
                    "purpose": "Groceries, Transit"
                },
                {
                    "id": "acc_5",
                    "institution_id": "inst_digital",
                    "institution_name": "Bank 2",
                    "type": "SAVINGS",
                    "balance": 8500.00,
                    "currency": "CAD",
                    "label": "Vacation Pot",
                    "account_number": "****7890",
                    "interest_rate": 3.5,
                    "purpose": "Travel Savings"
                },
                # Institution C: Fintech (Fintech 1)
                {
                    "id": "acc_6",
                    "institution_id": "inst_fintech",
                    "institution_name": "Fintech 1",
                    "type": "CHECKING",
                    "balance": 450.00,
                    "currency": "CAD",
                    "label": "Side-Hustle Account",
                    "account_number": "****2468",
                    "purpose": "Freelance Income"
                },
                {
                    "id": "acc_7",
                    "institution_id": "inst_fintech",
                    "institution_name": "Fintech 1",
                    "type": "INVESTMENT",
                    "balance": 12000.00,
                    "currency": "CAD",
                    "label": "TFSA Growth Portfolio",
                    "account_number": "****1357",
                    "mer": 0.5,
                    "purpose": "Tax-Free Growth"
                }
            ],
            "transactions": self._generate_stabilizer_transactions(),
            "subscriptions": self._generate_subscriptions("stabilizer"),
            "bills": self._generate_bills("stabilizer")
        }

    def _generate_hustler(self):
        """
        Persona B: The "Hustler" (Gig Worker)
        Mike Chen - Irregular income, cash flow management focus
        """
        return {
            "profile": {
                "id": "p_hustler",
                "name": "Mike Chen",
                "type": "Personal",
                "segment": "Hustler",
                "income_annual": 48000,
                "occupation": "Gig Worker (Uber, SkipTheDishes, Upwork)"
            },
            "institutions": [
                {
                    "id": "inst_bigbank",
                    "name": "Bank 1",
                    "type": "Big Bank",
                    "logo": "🏦"
                },
                {
                    "id": "inst_digital",
                    "name": "Bank 2",
                    "type": "Digital Bank",
                    "logo": "💳"
                },
                {
                    "id": "inst_fintech",
                    "name": "Fintech 1",
                    "type": "Fintech",
                    "logo": "📈"
                }
            ],
            "accounts": [
                # Institution A: Big Bank (RBC)
                {
                    "id": "acc_1",
                    "institution_id": "inst_bigbank",
                    "institution_name": "Bank 1",
                    "type": "CHECKING",
                    "balance": 450.00,
                    "currency": "CAD",
                    "label": "Primary Chequing",
                    "account_number": "****4321",
                    "purpose": "Main Account"
                },
                {
                    "id": "acc_2",
                    "institution_id": "inst_bigbank",
                    "institution_name": "Bank 1",
                    "type": "SAVINGS",
                    "balance": 1200.00,
                    "currency": "CAD",
                    "label": "Emergency Savings",
                    "account_number": "****8765",
                    "interest_rate": 2.5,
                    "purpose": "Emergency Fund"
                },
                {
                    "id": "acc_3",
                    "institution_id": "inst_bigbank",
                    "institution_name": "Bank 1",
                    "type": "LOAN",
                    "balance": 30000.00,
                    "currency": "CAD",
                    "label": "Student Loan",
                    "account_number": "****2109",
                    "purpose": "Debt"
                },
                # Institution B: Digital Bank (Bank 2)
                {
                    "id": "acc_4",
                    "institution_id": "inst_digital",
                    "institution_name": "Bank 2",
                    "type": "CHECKING",
                    "balance": 2100.00,
                    "currency": "CAD",
                    "label": "Daily Spending",
                    "account_number": "****6543",
                    "purpose": "Groceries, Bills"
                },
                {
                    "id": "acc_5",
                    "institution_id": "inst_digital",
                    "institution_name": "Bank 2",
                    "type": "SAVINGS",
                    "balance": 800.00,
                    "currency": "CAD",
                    "label": "Goal Savings",
                    "account_number": "****0987",
                    "interest_rate": 3.0,
                    "purpose": "Short-term Goals"
                },
                # Institution C: Fintech (Fintech 1)
                {
                    "id": "acc_6",
                    "institution_id": "inst_fintech",
                    "institution_name": "Fintech 1",
                    "type": "CHECKING",
                    "balance": 1850.00,
                    "currency": "CAD",
                    "label": "Gig Income Account",
                    "account_number": "****8642",
                    "purpose": "Uber, Skip, Upwork Payouts"
                },
                {
                    "id": "acc_7",
                    "institution_id": "inst_fintech",
                    "institution_name": "Fintech 1",
                    "type": "INVESTMENT",
                    "balance": 3200.00,
                    "currency": "CAD",
                    "label": "Micro-Investing",
                    "account_number": "****7531",
                    "mer": 0.4,
                    "purpose": "Weekly $50 Auto-Invest"
                }
            ],
            "transactions": self._generate_hustler_transactions(),
            "subscriptions": self._generate_subscriptions("hustler"),
            "bills": self._generate_bills("hustler")
        }

    def _generate_builder(self):
        """
        Persona C: The "Builder" (Small Business Owner)
        Elena Rodriguez - $350k/mo turnover, payroll management
        """
        return {
            "profile": {
                "id": "p_builder",
                "name": "Elena Rodriguez",
                "type": "Business",
                "segment": "Builder",
                "turnover_monthly": 350000,
                "occupation": "Small Business Owner (Marketing Agency)"
            },
            "institutions": [
                {
                    "id": "inst_bigbank",
                    "name": "Bank 1",
                    "type": "Big Bank",
                    "logo": "🏦"
                },
                {
                    "id": "inst_digital",
                    "name": "Bank 2",
                    "type": "Digital Bank",
                    "logo": "💼"
                },
                {
                    "id": "inst_fintech",
                    "name": "Fintech 1",
                    "type": "Fintech",
                    "logo": "📈"
                }
            ],
            "accounts": [
                # Institution A: Big Bank (Bank 1)
                {
                    "id": "acc_1",
                    "institution_id": "inst_bigbank",
                    "institution_name": "Bank 1",
                    "type": "CHECKING",
                    "balance": 85000.00,
                    "currency": "CAD",
                    "label": "Business Operating",
                    "account_number": "****5555",
                    "purpose": "Daily Operations"
                },
                {
                    "id": "acc_2",
                    "institution_id": "inst_bigbank",
                    "institution_name": "Bank 1",
                    "type": "SAVINGS",
                    "balance": 50000.00,
                    "currency": "CAD",
                    "label": "Business Reserve",
                    "account_number": "****6666",
                    "interest_rate": 3.5,
                    "purpose": "Emergency Reserve"
                },
                {
                    "id": "acc_3",
                    "institution_id": "inst_bigbank",
                    "institution_name": "Bank 1",
                    "type": "INVESTMENT",
                    "balance": 120000.00,
                    "currency": "CAD",
                    "label": "Corporate RRSP",
                    "account_number": "****7777",
                    "mer": 1.8,
                    "purpose": "Retirement Planning"
                },
                # Institution B: Digital Bank (Bank 2)
                {
                    "id": "acc_4",
                    "institution_id": "inst_digital",
                    "institution_name": "Bank 2",
                    "type": "CHECKING",
                    "balance": 25000.00,
                    "currency": "CAD",
                    "label": "Vendor Payments",
                    "account_number": "****8888",
                    "purpose": "Supplier Payments"
                },
                {
                    "id": "acc_5",
                    "institution_id": "inst_digital",
                    "institution_name": "Bank 2",
                    "type": "SAVINGS",
                    "balance": 40000.00,
                    "currency": "CAD",
                    "label": "Tax Reserve",
                    "account_number": "****9999",
                    "interest_rate": 4.0,
                    "purpose": "Quarterly Tax Payments"
                },
                # Institution C: Fintech (Fintech 1)
                {
                    "id": "acc_6",
                    "institution_id": "inst_fintech",
                    "institution_name": "Fintech 1",
                    "type": "CHECKING",
                    "balance": 45000.00,
                    "currency": "CAD",
                    "label": "Payroll Account",
                    "account_number": "****1111",
                    "purpose": "Employee Payroll"
                },
                {
                    "id": "acc_7",
                    "institution_id": "inst_fintech",
                    "institution_name": "Fintech 1",
                    "type": "INVESTMENT",
                    "balance": 75000.00,
                    "currency": "CAD",
                    "label": "Growth Portfolio",
                    "account_number": "****2222",
                    "mer": 0.5,
                    "purpose": "Business Growth Fund"
                }
            ],
            "transactions": self._generate_builder_transactions(),
            "subscriptions": self._generate_subscriptions("builder"),
            "bills": self._generate_bills("builder")
        }

    def _generate_stabilizer_transactions(self):
        """Generate transactions across all 7 accounts for Stabilizer"""
        txns = []
        
        # Account 1 (Primary Chequing): Payroll & Bills
        txns.extend([
            {"date": "2023-10-01", "amount": 3461.54, "description": "PAYROLL DEPOSIT - CORP INC", "category": "Income", "account_id": "acc_1", "institution": "Bank 1"},
            {"date": "2023-10-15", "amount": 3461.54, "description": "PAYROLL DEPOSIT - CORP INC", "category": "Income", "account_id": "acc_1", "institution": "Bank 1"},
            {"date": "2023-10-01", "amount": -1850.00, "description": "MORTGAGE PAYMENT", "category": "Housing", "account_id": "acc_1", "institution": "Bank 1"},
            {"date": "2023-10-05", "amount": -127.50, "description": "TORONTO HYDRO", "category": "Utilities", "account_id": "acc_1", "institution": "Bank 1"},
            {"date": "2023-10-08", "amount": -89.99, "description": "ROGERS INTERNET", "category": "Utilities", "account_id": "acc_1", "institution": "Bank 1"},
        ])
        
        # Account 4 (Daily Spending): Groceries, Transit
        txns.extend([
            {"date": "2023-10-03", "amount": -125.50, "description": "LOBLAWS", "category": "Groceries", "account_id": "acc_4", "institution": "Bank 2"},
            {"date": "2023-10-07", "amount": -138.00, "description": "METRO GROCERY", "category": "Groceries", "account_id": "acc_4", "institution": "Bank 2"},
            {"date": "2023-10-10", "amount": -156.00, "description": "WHOLE FOODS", "category": "Groceries", "account_id": "acc_4", "institution": "Bank 2"},
            {"date": "2023-10-04", "amount": -3.25, "description": "TTC PRESTO", "category": "Transportation", "account_id": "acc_4", "institution": "Bank 2"},
            {"date": "2023-10-11", "amount": -3.25, "description": "TTC PRESTO", "category": "Transportation", "account_id": "acc_4", "institution": "Bank 2"},
            {"date": "2023-10-06", "amount": -16.99, "description": "NETFLIX", "category": "Entertainment", "account_id": "acc_4", "institution": "Bank 2"},
            {"date": "2023-10-09", "amount": -10.99, "description": "SPOTIFY", "category": "Entertainment", "account_id": "acc_4", "institution": "Bank 2"},
        ])
        
        # Account 6 (Side-Hustle): Freelance income
        txns.extend([
            {"date": "2023-10-12", "amount": 450.00, "description": "UPWORK PAYOUT", "category": "Income", "account_id": "acc_6", "institution": "Fintech 1"},
            {"date": "2023-10-20", "amount": 350.00, "description": "FREELANCE CLIENT - DESIGN", "category": "Income", "account_id": "acc_6", "institution": "Fintech 1"},
        ])
        
        return sorted(txns, key=lambda x: x['date'], reverse=True)

    def _generate_hustler_transactions(self):
        """Generate transactions across all 7 accounts for Hustler"""
        txns = []
        
        # Account 1 (Primary): Minimal activity
        txns.extend([
            {"date": "2023-10-05", "amount": -45.00, "description": "GYM MEMBERSHIP", "category": "Health", "account_id": "acc_1", "institution": "Bank 1"},
        ])
        
        # Account 4 (Daily Spending): Main spending account
        txns.extend([
            {"date": "2023-10-03", "amount": -85.50, "description": "NO FRILLS", "category": "Groceries", "account_id": "acc_4", "institution": "Bank 2"},
            {"date": "2023-10-09", "amount": -92.00, "description": "FOOD BASICS", "category": "Groceries", "account_id": "acc_4", "institution": "Bank 2"},
            {"date": "2023-10-15", "amount": -78.50, "description": "FRESHCO", "category": "Groceries", "account_id": "acc_4", "institution": "Bank 2"},
            {"date": "2023-10-06", "amount": -18.99, "description": "NETFLIX", "category": "Entertainment", "account_id": "acc_4", "institution": "Bank 2"},
            {"date": "2023-10-10", "amount": -10.99, "description": "SPOTIFY", "category": "Entertainment", "account_id": "acc_4", "institution": "Bank 2"},
            {"date": "2023-10-08", "amount": -127.50, "description": "TORONTO HYDRO", "category": "Utilities", "account_id": "acc_4", "institution": "Bank 2"},
        ])
        
        # Account 6 (Gig Income): Multiple irregular payouts
        txns.extend([
            {"date": "2023-10-02", "amount": 287.50, "description": "UBER PAYOUT", "category": "Income", "account_id": "acc_6", "institution": "Fintech 1"},
            {"date": "2023-10-05", "amount": 156.00, "description": "SKIPTHEDISHES PAYOUT", "category": "Income", "account_id": "acc_6", "institution": "Fintech 1"},
            {"date": "2023-10-08", "amount": 312.00, "description": "UBER PAYOUT", "category": "Income", "account_id": "acc_6", "institution": "Fintech 1"},
            {"date": "2023-10-12", "amount": 450.00, "description": "UPWORK ESCROW", "category": "Income", "account_id": "acc_6", "institution": "Fintech 1"},
            {"date": "2023-10-15", "amount": 198.50, "description": "UBER PAYOUT", "category": "Income", "account_id": "acc_6", "institution": "Fintech 1"},
            {"date": "2023-10-18", "amount": 225.00, "description": "SKIPTHEDISHES PAYOUT", "category": "Income", "account_id": "acc_6", "institution": "Fintech 1"},
            {"date": "2023-10-20", "amount": 375.00, "description": "UPWORK ESCROW", "category": "Income", "account_id": "acc_6", "institution": "Fintech 1"},
            {"date": "2023-10-07", "amount": -50.00, "description": "WEALTHSIMPLE AUTO-INVEST", "category": "Investments", "account_id": "acc_6", "institution": "Fintech 1"},
            {"date": "2023-10-14", "amount": -50.00, "description": "WEALTHSIMPLE AUTO-INVEST", "category": "Investments", "account_id": "acc_6", "institution": "Fintech 1"},
            {"date": "2023-10-21", "amount": -50.00, "description": "WEALTHSIMPLE AUTO-INVEST", "category": "Investments", "account_id": "acc_6", "institution": "Fintech 1"},
        ])
        
        return sorted(txns, key=lambda x: x['date'], reverse=True)

    def _generate_builder_transactions(self):
        """Generate transactions across all 7 accounts for Builder"""
        txns = []
        
        # Account 1 (Business Operating): Client payments & expenses
        txns.extend([
            {"date": "2023-10-01", "amount": 45000.00, "description": "CLIENT INVOICE #1001", "category": "Income", "account_id": "acc_1", "institution": "Bank 1"},
            {"date": "2023-10-15", "amount": 38000.00, "description": "CLIENT INVOICE #1002", "category": "Income", "account_id": "acc_1", "institution": "Bank 1"},
            {"date": "2023-10-05", "amount": -2500.00, "description": "OFFICE RENT", "category": "Business", "account_id": "acc_1", "institution": "Bank 1"},
            {"date": "2023-10-08", "amount": -450.00, "description": "STAPLES - OFFICE SUPPLIES", "category": "Business", "account_id": "acc_1", "institution": "Bank 1"},
        ])
        
        # Account 4 (Vendor Payments)
        txns.extend([
            {"date": "2023-10-10", "amount": -3500.00, "description": "VENDOR PAYMENT #101", "category": "Business", "account_id": "acc_4", "institution": "Bank 2"},
            {"date": "2023-10-12", "amount": -2800.00, "description": "VENDOR PAYMENT #102", "category": "Business", "account_id": "acc_4", "institution": "Bank 2"},
            {"date": "2023-10-18", "amount": -4200.00, "description": "VENDOR PAYMENT #103", "category": "Business", "account_id": "acc_4", "institution": "Bank 2"},
        ])
        
        # Account 6 (Payroll)
        txns.extend([
            {"date": "2023-10-15", "amount": -12000.00, "description": "PAYROLL RUN - 4 EMPLOYEES", "category": "Payroll", "account_id": "acc_6", "institution": "Fintech 1"},
        ])
        
        return sorted(txns, key=lambda x: x['date'], reverse=True)

    def _generate_subscriptions(self, persona_type: str):
        """Generate subscription data across multiple accounts"""
        base_subs = [
            {"name": "Netflix", "amount": 16.99 if persona_type == "hustler" else 14.99, "account_id": "acc_4", "status": "increased" if persona_type == "hustler" else "stable", "change": 2.00 if persona_type == "hustler" else None},
            {"name": "Spotify", "amount": 10.99, "account_id": "acc_4", "status": "stable", "change": None},
        ]
        
        if persona_type == "stabilizer":
            base_subs.append({"name": "Amazon Prime", "amount": 9.99, "account_id": "acc_1", "status": "stable", "change": None})
            base_subs.append({"name": "Apple iCloud", "amount": 2.99, "account_id": "acc_6", "status": "stable", "change": None})
        elif persona_type == "hustler":
            base_subs.append({"name": "Gym Membership", "amount": 45.00, "account_id": "acc_1", "status": "increased", "change": 5.00})
        
        return base_subs

    def _generate_bills(self, persona_type: str):
        """Generate bill data"""
        bills = [
            {"id": "bill_1", "name": "Toronto Hydro", "amount": 127.50, "due_date": "2023-11-05", "account_id": "acc_1"},
            {"id": "bill_2", "name": "Rogers Internet", "amount": 89.99, "due_date": "2023-11-08", "account_id": "acc_1"},
        ]
        
        if persona_type == "stabilizer":
            bills.append({"id": "bill_3", "name": "Enbridge Gas", "amount": 156.20, "due_date": "2023-11-12", "account_id": "acc_1"})
        
        return bills
