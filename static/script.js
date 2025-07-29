// DOM Elements
const chatTab = document.getElementById('chat-tab');
const coursesTab = document.getElementById('courses-tab');
const resourcesTab = document.getElementById('resources-tab');
const progressTab = document.getElementById('progress-tab');
const settingsTab = document.getElementById('settings-tab');
const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const chatSearch = document.getElementById('chat-search');
const searchContainer = document.getElementById('search-container');
const themeSelect = document.getElementById('theme-select');
const fontSizeSlider = document.getElementById('font-size');
const fontSizeValue = document.getElementById('font-size-value');
const densitySelect = document.getElementById('density-select');
const coursesGrid = document.querySelector('.courses-grid');
const courseCategory = document.getElementById('course-category');
const courseSearch = document.getElementById('course-search');
const resourceGrids = document.querySelectorAll('.resource-grid');
const usernameInput = document.getElementById('username-input');
const emailInput = document.getElementById('email-input');
const profileModal = document.getElementById('profile-modal');
const clearChatModal = document.getElementById('clear-chat-modal');
const loadingOverlay = document.getElementById('loading-overlay');
const toast = document.getElementById('toast');
const emojiPicker = document.getElementById('emoji-picker');
const recordBtn = document.getElementById('record-btn');
const fileInput = document.getElementById('file-input');
const courseProgressChart = document.getElementById('course-progress-chart').getContext('2d');
const skillsChart = document.getElementById('skills-chart').getContext('2d');
const activityList = document.querySelector('.activity-list');

// Sample data
const courses = [
  { title: 'AI Cơ Bản', description: 'Khóa học nhập môn AI dành cho người mới bắt đầu', price: '2.500.000đ', rating: '4.8/5', category: 'beginner' },
  { title: 'Machine Learning Nâng Cao', description: 'Các thuật toán ML và ứng dụng thực tế', price: '3.500.000đ', rating: '4.9/5', category: 'advanced' },
  { title: 'Deep Learning với Python', description: 'Xây dựng mạng neural networks với TensorFlow', price: '4.000.000đ', rating: '4.7/5', category: 'advanced' },
  { title: 'Xử lý Ngôn ngữ Tự nhiên', description: 'NLP từ cơ bản đến ứng dụng thực tế', price: '3.200.000đ', rating: '4.6/5', category: 'specialization' },
  { title: 'Thị giác Máy tính', description: 'Nhận diện hình ảnh và video với OpenCV', price: '3.800.000đ', rating: '4.5/5', category: 'specialization' },
  { title: 'AI trong Kinh doanh', description: 'Ứng dụng AI để tối ưu hoá doanh nghiệp', price: '2.900.000đ', rating: '4.4/5', category: 'intermediate' }
];

const resources = [
  {
    category: 'books',
    items: [
      { title: 'Deep Learning', description: 'Ian Goodfellow', url: '#' },
      { title: 'Pattern Recognition', description: 'Christopher Bishop', url: '#' },
      { title: 'AI Superpowers', description: 'Kai-Fu Lee', url: '#' }
    ]
  },
  {
    category: 'videos',
    items: [
      { title: 'CS231n: Deep Learning', description: 'Stanford University', url: '#' },
      { title: 'NLP with Python', description: 'Coursera', url: '#' },
      { title: 'AI for Everyone', description: 'Andrew Ng', url: '#' }
    ]
  }
];

const activities = [
  { title: 'Hoàn thành bài học 1: AI Cơ Bản', time: 'Hôm qua, 14:30', icon: 'fas fa-check-circle' },
  { title: 'Đạt chứng chỉ Machine Learning', time: '2 ngày trước, 09:15', icon: 'fas fa-trophy' },
  { title: 'Xem video NLP', time: '3 ngày trước, 16:00', icon: 'fas fa-video' }
];

// Initialize the app
function initApp() {
  loadSettings();
  renderCourses();
  renderResources();
  renderActivities();
  renderCharts();
  checkSystemTheme();
  updateNotificationBadge();
}

