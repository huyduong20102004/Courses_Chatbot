# index.html :

<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AI Course Chatbot</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
  <style>
    @keyframes blink {
      0%, 100% { opacity: 0.3; }
      50% { opacity: 1; }
    }
  </style>
  <link rel="icon" type="image/png" href="{{ url_for('static', filename='favicon.png') }}" />
  <!-- Thêm Font Awesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
</head>
<body>
  <!-- Main content -->
  <div class="content">
    <header class="header">
      <h1>Chào mừng đến với Khóa học AI</h1>
      <p>Khám phá thế giới trí tuệ nhân tạo với sự hỗ trợ từ chatbot thông minh của chúngLum chúng tôi!</p>
    </header>
  </div>

  <!-- Chatbot toggle button -->
  <button id="chatbot-btn" class="chatbot-btn" title="Mở chatbot AI" aria-label="Mở chatbot AI">
    <span class="chatbot-icon"><i class="fas fa-robot"></i></span>
  </button>

  <!-- Chatbot popup -->
  <div id="chat-popup" class="chat-popup hidden">
    <!-- Chat header -->
    <div class="chat-header">
      <div class="chat-header-content" style="display: flex; align-items: center; gap: 10px; margin-right: auto;">
        <div style="background-color: #fff; border-radius: 50%; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center;">
          <i class="fas fa-robot" style="font-size: 20px; color: #4f46e5; line-height: 1; vertical-align: middle;"></i>
        </div>
        <div style="line-height: 1.2;">
          <h2 style="margin: 0; font-size: 16px;">AI Chatbot - Trợ lý Khoá học</h2>
          <div class="status-indicator" style="display: flex; align-items: center; gap: 6px;">
            <span class="status-dot" style="width: 8px; height: 8px; background-color: #00c853; border-radius: 50%; display: inline-block;"></span>
            <span class="status-text" style="font-size: 12px; color: #FFFFFF;">Đang trực tuyến</span>
          </div>
        </div>
      </div>
      <button id="close-btn" class="icon-btn" title="Đóng chatbot" aria-label="Đóng chatbot" style="margin-left: auto;">
        <span>✖</span>
      </button>
    </div>

    <!-- Chat body -->
    <div id="chat-box" class="chat-box">
      <div class="welcome-message">
        <div class="welcome-header" style="display: flex; align-items: center; gap: 10px;">
          <i class="fas fa-robot" style="font-size: 28px; color: #4f46e5;"></i>
          <h3 style="margin: 0;">Xin chào! Tôi là trợ lý AI</h3>
        </div>
        <p>Tôi có thể giúp gì cho bạn về khóa học Trí tuệ nhân tạo?</p>
        <div class="quick-questions">
          <button class="quick-btn" data-question="Khóa học AI gồm những nội dung gì?">Khóa học gồm nội dung gì?</button>
          <button class="quick-btn" data-question="Tôi cần chuẩn bị gì trước khi học?">Cần chuẩn bị gì?</button>
          <button class="quick-btn" data-question="Lộ trình học AI như thế nào?">Lộ trình học tập</button>
          <button class="quick-btn" data-question="Tôi có thể làm dự án gì với AI?">Dự án thực hành</button>
        </div>
      </div>
    </div>

    <!-- Typing indicator với avatar và 3 chấm -->
    <div id="typing-indicator" class="chat-message bot-message typing hidden" style="align-items: center; gap: 10px; padding: 8px 10px;">
      <div style="background-color: #fff; border-radius: 50%; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 4px rgba(0,0,0,0.1);">
        <i class="fas fa-robot" style="font-size: 18px; color: #4f46e5;"></i>
      </div>
      <div style="background-color: #f3f4f6; border-radius: 20px; padding: 6px 12px; display: flex; gap: 4px; align-items: center; vertical-align: middle;">
        <div class="typing-dot" style="width: 6px; height: 6px; background-color: #4f46e5; border-radius: 50%; animation: blink 1.4s infinite;"></div>
        <div class="typing-dot" style="width: 6px; height: 6px; background-color: #4f46e5; border-radius: 50%; animation: blink 1.4s infinite 0.2s;"></div>
        <div class="typing-dot" style="width: 6px; height: 6px; background-color: #4f46e5; border-radius: 50%; animation: blink 1.4s infinite 0.4s;"></div>
      </div>
    </div>

    <!-- Chat input -->
    <div class="chat-input">
      <div class="input-wrapper">
        <textarea 
          id="user-input" 
          placeholder="Nhập câu hỏi của bạn..." 
          rows="1"
          aria-label="Nhập câu hỏi"
        ></textarea>
        <div class="input-controls">
          <button id="send-btn" class="icon-btn primary" title="Gửi câu hỏi" aria-label="Gửi câu hỏi">
            <svg class="icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M22 2L11 13" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M22 2L15 22L11 13L2 9L22 2Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Chat controls -->
    <div class="chat-controls-bottom">
      <button id="history-btn" class="icon-btn" title="Lịch sử trò chuyện" aria-label="Lịch sử trò chuyện">
        <svg class="icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 8V12L15 15" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M12 21C16.9706 21 21 16.9706 21 12C21 7.02944 16.9706 3 12 3C7.02944 3 3 7.02944 3 12C3 16.9706 7.02944 21 12 21Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
      <button id="minimize-btn" class="icon-btn" title="Thu nhỏ chatbot" aria-label="Thu nhỏ chatbot">
        <svg class="icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M5 15H19" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
    </div>
  </div>

  <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>



