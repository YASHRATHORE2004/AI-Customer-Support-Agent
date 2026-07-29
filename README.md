# AI Customer Support Agent

An enterprise-grade, intelligent customer service agent system powered by **Google Gemini 2.0 Flash** (via OpenAI AgentKit compatibility). This system automates multi-step workflows, integrates with external tools (like order lookups and refunds), and maintains stateful conversation memory for a seamless customer support experience.

## 🏗️ Architecture & Features

- **Conversational AI**: Uses the Gemini 2.0 Flash model to interact with users naturally and empathetically.
- **Tool Integration**: Capable of dynamically routing queries to specific tools, such as:
  - `lookup_order`: Checks the status of an order.
  - `process_refund`: Processes a refund if the item is eligible.
  - `check_inventory`: Verifies product availability.
- **Stateful Memory**: Maintains context across the entire conversation to avoid repeating questions.
- **Production-Ready**: Includes built-in error handling and fallback mechanisms.

## 🚀 Setup & Installation

### 1. Requirements
- Python 3.11+
- A Google Gemini API Key

### 2. Installation

Clone the repository and install the dependencies in a virtual environment:

```bash
git clone https://github.com/YASHRATHORE2004/AI-Customer-Support-Agent.git
cd AI-Customer-Support-Agent

# Create and activate a virtual environment
python -m venv venv
# Windows
.\venv\Scripts\Activate.ps1
# macOS/Linux
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

### 3. Configuration

Create a `.env` file in the root directory and configure it for Gemini:

```properties
OPENAI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
OPENAI_API_KEY=your-gemini-api-key-here
DEFAULT_MODEL=gemini-2.0-flash

# Disable these to save API calls and avoid Free-Tier Rate Limits
ENABLE_EVALUATION=false
ENABLE_SENTIMENT_ANALYSIS=false

LOG_LEVEL=INFO
MAX_CONVERSATION_HISTORY=50
DEFAULT_TEMPERATURE=0.7
```

## 🎮 Running the Agent

You can test the agent interactively using the simplified test script:

```bash
python test_gemini.py
```

For advanced workflows and testing multiple conversation scenarios:

```bash
python scripts/run_demo.py --demo-type basic
```