// Tab navigation
function showTab(tabId) {
  const tabs = [chatTab, coursesTab, resourcesTab, progressTab, settingsTab];
  tabs.forEach(tab => tab.classList.remove('active'));
  document.getElementById(tabId).classList.add('active');
  
  const menuItems = document.querySelectorAll('.menu-item');
  menuItems.forEach(item => item.classList.remove('active'));
  document.querySelector(`.menu-item[onclick="showTab('${tabId}')"]`).classList.add('active');

  if (tabId === 'chat-tab') updateNotificationBadge();
}

// Render courses
function renderCourses(filter = 'all', searchQuery = '') {
  coursesGrid.innerHTML = '';
  const filteredCourses = courses.filter(course => 
    (filter === 'all' || course.category === filter) &&
    (course.title.toLowerCase().includes(searchQuery.toLowerCase()) || 
     course.description.toLowerCase().includes(searchQuery.toLowerCase()))
  );

  filteredCourses.forEach(course => {
    const courseCard = document.createElement('div');
    courseCard.className = 'course-card';
    courseCard.innerHTML = `
      <div class="course-image"><i class="fas fa-graduation-cap"></i></div>
      <div class="course-info">
        <h3 class="course-title">${course.title}</h3>
        <p class="course-desc">${course.description}</p>
        <div class="course-meta">
          <span class="course-price">${course.price}</span>
          <span class="course-rating"><i class="fas fa-star"></i> ${course.rating}</span>
        </div>
      </div>
    `;
    coursesGrid.appendChild(courseCard);
  });
}

// Render resources
function renderResources() {
  resourceGrids.forEach((grid, index) => {
    grid.innerHTML = '';
    resources[index].items.forEach(item => {
      const resourceItem = document.createElement('div');
      resourceItem.className = 'resource-item';
      resourceItem.innerHTML = `
        <h3>${item.title}</h3>
        <p>${item.description}</p>
        <a href="${item.url}" target="_blank">Xem thêm</a>
      `;
      grid.appendChild(resourceItem);
    });
  });
}

// Render activities
function renderActivities() {
  activityList.innerHTML = '';
  activities.forEach(activity => {
    const activityItem = document.createElement('div');
    activityItem.className = 'activity-item';
    activityItem.innerHTML = `
      <div class="activity-icon"><i class="${activity.icon}"></i></div>
      <div class="activity-content">
        <div class="activity-title">${activity.title}</div>
        <div class="activity-time">${activity.time}</div>
      </div>
    `;
    activityList.appendChild(activityItem);
  });
}

