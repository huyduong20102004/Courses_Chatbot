// === CÁC DOM ELEMENT ===
const chatbotBtn = document.getElementById('chatbot-btn');
const chatPopup = document.getElementById('chat-popup');
const closeBtn = document.getElementById('close-btn');
const sendBtn = document.getElementById('send-btn');
const userInput = document.getElementById('user-input');
const chatBox = document.getElementById('chat-box');
const clearBtn = document.getElementById('clear-btn');
const minimizeBtn = document.getElementById('minimize-btn');
const typingIndicator = document.getElementById('typing-indicator');
const notificationBadge = document.querySelector('.notification-badge');
const quickBtns = document.querySelectorAll('.quick-btn');

let isMinimized = false;
let hasNewMessage = false;
let messageHistory = [];

// === MỞ / ẨN CHATBOT ===
chatbotBtn.addEventListener('click', () => {
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
closeBtn.addEventListener('click', () => {
  chatPopup.classList.add('hidden');
  isMinimized = false;
});

// === THU NHỎ / MỞ RỘNG CHATBOT ===
minimizeBtn.addEventListener('click', () => {
  if (!isMinimized) {
    chatPopup.classList.add('minimized');
    minimizeBtn.querySelector('svg path').setAttribute('d', 'M5 9H19');
    isMinimized = true;
  } else {
    chatPopup.classList.remove('minimized');
    minimizeBtn.querySelector('svg path').setAttribute('d', 'M5 15H19');
    isMinimized = false;
    scrollToBottom();
  }
});

// === XÓA LỊCH SỬ ===
clearBtn.addEventListener('click', () => {
  if (chatBox.children.length > 1) {
    messageHistory.push({
      date: new Date().toISOString(),
      messages: Array.from(chatBox.children).slice(1).map(el => el.outerHTML)
    });
  }

  while (chatBox.firstChild) {
    chatBox.removeChild(chatBox.firstChild);
  }

  const welcomeMsg = document.createElement('div');
  welcomeMsg.className = 'welcome-message';
  welcomeMsg.innerHTML = `
    <div class="welcome-header">
      <img src="{{ url_for('static', filename='ai-icon.png') }}" alt="AI Icon" />
      <h3>Xin chào! Tôi là trợ lý AI</h3>
    </div>
    <p>Tôi có thể giúp gì cho bạn về khóa học Trí tuệ nhân tạo?</p>
    <div class="quick-questions">
      <button class="quick-btn" data-question="Khóa học AI gồm những nội dung gì?">Khóa học gồm nội dung gì?</button>
      <button class="quick-btn" data-question="Tôi cần chuẩn bị gì trước khi học?">Cần chuẩn bị gì?</button>
      <button class="quick-btn" data-question="Lộ trình học AI như thế nào?">Lộ trình học tập</button>
      <button class="quick-btn" data-question="Tôi có thể làm dự án gì với AI?">Dự án thực hành</button>
    </div>
  `;
  chatBox.appendChild(welcomeMsg);

  document.querySelectorAll('.quick-btn').forEach(btn => {
    btn.addEventListener('click', handleQuickQuestion);
  });

  showNotification("Cuộc trò chuyện đã được xóa");
});

// === XỬ LÝ NÚT NHANH ===
quickBtns.forEach(btn => {
  btn.addEventListener('click', handleQuickQuestion);
});

function handleQuickQuestion(e) {
  const question = e.target.dataset.question;
  userInput.value = question;
  sendMessage();
}

// === GỬI TIN NHẮN ===
sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

async function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;

  appendMessage(message, 'user');
  userInput.value = '';
  userInput.style.height = 'auto';

  typingIndicator.classList.remove('hidden');
  scrollToBottom();

  try {
    const res = await fetch('/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question: message })
    });

    if (!res.ok) throw new Error('Network response was not ok');

    const data = await res.json();
    typingIndicator.classList.add('hidden');
    await typeBotMessageHTML(data.answer);
  } catch (error) {
    typingIndicator.classList.add('hidden');
    await typeBotMessageHTML('Đã xảy ra lỗi. Vui lòng thử lại sau.');
  }
}

// === HIỂN THỊ TIN NHẮN NGƯỜI DÙNG ===
function appendMessage(text, sender) {
  const div = document.createElement('div');
  div.className = `chat-message ${sender}-message`;

  const contentDiv = document.createElement('div');
  contentDiv.className = 'message-content';
  contentDiv.innerHTML = `<p>${text}</p><span class="message-time">${getCurrentTime()}</span>`;

  div.appendChild(contentDiv);
  chatBox.appendChild(div);
  scrollToBottom();
}

// === HIỆU ỨNG ĐÁNH MÁY HTML ===
async function typeBotMessageHTML(html) {
  if (document.querySelector('.welcome-message')) {
    document.querySelector('.welcome-message').remove();
  }

  const wrapper = document.createElement('div');
  wrapper.innerHTML = html;

  const div = document.createElement('div');
  div.className = 'chat-message bot-message';
  const contentDiv = document.createElement('div');
  contentDiv.className = 'message-content';
  div.appendChild(contentDiv);
  chatBox.appendChild(div);
  scrollToBottom();

  for (const child of wrapper.childNodes) {
    await typeElement(child, contentDiv);
  }

  const timeSpan = document.createElement('span');
  timeSpan.className = 'message-time';
  timeSpan.textContent = getCurrentTime();
  contentDiv.appendChild(timeSpan);

  scrollToBottom();
  typingIndicator.classList.add('hidden');

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
      await new Promise(r => setTimeout(r, 15));
    }
  } else if (node.nodeType === Node.ELEMENT_NODE) {
    const el = document.createElement(node.tagName);
    for (const attr of node.attributes) {
      el.setAttribute(attr.name, attr.value);
    }

    parent.appendChild(el);
    for (const child of node.childNodes) {
      await typeElement(child, el);
    }
  }
}

// === GIỜ HIỆN TẠI ===
function getCurrentTime() {
  const now = new Date();
  return `${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}`;
}

// === CUỘN CUỐI ===
function scrollToBottom() {
  chatBox.scrollTop = chatBox.scrollHeight;
}

// === TỰ GIÃN TEXTAREA ===
userInput.addEventListener('input', () => {
  userInput.style.height = 'auto';
  userInput.style.height = `${Math.min(userInput.scrollHeight, 120)}px`;
});

// === THÔNG BÁO NHỎ ===
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










