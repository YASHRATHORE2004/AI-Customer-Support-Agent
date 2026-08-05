import os
import sys
from dotenv import load_dotenv

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from ai_customer_agent import CustomerServiceAgent


def main():
    load_dotenv()
    print("🤖 Initializing agent...")
    agent = CustomerServiceAgent()

    print("\n✅ Agent ready! Testing a single query...")

    message = "Hi, I'd like to check the status of my order ORD-12345"
    print(f"👤 User: {message}")

    response = agent.chat(message, customer_id="CUST-001")
    print(f"🤖 Agent: {response}")


if __name__ == "__main__":
    main()