// Render charts
function renderCharts() {
  new Chart(courseProgressChart, {
    type: 'doughnut',
    data: {
      labels: ['Hoàn thành', 'Đang học', 'Chưa bắt đầu'],
      datasets: [{
        data: [8, 4, 3],
        backgroundColor: ['#4cc9f0', '#f8961e', '#adb5bd']
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false
    }
  });

  new Chart(skillsChart, {
    type: 'radar',
    data: {
      labels: ['Python', 'ML Algorithms', 'Deep Learning', 'NLP', 'Computer Vision'],
      datasets: [{
        label: 'Kỹ năng',
        data: [80, 75, 60, 50, 65],
        backgroundColor: 'rgba(67, 97, 238, 0.2)',
        borderColor: '#4361ee',
        borderWidth: 2
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        r: {
          beginAtZero: true
        }
      }
    }
  });
}

// Chat functions
async function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;

  addMessage(message, 'user');
  userInput.value = '';
  showLoading();

  try {
    const typingIndicator = addTypingIndicator();
    await new Promise(resolve => setTimeout(resolve, 1000));
    const res = await fetch('/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question: message })
    });
    chatBox.removeChild(typingIndicator);
    const data = await res.json();
    addMessage(data.answer || 'Đã xảy ra lỗi không xác định', 'bot', !data.answer);
  } catch (err) {
    addMessage('Không kết nối được đến máy chủ', 'bot', true);
    console.error('Error:', err);
  } finally {
    hideLoading();
  }

  scrollToBottom();
  updateNotificationBadge();
}

function addMessage(text, sender, isError = false) {
  const messageDiv = document.createElement('div');
  messageDiv.className = `message message-${sender} ${isError ? 'message-error' : ''}`;

  const now = new Date();
  const timeString = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

  const messageAvatar = `<div class="message-avatar">${sender === 'user' ? '<i class="fas fa-user"></i>' : '<i class="fas fa-robot"></i>'}</div>`;
  const messageContent = document.createElement('div');
  messageContent.className = 'message-content';

  const messageText = document.createElement('div');
  messageText.className = 'message-text';
  const messageTime = document.createElement('div');
  messageTime.className = 'message-time';
  messageTime.textContent = timeString;

  messageContent.appendChild(messageText);
  messageContent.appendChild(messageTime);
  messageDiv.innerHTML = messageAvatar;
  messageDiv.appendChild(messageContent);
  chatBox.appendChild(messageDiv);

  // Nếu là user hoặc lỗi → hiện ngay
  if (sender === 'user' || isError) {
    const cleanedText = text.replace(/\*/g, '').replace(/\n/g, '<br>'); // Xóa tất cả dấu *
    messageText.innerHTML = cleanedText;
    scrollToBottom();
    return;
  }

  // Nếu là bot → hiện từ từ
  let index = 0;
  const cleanedText = text.replace(/\*/g, '').replace(/\n/g, '<br>'); // Xóa dấu * và giữ xuống dòng
  const typingInterval = setInterval(() => {
    messageText.innerHTML = cleanedText.slice(0, index + 1);
    index++;
    if (index >= cleanedText.length) {
      clearInterval(typingInterval);
    }
    scrollToBottom();
  }, 10);
}


function addTypingIndicator() {
  const typingDiv = document.createElement('div');
  typingDiv.className = 'message message-bot';
  typingDiv.innerHTML = `
    <div class="message-avatar"><i class="fas fa-robot"></i></div>
    <div class="message-content">
      <div class="message-text typing-indicator">
        <span>.</span><span>.</span><span>.</span>
      </div>
    </div>
  `;
  chatBox.appendChild(typingDiv);
  scrollToBottom();
  return typingDiv;
}


function clearChat() {
  closeModal('clear-chat-modal');
  chatBox.innerHTML = `
    <div class="welcome-message">
      <div class="bot-avatar pulse"><i class="fas fa-brain"></i></div>
      <div class="welcome-content">
        <h3>Chào mừng đến với AI Mentor Pro!</h3>
        <p>Tôi là trợ lý AI có thể giúp bạn:</p>
        <ul class="welcome-features">
          <li><i class="fas fa-check-circle"></i> Tư vấn khóa học AI/ML phù hợp</li>
          <li><i class="fas fa-check-circle"></i> Đánh giá lộ trình học tập</li>
          <li><i class="fas fa-check-circle"></i> Giải đáp thắc mắc về công nghệ AI</li>
          <li><i class="fas fa-check-circle"></i> Gợi ý tài nguyên học tập</li>
        </ul>
        <div class="quick-questions">
          <p class="quick-title">Bạn quan tâm đến:</p>
          <div class="quick-grid">
            <button class="quick-btn" onclick="insertQuestion('Khóa học AI nào phù hợp cho người mới bắt đầu?')">
              <i class="fas fa-user-graduate"></i> Khóa học cho người mới
            </button>
            <button class="quick-btn" onclick="insertQuestion('Học AI cần những kiến thức nền tảng gì?')">
              <i class="fas fa-layer-group"></i> Kiến thức nền tảng
            </button>
            <button class="quick-btn" onclick="insertQuestion('Có học bổng cho khóa học AI không?')">
              <i class="fas fa-award"></i> Học bổng AI
            </button>
            <button class="quick-btn" onclick="insertQuestion('Lộ trình trở thành chuyên gia AI?')">
              <i class="fas fa-road"></i> Lộ trình học tập
            </button>
          </div>
        </div>
      </div>
    </div>
  `;
  showToast('Lịch sử trò chuyện đã được xóa!');
  updateNotificationBadge();
}

function insertQuestion(question) {
  userInput.value = question;
  userInput.focus();
}

function scrollToBottom() {
  chatBox.scrollTop = chatBox.scrollHeight;
}

function handleKeyPress(e) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
}