# css



/* Global styles */
:root {
  --primary: #2563eb;
  --primary-dark: #1d4ed8;
  --secondary: #8b5cf6;
  --text: #1f2937;
  --text-light: #6b7280;
  --bg: #f9fafb;
  --bg-light: #ffffff;
  --border: #e5e7eb;
  --success: #10b981;
  --error: #ef4444;
  --warning: #f59e0b;
  --bot-bg: #f3f4f6;
  --user-bg: #dbeafe;
  --shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.15);
  --radius: 12px;
  --radius-sm: 8px;
  --transition: all 0.3s ease;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
  background: linear-gradient(135deg, #f0f4f8, #e6f0ff);
  margin: 0;
  padding: 0;
  color: var(--text);
  line-height: 1.6;
}

/* Main content */
.content {
  padding: 80px 20px;
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
}

.header h1 {
  font-size: 2.8rem;
  font-weight: 800;
  color: var(--primary-dark);
  margin-bottom: 1rem;
  background: linear-gradient(90deg, var(--primary), var(--secondary));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.header p {
  font-size: 1.2rem;
  color: var(--text-light);
  max-width: 600px;
  margin: 0 auto;
}

/* Chatbot button */
.chatbot-btn {
  position: fixed;
  bottom: 30px;
  right: 30px;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  color: white;
  border: none;
  padding: 16px 24px;
  border-radius: 50px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 10px;
  box-shadow: var(--shadow-lg);
  transition: var(--transition);
  z-index: 1000;
  animation: pulse 2s infinite;
}

.chatbot-btn:hover {
  transform: translateY(-3px) scale(1.05);
  box-shadow: 0 10px 25px rgba(37, 99, 235, 0.35);
}

.chatbot-icon {
  font-size: 1.8rem;
}

.chatbot-text {
  display: none;
  font-weight: 600;
}

.notification-badge {
  position: absolute;
  top: -5px;
  right: -5px;
  background-color: var(--error);
  color: white;
  font-size: 0.7rem;
  font-weight: 700;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

@media (min-width: 768px) {
  .chatbot-text {
    display: inline;
  }
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(37, 99, 235, 0.5);
  }
  70% {
    box-shadow: 0 0 0 12px rgba(37, 99, 235, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(37, 99, 235, 0);
  }
}

/* Chat popup */
.chat-popup {
  position: fixed;
  bottom: 90px;
  right: 30px;
  width: 90%;
  max-width: 420px;
  background-color: var(--bg-light);
  border-radius: var(--radius);
  box-shadow: var(--shadow-lg);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  transition: var(--transition);
  opacity: 0;
  transform: translateY(20px);
  z-index: 1001;
  height: 75vh;
  max-height: 650px;
}

.chat-popup:not(.hidden) {
  opacity: 1;
  transform: translateY(0);
}

/* Minimized state */
.chat-popup.minimized {
  height: 60px;
  max-height: 60px;
  overflow: hidden;
}

.chat-popup.minimized .chat-header,
.chat-popup.minimized .chat-box,
.chat-popup.minimized .chat-input,
.chat-popup.minimized .chat-controls {
  display: none;
}

/* Chat header */
.chat-header {
  background: linear-gradient(90deg, var(--primary), var(--secondary));
  color: white;
  padding: 16px 20px;
  display: flex;
  justify-content: space-between; /* NEW: chia trái và phải */
  align-items: center;
}


.chat-header-content {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.95rem;
}

.ai-icon {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background-color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px; /* bạn có thể điều chỉnh theo ý */
  color: var(--primary);
  box-shadow: 0 0 0 1px var(--border);
  line-height: 1;
  vertical-align: middle;
}




.status-indicator {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-top: 4px;
}

.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: #4ade80;
  animation: pulse-dot 1.5s infinite;
}

.status-text {
  font-size: 0.85rem;
  font-weight: 500;
  opacity: 0.9;
}

.icon-btn {
  background: none;
  border: none;
  color: white;
  cursor: pointer;
  padding: 6px;
  transition: var(--transition);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
}

.icon-btn:hover {
  background-color: rgba(255, 255, 255, 0.2);
}

.icon-btn.primary {
  background-color: var(--primary);
  color: white;
}

.icon-btn.primary:hover {
  background-color: var(--primary-dark);
}

.icon {
  width: 20px;
  height: 20px;
}

@keyframes pulse-dot {
  0% {
    opacity: 0.6;
  }
  50% {
    opacity: 1;
  }
  100% {
    opacity: 0.6;
  }
}

/* Chat box */
.chat-box {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  background-color: var(--bg);
  display: flex;
  flex-direction: column;
  gap: 15px;
}

/* Welcome message */
.welcome-message {
  background-color: var(--bg-light);
  border-radius: var(--radius-sm);
  padding: 20px;
  box-shadow: var(--shadow);
  text-align: center;
  margin-bottom: 15px;
}

.welcome-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 15px;
}

