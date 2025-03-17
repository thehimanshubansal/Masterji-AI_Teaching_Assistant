# 👨‍🏫 Masterji - AI Chatbot

Masterji is a AI Teaching assistant cum chatbot designed to provide educational assistance to students via Telegram. It can generate math quizzes, provide explanations, summaries, and examples for various topics.

## 📝 About Masterji
1️⃣ *Conversational AI* – Can understand natural language and respond like a teacher.  
2️⃣ *Topic-Specific Help* – Can assist with any topic provided by the user and more.  
3️⃣ *Interactive Learning* – Quizzes, examples, and explanations.  
4️⃣ *Student Engagement* – Encouraging responses, chat and motivation. 

🟢 It is built using *Dialogflow for NLP processing* , *FastAPI as the backend webhook* and Integrates with *Google Gemini AI for content generation*, which allows it to generate **dynamic responses* based on student queries.  


## 🛠 Tech Stack & Tools Used
  - Backend: FastAPI (Python)
  - Frontend: HTML (embedded Dialogflow bot)
  - AI Services: Google Gemini AI
  - Backend Deployment: Render
  - Messaging Platform: Telegram (via Bot API)
  - Webhook Handling and Creation: Dialogflow Webhook

## 🌟 Masterji's Features
*Masterji* is your *AI-powered teacher chatbot*, designed to assist students with learning by:  
✅ *Explaining topics*  
✅ *Providing examples*  
✅ *Summarizing lessons*  
✅ *Generating quizzes*  
✅ *Checking answers*  
✅ *Offering chatting & motivation*  


## ▶ How to Use
1. **Telegram:**
   - Open [Masterji AI Bot](http://t.me/Masterji_AIbot) on Telegram.
   - Start the bot by clicking "Start".
   - Ask Masterji and It will provide explanations, quizzes, or summaries and much more based on your input.

2. **Local Web Interface (HTML Page):**
   - Open the masterji_index.html file in your browser.
   - This file contains an embedded Dialogflow chatbot interface.
   - You can interact with Masterji directly from the webpage.

## 📥 Prerequisites
- Python 3.8+
- Virtual environment (recommended)

##  🚀 Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/thehimanshubansal/masterji.git
   cd masterji
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   uvicorn masterji:app --host 0.0.0.0 --port 8000
   ```
## 📲 Available on Telegram: [Masterji AI Bot](http://t.me/Masterji_AIbot)


## ⚠️ Important Note:
#### 🔚 API Endpoints
| Method | Endpoint       | Description |
|--------|--------------|-------------|
| POST   | `/webhook`   | Handles Dialogflow requests |

## 📜 License
This project is open-source under the [MIT License](LICENSE).

---

## ❤️ Final Words
Made with love by me (Himanshu Bansal). Thank you for reviewing our project!

