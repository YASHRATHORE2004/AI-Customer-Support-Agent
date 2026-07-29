"""
Performance monitoring and reporting example.
"""

import os
import sys
import json
from datetime import datetime
from dotenv import load_dotenv

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from ai_customer_agent import CustomerServiceAgent, AgentConfig


def main():
    """Demonstrate performance monitoring and reporting."""
    print("🤖 AI Customer Service Agent - Performance Monitoring")
    print("=" * 50)

    # Load environment variables
    load_dotenv()

    # Initialize agent with evaluation enabled
    config = AgentConfig(enable_evaluation=True)
    agent = CustomerServiceAgent(config=config)

    print(f"✅ Agent initialized (Evaluation: {config.enable_evaluation})")
    print()

    # Simulate a series of interactions
    test_interactions = [
        ("Hello, I need help with my order", "CUST-001"),
        ("Where is my order ORD-12345?", "CUST-001"),
        ("The product is damaged, I want a refund", "CUST-001"),
        ("What smart watches do you have?", "CUST-002"),
        ("I have a billing issue with my account", "CUST-003"),
        ("Thank you for your help!", "CUST-001"),
    ]

    print("🔄 Simulating customer interactions...")
    for user_message, customer_id in test_interactions:
        response = agent.chat(user_message, customer_id)
        print(f"👤 {customer_id}: {user_message}")
        print(f"🤖: {response[:80]}...")
        print()

    # Generate various reports
    print("📊 PERFORMANCE REPORTS")
    print("=" * 50)

    # Full report
    print("\n📈 Full Performance Report (All interactions)")
    print("-" * 40)
    full_report = agent.get_performance_report()
    print(full_report)

    # Recent report
    print("\n📈 Recent Performance Report (Last 3 interactions)")
    print("-" * 40)
    recent_report = agent.get_performance_report(last_n_interactions=3)
    print(recent_report)

    # Export evaluation data
    print("\n💾 Exporting Evaluation Data")
    print("-" * 40)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    export_file = f"evaluation_export_{timestamp}.json"

    if agent.evaluator:
        agent.evaluator.save_evaluation_data(export_file)
        print(f"✅ Evaluation data exported to: {export_file}")

        # Show exported data structure
        with open(export_file, "r") as f:
            export_data = json.load(f)

        print(
            f"📁 Exported {len(export_data['evaluation_results'])} evaluation results"
        )

    # Agent statistics
    print("\n🔢 AGENT STATISTICS")
    print("=" * 50)

    info = agent.get_agent_info()
    print(f"Total Interactions: {info['total_interactions']}")
    print(f"Total Tool Calls: {info['total_tool_calls']}")
    print(
        f"Tool Usage Rate: {info['total_tool_calls'] / max(info['total_interactions'], 1):.1%}"
    )

    if agent.metadata.sentiment_scores:
        avg_sentiment = sum(agent.metadata.sentiment_scores) / len(
            agent.metadata.sentiment_scores
        )
        print(f"Average Sentiment: {avg_sentiment:.2f}")

    # Conversation insights
    print("\n💡 CONVERSATION INSIGHTS")
    print("=" * 50)

    summary = agent.get_conversation_summary()
    print(summary)


if __name__ == "__main__":
    main()