.welcome-header img {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  margin-bottom: 12px;
}


.welcome-header h3 {
  font-size: 1.3rem;
  color: var(--primary-dark);
  margin-bottom: 5px;
}

.welcome-message p {
  color: var(--text-light);
  margin-bottom: 20px;
}

.quick-questions {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  margin-top: 15px;
}

.quick-btn {
  background-color: var(--bot-bg);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 8px 12px;
  font-size: 0.85rem;
  cursor: pointer;
  transition: var(--transition);
  text-align: center;
}

.quick-btn:hover {
  background-color: var(--user-bg);
  border-color: var(--primary);
}

/* Chat message */
.chat-message {
  display: flex;
  max-width: 85%;
  animation: fadeIn 0.3s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.bot-message {
  align-self: flex-start;
}

.user-message {
  align-self: flex-end;
}

.message-content {
  padding: 12px 16px;
  border-radius: 18px;
  position: relative;
  box-shadow: var(--shadow);
}

.bot-message .message-content {
  background-color: var(--bot-bg);
  color: var(--text);
  border-radius: 18px 18px 18px 4px;
}

.user-message .message-content {
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  color: white;
  border-radius: 18px 18px 4px 18px;
}

.message-content p {
  margin: 0;
  line-height: 1.5;
}

.message-time {
  font-size: 0.7rem;
  opacity: 0.7;
  display: block;
  text-align: right;
  margin-top: 5px;
}

/* === Typing Indicator === */
#typing-indicator {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 10px 0;
}

#typing-indicator .typing-dot {
  animation: blink 1.4s infinite;
}

/* Avatar bot */
#typing-indicator .avatar {
  width: 32px;
  height: 32px;
  background-color: #fff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

/* Bubble chứa 3 chấm */
#typing-indicator .typing-bubble {
  background-color: var(--bot-bg);
  padding: 8px 12px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  gap: 6px;
  box-shadow: var(--shadow);
  height: 20px;
}

/* Ẩn khi không cần */
#typing-indicator.hidden {
  display: none;
}

/* Dấu 3 chấm */
.typing-dot {
  width: 6px;
  height: 6px;
  background-color: var(--primary);
  border-radius: 50%;
  animation: bounce 1.4s infinite cubic-bezier(0.6, 0.05, 0.2, 0.9);
}


/* Độ trễ từng chấm */
.typing-dot:nth-child(1) {
  animation-delay: 0s;
}
.typing-dot:nth-child(2) {
  animation-delay: 0.2s;
}
.typing-dot:nth-child(3) {
  animation-delay: 0.4s;
}

/* Animation nhảy lên xuống mượt */
@keyframes bounce {
  0%, 100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-6px);
  }
  60% {
    transform: translateY(3px);
  }
  80% {
    transform: translateY(-2px);
  }
}





/* Chat input */
.chat-input {
  padding: 15px;
  background: var(--bg-light);
  border-top: 1px solid var(--border);
}

.input-wrapper {
  display: flex;
  align-items: flex-end;
  background: var(--bg);
  border-radius: var(--radius);
  padding: 10px;
  transition: var(--transition);
}

.input-wrapper:focus-within {
  box-shadow: 0 0 0 2px var(--primary);
}