// Search functions
function toggleSearch() {
  searchContainer.classList.toggle('active');
  if (searchContainer.classList.contains('active')) {
    chatSearch.focus();
  } else {
    chatSearch.value = '';
    searchChat();
  }
}

function searchChat() {
  const query = chatSearch.value.toLowerCase();
  const messages = chatBox.querySelectorAll('.message');
  messages.forEach(message => {
    const text = message.querySelector('.message-text').textContent.toLowerCase();
    message.style.display = text.includes(query) || query === '' ? '' : 'none';
  });
}

// Profile and modal functions
function showProfileModal() {
  document.getElementById('modal-username').textContent = usernameInput.value;
  document.getElementById('modal-email').textContent = emailInput.value;
  profileModal.classList.add('active');
}

function closeModal(modalId) {
  document.getElementById(modalId).classList.remove('active');
}

function showClearChatModal() {
  clearChatModal.classList.add('active');
}

// Export chat
function exportChat() {
  const messages = chatBox.querySelectorAll('.message');
  let chatContent = '';
  messages.forEach(message => {
    const text = message.querySelector('.message-text').textContent;
    const sender = message.classList.contains('message-user') ? 'You' : 'Bot';
    const time = message.querySelector('.message-time').textContent;
    chatContent += `[${time}] ${sender}: ${text}\n`;
  });
  const blob = new Blob([chatContent], { type: 'text/plain' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'chat_history.txt';
  a.click();
  URL.revokeObjectURL(url);
  showToast('Lịch sử trò chuyện đã được xuất!');
}

// Settings functions
function loadSettings() {
  const savedTheme = localStorage.getItem('theme') || 'light';
  const savedFontSize = localStorage.getItem('fontSize') || '16';
  const savedDensity = localStorage.getItem('density') || 'comfortable';

  themeSelect.value = savedTheme;
  fontSizeSlider.value = savedFontSize;
  densitySelect.value = savedDensity;
  fontSizeValue.textContent = `${savedFontSize}px`;

  applyTheme(savedTheme);
  applyFontSize(savedFontSize);
  applyDensity(savedDensity);
}

function saveSettings() {
  const theme = themeSelect.value;
  const fontSize = fontSizeSlider.value;
  const density = densitySelect.value;

  localStorage.setItem('theme', theme);
  localStorage.setItem('fontSize', fontSize);
  localStorage.setItem('density', density);

  applyTheme(theme);
  applyFontSize(fontSize);
  applyDensity(density);

  showToast('Cài đặt đã được lưu thành công!');
}

function resetSettings() {
  localStorage.removeItem('theme');
  localStorage.removeItem('fontSize');
  localStorage.removeItem('density');

  themeSelect.value = 'light';
  fontSizeSlider.value = '16';
  densitySelect.value = 'comfortable';
  fontSizeValue.textContent = '16px';

  applyTheme('light');
  applyFontSize('16');
  applyDensity('comfortable');

  showToast('Cài đặt đã được đặt lại mặc định!');
}

function applyTheme(theme) {
  if (theme === 'system') {
    checkSystemTheme();
  } else {
    document.documentElement.setAttribute('data-theme', theme);
  }
}

function checkSystemTheme() {
  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.documentElement.setAttribute('data-theme', 'dark');
  } else {
    document.documentElement.setAttribute('data-theme', 'light');
  }
}

function applyFontSize(size) {
  document.documentElement.style.fontSize = `${size}px`;
  fontSizeValue.textContent = `${size}px`;
}

function applyDensity(density) {
  document.documentElement.setAttribute('data-density', density);
}

// Course filtering
courseCategory.addEventListener('change', () => {
  renderCourses(courseCategory.value, courseSearch.value);
});

courseSearch.addEventListener('input', () => {
  renderCourses(courseCategory.value, courseSearch.value);
});

// Toast notification
function showToast(message) {
  toast.textContent = message;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 3000);
}

