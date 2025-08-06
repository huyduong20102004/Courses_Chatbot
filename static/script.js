// SDT Academy Chatbot Script
// Description: JavaScript for handling chatbot functionality
// Version: 1.2.0 (Optimized after removing chat controls)

// === DOM Elements ===
const elements = {
  chatbotButton: document.getElementById('chatbot-btn'),
  chatPopup: document.getElementById('chat-popup'),
  closeButton: document.getElementById('close-btn'),
  sendButton: document.getElementById('send-btn'),
  userInput: document.getElementById('user-input'),
  chatBox: document.getElementById('chat-box'),
  typingIndicator: document.getElementById('typing-indicator'),
  quickButtons: document.querySelectorAll('.quick-btn'),
  notificationBadge: document.querySelector('.notification-badge')
};

// === State Variables ===
let state = {
  hasNewMessage: false,
  messageHistory: []
};

// === Utility Functions ===
const getCurrentTime = () => {
  const now = new Date();
  return `${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}`;
};

const scrollToBottom = () => {
  elements.chatBox.scrollTop = elements.chatBox.scrollHeight;
};

const showNotification = (message, type = 'error') => {
  const notification = document.createElement('div');
  notification.className = `notification notification-${type}`;
  notification.textContent = message;
  document.body.appendChild(notification);

  setTimeout(() => {
    notification.classList.add('show');
  }, 10);

  setTimeout(() => {
    notification.classList.remove('show');
    setTimeout(() => notification.remove(), 300);
  }, 3000);
};

// === Chatbot Toggle ===
elements.chatbotButton.addEventListener('click', () => {
  elements.chatPopup.classList.toggle('hidden');
  if (!elements.chatPopup.classList.contains('hidden')) {
    elements.userInput.focus();
    scrollToBottom();
    if (state.hasNewMessage) {
      state.hasNewMessage = false;
      if (elements.notificationBadge) {
        elements.notificationBadge.classList.add('hidden');
        elements.notificationBadge.textContent = '';
      }
    }
  }
});

// === Close Chatbot ===
elements.closeButton.addEventListener('click', () => {
  elements.chatPopup.classList.add('hidden');
});

// === Quick Buttons Handling ===
elements.quickButtons.forEach(button => {
  button.addEventListener('click', () => {
    const question = button.dataset.question;
    if (question) {
      elements.userInput.value = question;
      sendMessage();
    }
  });
});

// === Send Message ===
elements.sendButton.addEventListener('click', sendMessage);
elements.userInput.addEventListener('keydown', (event) => {
  if (event.key === 'Enter' && !event.shiftKey) {
    event.preventDefault();
    sendMessage();
  }
});

async function sendMessage() {
  const message = elements.userInput.value.trim();
  if (!message) return;

  appendMessage(message, 'user');
  state.messageHistory.push({ sender: 'user', text: message, time: getCurrentTime() });
  elements.userInput.value = '';
  elements.userInput.style.height = 'auto';
  scrollToBottom();

  showTypingIndicator();
  try {
    const response = await fetch('/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question: message })
    });

    if (!response.ok) throw new Error('Lỗi kết nối máy chủ: ' + response.status);

    const data = await response.json();
    hideTypingIndicator();
    await typeBotMessage(data.answer);
  } catch (error) {
    hideTypingIndicator();
    await typeBotMessage('Đã xảy ra lỗi. Vui lòng thử lại sau.');
    showNotification(error.message || 'Không thể kết nối với máy chủ', 'error');
  }
}

// === Typing Indicator ===
const showTypingIndicator = () => {
  elements.typingIndicator.classList.remove('hidden');
  scrollToBottom();
};

const hideTypingIndicator = () => {
  elements.typingIndicator.classList.add('hidden');
};

// === Append Message ===
const appendMessage = (text, sender) => {
  const messageDiv = document.createElement('div');
  messageDiv.className = `message-row ${sender}`;
  
  const avatar = document.createElement('div');
  avatar.className = `avatar ${sender === 'user' ? 'user-avatar' : 'bot-avatar'}`;
  avatar.innerHTML = sender === 'user' ? 'D' : '<i class="fas fa-robot" style="font-size: 18px;"></i>';

  const contentDiv = document.createElement('div');
  contentDiv.className = 'message-content';
  contentDiv.innerHTML = `<p>${text}</p><span class="message-time">${getCurrentTime()}</span>`;

  messageDiv.appendChild(avatar);
  messageDiv.appendChild(contentDiv);
  elements.chatBox.appendChild(messageDiv);
  scrollToBottom();
};

// === Type Bot Message with Animation ===
async function typeBotMessage(html) {
  const wrapper = document.createElement('div');
  wrapper.innerHTML = html;

  const messageDiv = document.createElement('div');
  messageDiv.className = 'message-row bot';
  messageDiv.style.display = 'flex';
  messageDiv.style.alignItems = 'flex-start';
  messageDiv.style.gap = '10px';

  const avatar = document.createElement('div');
  avatar.className = 'avatar bot-avatar';
  avatar.innerHTML = '<i class="fas fa-robot" style="font-size: 18px;"></i>';

  const contentDiv = document.createElement('div');
  contentDiv.className = 'message-content';

  messageDiv.appendChild(avatar);
  messageDiv.appendChild(contentDiv);
  elements.chatBox.appendChild(messageDiv);
  scrollToBottom();

  for (const child of wrapper.childNodes) {
    await typeElement(child, contentDiv);
  }

  const timeSpan = document.createElement('span');
  timeSpan.className = 'message-time';
  timeSpan.textContent = getCurrentTime();
  contentDiv.appendChild(timeSpan);

  state.messageHistory.push({ sender: 'bot', text: html, time: getCurrentTime() });
  scrollToBottom();

  if (elements.chatPopup.classList.contains('hidden')) {
    state.hasNewMessage = true;
    if (elements.notificationBadge) {
      elements.notificationBadge.classList.remove('hidden');
      let count = parseInt(elements.notificationBadge.textContent) || 0;
      elements.notificationBadge.textContent = (count + 1).toString();
    }
  }
}

async function typeElement(node, parent) {
  if (node.nodeType === Node.TEXT_NODE) {
    const text = node.textContent;
    for (let i = 0; i < text.length; i++) {
      const char = text[i];
      if (char === '\n') {
        parent.appendChild(document.createElement('br'));
      } else {
        parent.innerHTML += char;
      }
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


// === Auto-resize Textarea ===
elements.userInput.addEventListener('input', () => {
  elements.userInput.style.height = 'auto';
  elements.userInput.style.height = `${Math.min(elements.userInput.scrollHeight, 120)}px`;
});

// === Notification Styles ===
const notificationStyles = `
  .notification {
    position: fixed;
    top: 20px;
    right: 20px;
    background-color: #ef4444;
    color: white;
    padding: 12px 20px;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    opacity: 0;
    transform: translateY(-10px);
    transition: all 0.3s ease;
    z-index: 2000;
  }
  .notification.show {
    opacity: 1;
    transform: translateY(0);
  }
  .notification-success {
    background-color: #10b981;
  }
`;

const styleSheet = document.createElement('style');
styleSheet.textContent = notificationStyles;
document.head.appendChild(styleSheet);

// === Error Handling for Missing Elements ===
Object.keys(elements).forEach(key => {
  if (!elements[key] && key !== 'quickButtons' && key !== 'notificationBadge') {
    console.error(`Element with ID '${key}' not found in the DOM`);
  }
});