#user-input {
  flex: 1;
  padding: 8px 0;
  border: none;
  outline: none;
  background: transparent;
  font-size: 0.95rem;
  resize: none;
  line-height: 1.5;
  max-height: 120px;
  font-family: inherit;
}

.input-controls {
  display: flex;
  gap: 5px;
  margin-left: 8px;
}

/* Chat controls */
.chat-controls {
  display: flex;
  justify-content: space-between;
  padding: 10px 15px;
  background: var(--bg-light);
  border-top: 1px solid var(--border);
}

/* Scrollbar styling */
.chat-box::-webkit-scrollbar {
  width: 8px;
}

.chat-box::-webkit-scrollbar-track {
  background: var(--bg);
  border-radius: 4px;
}

.chat-box::-webkit-scrollbar-thumb {
  background: #c5c7d0;
  border-radius: 4px;
}

.chat-box::-webkit-scrollbar-thumb:hover {
  background: #a5a9b8;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .content {
    padding: 60px 15px;
  }
  
  .header h1 {
    font-size: 2.2rem;
  }
  
  .chat-popup {
    bottom: 0;
    right: 0;
    width: 100%;
    max-width: none;
    border-radius: 0;
    height: 100vh;
    max-height: none;
  }
  
  .chatbot-btn {
    bottom: 20px;
    right: 20px;
    padding: 14px 20px;
  }
  
  .quick-questions {
    grid-template-columns: 1fr;
  }
}
.message-row {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  max-width: 85%;
  animation: fadeIn 0.3s ease-out;
}

.message-row.bot {
  flex-direction: row;
  align-self: flex-start;
}

.message-row.user {
  flex-direction: row-reverse;
  align-self: flex-end;
}

.avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background-color: var(--primary);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 16px;
  box-shadow: 0 0 0 1px var(--border);
}

.bot-avatar {
  background-color: var(--primary);
}

.user-avatar {
  background-color: var(--secondary);
}

/* Optional: typing indicator with avatar */
.message-row.typing .message-content {
  background-color: var(--bot-bg);
  padding: 8px 12px;
  border-radius: 18px;
  display: flex;
  gap: 6px;
}

# js
// === LẤY CÁC PHẦN TỬ DOM ===
const chatbotButton = document.getElementById('chatbot-btn');
const chatPopup = document.getElementById('chat-popup');
const closeButton = document.getElementById('close-btn');
const sendButton = document.getElementById('send-btn');
const userInput = document.getElementById('user-input');
const chatBox = document.getElementById('chat-box');
const minimizeButton = document.getElementById('minimize-btn');
const typingIndicator = document.getElementById('typing-indicator');
const notificationBadge = document.querySelector('.notification-badge');
const quickButtons = document.querySelectorAll('.quick-btn');

let isMinimized = false;
let hasNewMessage = false;
let messageHistory = [];

// === MỞ / ẨN CHATBOT ===
chatbotButton.addEventListener('click', () => {
  chatPopup.classList.toggle('hidden');
  if (!chatPopup.classList.contains('hidden')) {
    userInput.focus();
    scrollToBottom();
    if (hasNewMessage) {
      hasNewMessage = false;
      notificationBadge.classList.add('hidden');
      notificationBadge.textContent = '';
    }
  }
});

// === ĐÓNG CHATBOT ===
closeButton.addEventListener('click', () => {
  chatPopup.classList.add('hidden');
  isMinimized = false;
});

// === THU NHỎ / MỞ RỘNG CHATBOT ===
minimizeButton.addEventListener('click', () => {
  if (!isMinimized) {
    chatPopup.classList.add('minimized');
    minimizeButton.querySelector('svg path').setAttribute('d', 'M5 9H19');
    isMinimized = true;
  } else {
    chatPopup.classList.remove('minimized');
    minimizeButton.querySelector('svg path').setAttribute('d', 'M5 15H19');
    isMinimized = false;
    scrollToBottom();
  }
});

// === XỬ LÝ NÚT NHANH ===
quickButtons.forEach(button => {
  button.addEventListener('click', handleQuickQuestion);
});

function handleQuickQuestion(event) {
  const question = event.target.dataset.question;
  userInput.value = question;
  sendMessage();
}

// === GỬI TIN NHẮN ===
sendButton.addEventListener('click', sendMessage);
userInput.addEventListener('keydown', (event) => {
  if (event.key === 'Enter' && !event.shiftKey) {
    event.preventDefault();
    sendMessage();
  }
});