// Loading overlay (đã loại bỏ overlay toàn màn hình)
function showLoading() {
  // Đã thay bằng hiệu ứng dấu ba chấm trong chat bubble
}

function hideLoading() {
  // Đã thay bằng hiệu ứng dấu ba chấm trong chat bubble
}


// Emoji picker
function toggleEmojiPicker() {
  emojiPicker.classList.toggle('active');
  if (emojiPicker.classList.contains('active')) {
    const picker = document.createElement('emoji-picker');
    picker.addEventListener('emoji-click', e => {
      userInput.value += e.detail.unicode;
      userInput.focus();
    });
    emojiPicker.innerHTML = '';
    emojiPicker.appendChild(picker);
  }
}

// File upload
fileInput.addEventListener('change', async (e) => {
  const file = e.target.files[0];
  if (!file) return;

  showLoading();
  try {
    const formData = new FormData();
    formData.append('file', file);
    const res = await fetch('/upload', {
      method: 'POST',
      body: formData
    });
    const data = await res.json();
    addMessage(data.message || 'Tệp đã được tải lên thành công!', 'bot');
  } catch (err) {
    addMessage('Lỗi khi tải lên tệp', 'bot', true);
    console.error('Error:', err);
  } finally {
    hideLoading();
    fileInput.value = '';
  }
  scrollToBottom();
});

// Voice recording
let mediaRecorder;
let audioChunks = [];

function toggleRecording() {
  if (!mediaRecorder || mediaRecorder.state === 'inactive') {
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(stream => {
        mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.start();
        recordBtn.classList.add('recording');
        recordBtn.innerHTML = '<i class="fas fa-stop"></i>';
        showToast('Đang ghi âm...');

        mediaRecorder.ondataavailable = e => audioChunks.push(e.data);
        mediaRecorder.onstop = async () => {
          const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
          audioChunks = [];
          showLoading();
          try {
            const formData = new FormData();
            formData.append('audio', audioBlob, 'recording.webm');
            const res = await fetch('/upload-audio', {
              method: 'POST',
              body: formData
            });
            const data = await res.json();
            addMessage(data.message || 'Ghi âm đã được xử lý!', 'bot');
          } catch (err) {
            addMessage('Lỗi khi xử lý ghi âm', 'bot', true);
            console.error('Error:', err);
          } finally {
            hideLoading();
          }
          scrollToBottom();
        };
      })
      .catch(err => {
        showToast('Không thể truy cập microphone');
        console.error('Error:', err);
      });
  } else {
    mediaRecorder.stop();
    recordBtn.classList.remove('recording');
    recordBtn.innerHTML = '<i class="fas fa-microphone"></i>';
  }
}

// Avatar selection
document.querySelectorAll('.avatar-option').forEach(option => {
  option.addEventListener('click', () => {
    document.querySelectorAll('.avatar-option').forEach(opt => opt.classList.remove('selected'));
    option.classList.add('selected');
    const icon = option.innerHTML;
    document.getElementById('user-avatar').innerHTML = icon;
    document.getElementById('modal-avatar-icon').innerHTML = icon;
  });
});

// Notification badge
function updateNotificationBadge() {
  const notificationBadge = document.getElementById('chat-notification');
  const messageCount = chatBox.querySelectorAll('.message').length;
  notificationBadge.textContent = messageCount > 0 ? messageCount : '0';
  notificationBadge.style.display = messageCount > 0 ? 'flex' : 'none';
}

// Event listeners
document.addEventListener('DOMContentLoaded', initApp);
themeSelect.addEventListener('change', () => applyTheme(themeSelect.value));
fontSizeSlider.addEventListener('input', () => applyFontSize(fontSizeSlider.value));
densitySelect.addEventListener('change', () => applyDensity(densitySelect.value));
sendBtn.addEventListener('click', sendMessage);
chatSearch.addEventListener('input', searchChat);
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
  if (themeSelect.value === 'system') applyTheme('system');
});