async function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;

  appendMessage(message, 'user');
  userInput.value = '';
  userInput.style.height = 'auto';
  scrollToBottom();

  showTypingIndicator();
  await new Promise(resolve => setTimeout(resolve, 1000));

  try {
    const response = await fetch('/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question: message })
    });

    if (!response.ok) throw new Error('Lỗi kết nối máy chủ');

    const data = await response.json();
    hideTypingIndicator();
    await typeBotMessageHTML(data.answer);
  } catch (error) {
    hideTypingIndicator();
    await typeBotMessageHTML('Đã xảy ra lỗi. Vui lòng thử lại sau.');
  }
}

function showTypingIndicator() {
  typingIndicator.classList.remove('hidden');
  const dots = typingIndicator.querySelectorAll('.typing-dot');
  dots.forEach((dot, index) => {
    dot.style.animationDelay = `${index * 0.2}s`;
  });
}

function hideTypingIndicator() {
  typingIndicator.classList.add('hidden');
  const dots = typingIndicator.querySelectorAll('.typing-dot');
  dots.forEach(dot => {
    dot.style.animationDelay = '0s';
  });
}

function appendMessage(text, sender) {
  const messageDiv = document.createElement('div');
  messageDiv.className = `chat-message ${sender}-message`;

  const contentDiv = document.createElement('div');
  contentDiv.className = 'message-content';
  contentDiv.innerHTML = `<p>${text}</p><span class="message-time">${getCurrentTime()}</span>`;

  messageDiv.appendChild(contentDiv);
  chatBox.appendChild(messageDiv);
  scrollToBottom();
}

async function typeBotMessageHTML(html) {
  const wrapper = document.createElement('div');
  wrapper.innerHTML = html;

  const messageDiv = document.createElement('div');
  messageDiv.className = 'chat-message bot-message';
  messageDiv.style.display = 'flex';
  messageDiv.style.alignItems = 'flex-start';
  messageDiv.style.gap = '10px';

  const avatar = document.createElement('div');
  avatar.style.backgroundColor = '#fff';
  avatar.style.borderRadius = '50%';
  avatar.style.width = '32px';
  avatar.style.height = '32px';
  avatar.style.display = 'flex';
  avatar.style.alignItems = 'center';
  avatar.style.justifyContent = 'center';
  avatar.innerHTML = `<i class="fas fa-robot" style="font-size: 18px; color: #4f46e5;"></i>`;

  const contentDiv = document.createElement('div');
  contentDiv.className = 'message-content';

  messageDiv.appendChild(avatar);
  messageDiv.appendChild(contentDiv);
  chatBox.appendChild(messageDiv);
  scrollToBottom();

  for (const child of wrapper.childNodes) {
    await typeElement(child, contentDiv);
  }

  const timeSpan = document.createElement('span');
  timeSpan.className = 'message-time';
  timeSpan.textContent = getCurrentTime();
  contentDiv.appendChild(timeSpan);

  scrollToBottom();

  if (chatPopup.classList.contains('hidden') || chatPopup.classList.contains('minimized')) {
    hasNewMessage = true;
    notificationBadge.classList.remove('hidden');
    let count = parseInt(notificationBadge.textContent) || 0;
    notificationBadge.textContent = (count + 1).toString();
  }
}

async function typeElement(node, parent) {
  if (node.nodeType === Node.TEXT_NODE) {
    const text = node.textContent;
    for (let i = 0; i < text.length; i++) {
      parent.innerHTML += text[i];
      scrollToBottom();
      await new Promise(resolve => setTimeout(resolve, 15));
    }
  } else if (node.nodeType === Node.ELEMENT_NODE) {
    const element = document.createElement(node.tagName);
    for (const attribute of node.attributes) {
      element.setAttribute(attribute.name, attribute.value);
    }
    parent.appendChild(element);
    for (const child of node.childNodes) {
      await typeElement(child, element);
    }
  }
}

function getCurrentTime() {
  const now = new Date();
  return `${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}`;
}

function scrollToBottom() {
  chatBox.scrollTop = chatBox.scrollHeight;
}

userInput.addEventListener('input', () => {
  userInput.style.height = 'auto';
  userInput.style.height = `${Math.min(userInput.scrollHeight, 120)}px`;
});

function showNotification(message) {
  const notification = document.createElement('div');
  notification.className = 'notification';
  notification.textContent = message;
  document.body.appendChild(notification);

  setTimeout(() => {
    notification.classList.add('show');
  }, 10);

  setTimeout(() => {
    notification.classList.remove('show');
    setTimeout(() => {
      document.body.removeChild(notification);
    }, 300);
  }, 3000);
}

