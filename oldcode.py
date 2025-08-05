# index.html :

<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AI Mentor Pro - Trợ lý khóa học AI</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/static/style.css" />
</head>
<body>
  <div class="app-container">
    <!-- Sidebar nâng cấp -->
    <div class="sidebar">
      <div class="sidebar-header">
        <div class="logo-container">
          <i class="fas fa-brain logo-icon"></i>
          <h2>AI Mentor <span class="pro-badge">Pro</span></h2>
        </div>
        <p class="sidebar-subtitle">Trợ lý thông minh tư vấn khóa học AI/ML</p>
      </div>
      
      <div class="sidebar-menu">
        <button class="menu-item active" onclick="showTab('chat-tab')">
          <i class="fas fa-comment-dots"></i> Trò chuyện
          <span class="notification-badge" id="chat-notification">2</span>
        </button>
        <button class="menu-item" onclick="showTab('courses-tab')">
          <i class="fas fa-book-open"></i> Khóa học
        </button>
        <button class="menu-item" onclick="showTab('resources-tab')">
          <i class="fas fa-box-open"></i> Tài nguyên
        </button>
        <button class="menu-item" onclick="showTab('progress-tab')">
          <i class="fas fa-chart-line"></i> Tiến trình
        </button>
        <button class="menu-item" onclick="showTab('settings-tab')">
          <i class="fas fa-sliders-h"></i> Cài đặt
        </button>
      </div>
      
      <div class="sidebar-footer">
        <div class="user-profile">
          <div class="avatar" id="user-avatar">
            <i class="fas fa-user"></i>
          </div>
          <div class="user-info">
            <span class="username" id="username">Người dùng</span>
            <span class="user-email" id="user-email">user@example.com</span>
          </div>
          <button class="profile-btn" onclick="showProfileModal()">
            <i class="fas fa-ellipsis-v"></i>
          </button>
        </div>
      </div>
    </div>
    
    <!-- Main Content -->
    <div class="main-content">
      <!-- Tab Chat -->
      <div class="content-tab active" id="chat-tab">
        <div class="chat-header">
          <div class="header-left">
            <h1><i class="fas fa-robot"></i> Trợ lý AI Mentor</h1>
            <div class="status-indicator">
              <span class="status-dot online"></span>
              <span class="status-text">Online</span>
            </div>
          </div>
          <div class="chat-actions">
            <button class="action-btn" title="Lịch sử trò chuyện" onclick="showChatHistory()">
              <i class="fas fa-history"></i>
            </button>
            <button class="action-btn" title="Xóa lịch sử" onclick="showClearChatModal()">
              <i class="fas fa-trash"></i>
            </button>
            <button class="action-btn" title="Tải xuống" onclick="exportChat()">
              <i class="fas fa-file-export"></i>
            </button>
            <button class="action-btn" title="Tìm kiếm" onclick="toggleSearch()">
              <i class="fas fa-search"></i>
            </button>
          </div>
        </div>
        
        <div class="search-container" id="search-container" style="display: none;">
          <input type="text" id="chat-search" placeholder="Tìm kiếm trong trò chuyện...">
          <button class="search-btn" onclick="searchChat()"><i class="fas fa-search"></i></button>
          <button class="close-search-btn" onclick="toggleSearch()"><i class="fas fa-times"></i></button>
        </div>
        
        <div id="chat-box" class="chat-box">
          <div class="welcome-message">
            <div class="bot-avatar pulse">
              <i class="fas fa-brain"></i>
            </div>
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
        </div>
        
        <div class="input-container">
          <div class="input-tools">
            <button class="tool-btn" title="Tải lên tệp" onclick="document.getElementById('file-input').click()">
              <i class="fas fa-paperclip"></i>
              <input type="file" id="file-input" style="display: none;">
            </button>
            <button class="tool-btn" title="Ghi âm" id="record-btn" onclick="toggleRecording()">
              <i class="fas fa-microphone"></i>
            </button>
            <button class="tool-btn" title="Bảng ký tự đặc biệt" onclick="toggleEmojiPicker()">
              <i class="far fa-smile"></i>
            </button>
          </div>
          <div class="emoji-picker" id="emoji-picker" style="display: none;"></div>
          <input 
            type="text" 
            id="user-input" 
            placeholder="Nhập câu hỏi hoặc yêu cầu về khóa học AI..." 
            onkeypress="handleKeyPress(event)"
          />
          <button class="send-btn" id="send-btn" onclick="sendMessage()" title="Gửi (Enter)">
            <i class="fas fa-paper-plane"></i>
          </button>
        </div>
      </div>
      
      <!-- Tab Khóa học -->
      <div class="content-tab" id="courses-tab">
        <div class="courses-header">
          <h1><i class="fas fa-book-open"></i> Danh mục Khóa Học AI/ML</h1>
          <div class="courses-filter">
            <select id="course-category">
              <option value="all">Tất cả danh mục</option>
              <option value="beginner">Cơ bản</option>
              <option value="intermediate">Trung cấp</option>
              <option value="advanced">Nâng cao</option>
              <option value="specialization">Chuyên ngành</option>
            </select>
            <div class="search-box">
              <input type="text" id="course-search" placeholder="Tìm khóa học...">
              <button class="search-btn"><i class="fas fa-search"></i></button>
            </div>
          </div>
        </div>
        
        <div class="courses-grid" id="courses-grid">
          <!-- Courses will be loaded here -->
        </div>
        
        <div class="pagination">
          <button class="page-btn" disabled><i class="fas fa-chevron-left"></i></button>
          <span class="page-info">Trang 1/5</span>
          <button class="page-btn"><i class="fas fa-chevron-right"></i></button>
        </div>
      </div>
      
      <!-- Tab Tài nguyên -->
      <div class="content-tab" id="resources-tab">
        <h1><i class="fas fa-box-open"></i> Tài Nguyên Học Tập</h1>
        <div class="resources-container">
          <div class="resource-category">
            <h2><i class="fas fa-book"></i> Sách & Tài liệu</h2>
            <div class="resource-grid">
              <!-- Resources will be loaded here -->
            </div>
          </div>
          <div class="resource-category">
            <h2><i class="fas fa-video"></i> Video & Khóa học miễn phí</h2>
            <div class="resource-grid">
              <!-- Resources will be loaded here -->
            </div>
          </div>
        </div>
      </div>
      
      <!-- Tab Tiến trình -->
      <div class="content-tab" id="progress-tab">
        <h1><i class="fas fa-chart-line"></i> Tiến Trình Học Tập</h1>
        <div class="progress-container">
          <div class="progress-stats">
            <div class="stat-card">
              <div class="stat-icon blue">
                <i class="fas fa-clock"></i>
              </div>
              <div class="stat-info">
                <h3>12 giờ</h3>
                <p>Tổng thời gian học</p>
              </div>
            </div>
            <div class="stat-card">
              <div class="stat-icon green">
                <i class="fas fa-check-circle"></i>
              </div>
              <div class="stat-info">
                <h3>8/15</h3>
                <p>Bài học đã hoàn thành</p>
              </div>
            </div>
            <div class="stat-card">
              <div class="stat-icon orange">
                <i class="fas fa-trophy"></i>
              </div>
              <div class="stat-info">
                <h3>3</h3>
                <p>Chứng chỉ đạt được</p>
              </div>
            </div>
          </div>
          
          <div class="progress-charts">
            <div class="chart-container">
              <h3>Tiến độ khóa học</h3>
              <div class="chart" id="course-progress-chart">
                <!-- Chart will be rendered here -->
              </div>
            </div>
            <div class="chart-container">
              <h3>Kỹ năng đạt được</h3>
              <div class="chart" id="skills-chart">
                <!-- Chart will be rendered here -->
              </div>
            </div>
          </div>
          
          <div class="recent-activity">
            <h3>Hoạt động gần đây</h3>
            <div class="activity-list">
              <!-- Activities will be loaded here -->
            </div>
          </div>
        </div>
      </div>
      
      <!-- Tab Cài đặt -->
      <div class="content-tab" id="settings-tab">
        <h1><i class="fas fa-sliders-h"></i> Cài Đặt</h1>
        <div class="settings-container">
          <div class="settings-section">
            <h2><i class="fas fa-user-cog"></i> Tài khoản</h2>
            <div class="settings-form">
              <div class="form-group">
                <label for="username-input">Tên hiển thị</label>
                <input type="text" id="username-input" value="Người dùng">
              </div>
              <div class="form-group">
                <label for="email-input">Email</label>
                <input type="email" id="email-input" value="user@example.com">
              </div>
              <div class="form-group">
                <label for="avatar-select">Ảnh đại diện</label>
                <div class="avatar-options">
                  <div class="avatar-option selected" onclick="selectAvatar(1)">
                    <i class="fas fa-user"></i>
                  </div>
                  <div class="avatar-option" onclick="selectAvatar(2)">
                    <i class="fas fa-robot"></i>
                  </div>
                  <div class="avatar-option" onclick="selectAvatar(3)">
                    <i class="fas fa-graduation-cap"></i>
                  </div>
                  <div class="avatar-option" onclick="selectAvatar(4)">
                    <i class="fas fa-laptop-code"></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <div class="settings-section">
            <h2><i class="fas fa-paint-brush"></i> Giao diện</h2>
            <div class="settings-form">
              <div class="form-group">
                <label for="theme-select">Chủ đề</label>
                <select id="theme-select">
                  <option value="light">Sáng</option>
                  <option value="dark">Tối</option>
                  <option value="system">Theo hệ thống</option>
                  <option value="professional">Chuyên nghiệp</option>
                  <option value="midnight">Nửa đêm</option>
                </select>
              </div>
              <div class="form-group">
                <label for="font-size">Cỡ chữ: <span id="font-size-value">16px</span></label>
                <input type="range" id="font-size" min="12" max="20" value="16" step="1">
              </div>
              <div class="form-group">
                <label for="density-select">Mật độ hiển thị</label>
                <select id="density-select">
                  <option value="comfortable">Thoải mái</option>
                  <option value="normal">Bình thường</option>
                  <option value="compact">Gọn gàng</option>
                </select>
              </div>
            </div>
          </div>
          
          <div class="settings-section">
            <h2><i class="fas fa-bell"></i> Thông báo</h2>
            <div class="settings-form">
              <div class="form-group checkbox-group">
                <input type="checkbox" id="notify-messages" checked>
                <label for="notify-messages">Thông báo tin nhắn mới</label>
              </div>
              <div class="form-group checkbox-group">
                <input type="checkbox" id="notify-courses" checked>
                <label for="notify-courses">Thông báo khóa học mới</label>
              </div>
              <div class="form-group checkbox-group">
                <input type="checkbox" id="notify-promotions">
                <label for="notify-promotions">Thông báo ưu đãi</label>
              </div>
            </div>
          </div>
          
          <div class="settings-actions">
            <button class="save-btn" onclick="saveSettings()">
              <i class="fas fa-save"></i> Lưu thay đổi
            </button>
            <button class="reset-btn" onclick="resetSettings()">
              <i class="fas fa-undo"></i> Mặc định
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  
  <!-- Modals -->
  <div class="modal" id="profile-modal">
    <div class="modal-content">
      <div class="modal-header">
        <h3>Tài khoản</h3>
        <button class="close-modal" onclick="closeModal('profile-modal')">
          <i class="fas fa-times"></i>
        </button>
      </div>
      <div class="modal-body">
        <div class="profile-avatar-large">
          <i class="fas fa-user" id="modal-avatar-icon"></i>
        </div>
        <div class="profile-info">
          <h4 id="modal-username">Người dùng</h4>
          <p id="modal-email">user@example.com</p>
          <p class="member-since">Thành viên từ: 24/07/2023</p>
        </div>
        <div class="profile-actions">
          <button class="profile-action-btn">
            <i class="fas fa-user-edit"></i> Chỉnh sửa hồ sơ
          </button>
          <button class="profile-action-btn">
            <i class="fas fa-key"></i> Đổi mật khẩu
          </button>
          <button class="profile-action-btn logout-btn">
            <i class="fas fa-sign-out-alt"></i> Đăng xuất
          </button>
        </div>
      </div>
    </div>
  </div>
  
  <div class="modal" id="clear-chat-modal">
    <div class="modal-content small">
      <div class="modal-header">
        <h3>Xác nhận</h3>
        <button class="close-modal" onclick="closeModal('clear-chat-modal')">
          <i class="fas fa-times"></i>
        </button>
      </div>
      <div class="modal-body">
        <p>Bạn có chắc chắn muốn xóa toàn bộ lịch sử trò chuyện?</p>
        <p class="text-muted">Hành động này không thể hoàn tác.</p>
      </div>
      <div class="modal-footer">
        <button class="btn secondary" onclick="closeModal('clear-chat-modal')">Hủy bỏ</button>
        <button class="btn danger" onclick="clearChat()">Xóa tất cả</button>
      </div>
    </div>
  </div>
  

  <!-- Toast notification -->
  <div class="toast" id="toast"></div>
  
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/emoji-picker-element@latest"></script>
  <script src="/static/script.js"></script>
</body>
</html>




# css



:root {
  --primary-color: #4361ee;
  --secondary-color: #3f37c9;
  --accent-color: #4895ef;
  --light-color: #f8f9fa;
  --dark-color: #212529;
  --success-color: #4cc9f0;
  --warning-color: #f8961e;
  --danger-color: #f72585;
  --gray-color: #adb5bd;
  --bg-color: #ffffff;
  --text-color: #212529;
  --card-bg: #ffffff;
  --input-bg: #f8f9fa;
  --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  --border-radius: 12px;
}

[data-theme="dark"] {
  --primary-color: #4895ef;
  --secondary-color: #4361ee;
  --accent-color: #3f37c9;
  --light-color: #343a40;
  --dark-color: #f8f9fa;
  --bg-color: #212529;
  --text-color: #f8f9fa;
  --card-bg: #2b3035;
  --input-bg: #343a40;
  --shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  transition: background-color 0.3s, color 0.3s;
}

body {
  font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: var(--bg-color);
  color: var(--text-color);
  line-height: 1.6;
  min-height: 100vh;
}

.app-container {
  display: flex;
  min-height: 100vh;
}

/* Sidebar styles */
.sidebar {
  width: 280px;
  background-color: var(--card-bg);
  padding: 20px;
  display: flex;
  flex-direction: column;
  border-right: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: var(--shadow);
  z-index: 10;
}

.sidebar-header {
  padding-bottom: 20px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.logo-container {
  display: flex;
  align-items: center;
  gap: 10px;
}

.logo-icon {
  font-size: 1.8rem;
  color: var(--primary-color);
}

.sidebar-header h2 {
  color: var(--text-color);
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 1.5rem;
}

.pro-badge {
  background-color: var(--accent-color);
  color: white;
  padding: 2px 8px;
  border-radius: 10px;
  font-size: 0.8rem;
  margin-left: 5px;
}

.sidebar-subtitle {
  color: var(--gray-color);
  font-size: 0.9rem;
  margin-top: 5px;
}

.sidebar-menu {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 15px;
  border-radius: var(--border-radius);
  background: transparent;
  border: none;
  color: var(--text-color);
  cursor: pointer;
  font-size: 1rem;
  text-align: left;
  transition: all 0.2s;
}

.menu-item:hover {
  background-color: rgba(67, 97, 238, 0.1);
}

.menu-item.active {
  background-color: var(--primary-color);
  color: white;
}

.notification-badge {
  background-color: var(--danger-color);
  color: white;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.7rem;
  margin-left: auto;
}

.sidebar-footer {
  padding-top: 20px;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 12px;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: var(--primary-color);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  transition: transform 0.2s;
}

.avatar:hover {
  transform: scale(1.1);
}

.user-info {
  flex: 1;
}

.username {
  font-weight: 500;
  color: var(--text-color);
  display: block;
}

.user-email {
  font-size: 0.8rem;
  color: var(--gray-color);
  display: block;
}

.profile-btn {
  background: transparent;
  border: none;
  color: var(--text-color);
  cursor: pointer;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
}

.profile-btn:hover {
  background-color: rgba(0, 0, 0, 0.05);
}

/* Main content styles */
.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.content-tab {
  display: none;
  flex: 1;
  padding: 30px;
  flex-direction: column;
  height: 100%;
  overflow-y: auto;
}

.content-tab.active {
  display: flex;
}

/* Chat tab styles */
.chat-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}

.header-left {
  display: flex;
  align-items: center;
  gap: 10px;
}

.chat-header h1 {
  font-size: 1.5rem;
  color: var(--primary-color);
  display: flex;
  align-items: center;
  gap: 10px;
}

.status-indicator {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 0.9rem;
  color: var(--gray-color);
}

.status-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}

.status-dot.online {
  background-color: var(--success-color);
}

.chat-actions {
  display: flex;
  gap: 10px;
}

.action-btn {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: var(--input-bg);
  border: none;
  color: var(--text-color);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.action-btn:hover {
  background-color: var(--primary-color);
  color: white;
}

.search-container {
  display: none;
  gap: 10px;
  margin-bottom: 20px;
  padding: 10px;
  background-color: var(--card-bg);
  border-radius: var(--border-radius);
}

.search-container.active {
  display: flex;
}

#chat-search {
  flex: 1;
  padding: 10px 15px;
  border-radius: 20px;
  border: none;
  background-color: var(--input-bg);
  color: var(--text-color);
}

.search-btn, .close-search-btn {
  background: transparent;
  border: none;
  color: var(--text-color);
  cursor: pointer;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
}

.search-btn:hover, .close-search-btn:hover {
  background-color: rgba(0, 0, 0, 0.05);
}

/* Chat box styles */
.chat-box {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
  background-color: var(--bg-color);
  border-radius: var(--border-radius);
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
  gap: 15px;
  scroll-behavior: smooth;
}

.welcome-message {
  display: flex;
  gap: 15px;
  margin-bottom: 20px;
  padding: 20px;
  background-color: var(--card-bg);
  border-radius: var(--border-radius);
  box-shadow: var(--shadow);
}

.bot-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: var(--primary-color);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  flex-shrink: 0;
}

.bot-avatar.pulse {
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
}

.welcome-content {
  flex: 1;
}

.welcome-content h3 {
  margin-bottom: 10px;
  color: var(--primary-color);
}

.welcome-features {
  list-style: none;
  margin: 15px 0;
}

.welcome-features li {
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.welcome-features i {
  color: var(--success-color);
}

.quick-questions {
  margin-top: 20px;
}

.quick-title {
  font-size: 0.9rem;
  color: var(--gray-color);
  margin-bottom: 10px;
}

.quick-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
}

.quick-btn {
  padding: 10px;
  background-color: var(--input-bg);
  border: none;
  border-radius: var(--border-radius);
  color: var(--text-color);
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 8px;
  justify-content: center;
}

.quick-btn:hover {
  background-color: var(--primary-color);
  color: white;
  transform: scale(1.03);
}

/* Message styles */
.message {
  display: flex;
  gap: 12px;
  max-width: 80%;
  animation: fadeIn 0.3s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.message-user {
  align-self: flex-end;
  flex-direction: row-reverse;
}

.message-bot {
  align-self: flex-start;
}

.message-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: var(--primary-color);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  flex-shrink: 0;
}

.message-bot .message-avatar {
  background-color: var(--accent-color);
}

.message-content {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.message-text {
  padding: 12px 15px;
  border-radius: 18px;
  line-height: 1.5;
  word-wrap: break-word;
  max-width: 100%;
}

.message-user .message-text {
  background-color: var(--primary-color);
  color: white;
  border-bottom-right-radius: 4px;
}

.message-bot .message-text {
  background-color: var(--input-bg);
  color: var(--text-color);
  border-bottom-left-radius: 4px;
}

.message-time {
  font-size: 0.75rem;
  color: var(--gray-color);
  padding: 0 5px;
}

.message-error .message-text {
  background-color: var(--danger-color);
  color: white;
}

/* Input area styles */
.input-container {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 15px;
  background-color: var(--card-bg);
  border-radius: var(--border-radius);
  box-shadow: var(--shadow);
  position: relative;
}

.input-tools {
  display: flex;
  gap: 5px;
}

.tool-btn {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: transparent;
  border: none;
  color: var(--text-color);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  transition: all 0.2s;
}

.tool-btn:hover {
  background-color: rgba(67, 97, 238, 0.1);
  color: var(--primary-color);
}

.input-wrapper {
  display: flex;
  gap: 10px;
}

#user-input {
  flex: 1;
  padding: 12px 15px;
  border-radius: 20px;
  border: none;
  background-color: var(--input-bg);
  color: var(--text-color);
  font-size: 1rem;
  outline: none;
}

#user-input::placeholder {
  color: var(--gray-color);
}

.send-btn {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: var(--primary-color);
  border: none;
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  transition: all 0.2s;
}

.send-btn:hover {
  background-color: var(--secondary-color);
  transform: scale(1.05);
}

.emoji-picker {
  position: absolute;
  bottom: 80px;
  right: 30px;
  z-index: 100;
  display: none;
}

.emoji-picker.active {
  display: block;
}

/* Courses tab styles */
.courses-header {
  margin-bottom: 20px;
}

.courses-header h1 {
  font-size: 1.5rem;
  color: var(--primary-color);
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 15px;
}

.courses-filter {
  display: flex;
  gap: 15px;
}

#course-category {
  padding: 10px 15px;
  border-radius: var(--border-radius);
  border: none;
  background-color: var(--input-bg);
  color: var(--text-color);
  min-width: 200px;
}

.search-box {
  flex: 1;
  display: flex;
  background-color: var(--input-bg);
  border-radius: var(--border-radius);
  overflow: hidden;
}

#course-search {
  flex: 1;
  padding: 10px 15px;
  border: none;
  background: transparent;
  color: var(--text-color);
}

.search-box button {
  background: transparent;
  border: none;
  padding: 0 15px;
  color: var(--text-color);
  cursor: pointer;
}

.courses-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.course-card {
  background-color: var(--card-bg);
  border-radius: var(--border-radius);
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: transform 0.3s, box-shadow 0.3s;
}

.course-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.course-image {
  height: 160px;
  background-color: var(--primary-color);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 2rem;
}

.course-info {
  padding: 20px;
}

.course-title {
  font-size: 1.2rem;
  margin-bottom: 10px;
  color: var(--primary-color);
}

.course-desc {
  color: var(--gray-color);
  font-size: 0.9rem;
  margin-bottom: 15px;
}

.course-meta {
  display: flex;
  justify-content: space-between;
  font-size: 0.9rem;
}

.course-price {
  font-weight: bold;
  color: var(--success-color);
}

.course-rating {
  color: var(--warning-color);
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 15px;
  margin-top: 30px;
}

.page-btn {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: var(--input-bg);
  border: none;
  color: var(--text-color);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.page-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.page-btn:hover:not(:disabled) {
  background-color: var(--primary-color);
  color: white;
}

.page-info {
  font-size: 0.9rem;
  color: var(--gray-color);
}

/* Resources tab styles */
.resources-container {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.resource-category {
  background-color: var(--card-bg);
  border-radius: var(--border-radius);
  padding: 20px;
  box-shadow: var(--shadow);
}

.resource-category h2 {
  font-size: 1.3rem;
  margin-bottom: 15px;
  color: var(--primary-color);
  display: flex;
  align-items: center;
  gap: 10px;
}

.resource-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 15px;
}

.resource-item {
  background-color: var(--input-bg);
  border-radius: var(--border-radius);
  padding: 15px;
  transition: transform 0.2s;
}

.resource-item:hover {
  transform: translateY(-3px);
}

.resource-item h3 {
  font-size: 1rem;
  margin-bottom: 5px;
  color: var(--text-color);
}

.resource-item p {
  font-size: 0.8rem;
  color: var(--gray-color);
}

/* Progress tab styles */
.progress-container {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.progress-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 15px;
}

.stat-card {
  background-color: var(--card-bg);
  border-radius: var(--border-radius);
  padding: 20px;
  display: flex;
  align-items: center;
  gap: 15px;
  box-shadow: var(--shadow);
}

.stat-icon {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.3rem;
  color: white;
}

.stat-icon.blue {
  background-color: var(--primary-color);
}

.stat-icon.green {
  background-color: var(--success-color);
}

.stat-icon.orange {
  background-color: var(--warning-color);
}

.stat-info h3 {
  font-size: 1.5rem;
  margin-bottom: 5px;
}

.stat-info p {
  font-size: 0.9rem;
  color: var(--gray-color);
}

.progress-charts {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 20px;
}

.chart-container {
  background-color: var(--card-bg);
  border-radius: var(--border-radius);
  padding: 20px;
  box-shadow: var(--shadow);
}

.chart-container h3 {
  margin-bottom: 15px;
  font-size: 1.1rem;
  color: var(--primary-color);
}

.chart {
  height: 250px;
  position: relative;
}

.recent-activity {
  background-color: var(--card-bg);
  border-radius: var(--border-radius);
  padding: 20px;
  box-shadow: var(--shadow);
}

.activity-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 15px;
}

.activity-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px;
  border-radius: 8px;
  transition: background-color 0.2s;
}

.activity-item:hover {
  background-color: var(--input-bg);
}

.activity-icon {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: rgba(67, 97, 238, 0.1);
  color: var(--primary-color);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
}

.activity-content {
  flex: 1;
}

.activity-title {
  font-size: 0.9rem;
  margin-bottom: 2px;
}

.activity-time {
  font-size: 0.7rem;
  color: var(--gray-color);
}

/* Settings tab styles */
.settings-container {
  max-width: 800px;
}

.settings-section {
  background-color: var(--card-bg);
  border-radius: var(--border-radius);
  padding: 25px;
  margin-bottom: 20px;
  box-shadow: var(--shadow);
}

.settings-section h2 {
  font-size: 1.3rem;
  margin-bottom: 20px;
  color: var(--primary-color);
  display: flex;
  align-items: center;
  gap: 10px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
}

.form-group input[type="text"],
.form-group input[type="email"],
.form-group select {
  width: 100%;
  padding: 12px 15px;
  border-radius: var(--border-radius);
  background-color: var(--input-bg);
  border: none;
  color: var(--text-color);
  font-size: 1rem;
}

.form-group input[type="range"] {
  width: 100%;
}

#font-size-value {
  color: var(--primary-color);
  font-weight: 500;
}

.avatar-options {
  display: flex;
  gap: 15px;
  margin-top: 10px;
}

.avatar-option {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: var(--input-bg);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  cursor: pointer;
  transition: all 0.2s;
}

.avatar-option.selected {
  background-color: var(--primary-color);
  color: white;
  transform: scale(1.1);
}

.avatar-option:hover {
  transform: scale(1.1);
}

.checkbox-group {
  display: flex;
  align-items: center;
  gap: 10px;
}

.checkbox-group input {
  width: 18px;
  height: 18px;
}

.settings-actions {
  display: flex;
  gap: 15px;
  margin-top: 30px;
}

.save-btn, .reset-btn {
  padding: 12px 25px;
  border-radius: var(--border-radius);
  border: none;
  cursor: pointer;
  font-size: 1rem;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 8px;
}

.save-btn {
  background-color: var(--primary-color);
  color: white;
}

.save-btn:hover {
  background-color: var(--secondary-color);
}

.reset-btn {
  background-color: var(--input-bg);
  color: var(--text-color);
}

.reset-btn:hover {
  background-color: var(--gray-color);
  color: white;
}

/* Modal styles */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s;
}

.modal.active {
  opacity: 1;
  visibility: visible;
}

.modal-content {
  background-color: var(--card-bg);
  border-radius: var(--border-radius);
  width: 90%;
  max-width: 500px;
  box-shadow: var(--shadow);
  transform: translateY(-20px);
  transition: transform 0.3s;
}

.modal.active .modal-content {
  transform: translateY(0);
}

.modal-header {
  padding: 20px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-header h3 {
  font-size: 1.3rem;
  color: var(--primary-color);
}

.close-modal {
  background: transparent;
  border: none;
  color: var(--text-color);
  font-size: 1.3rem;
  cursor: pointer;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
}

.close-modal:hover {
  background-color: rgba(0, 0, 0, 0.05);
}

.modal-body {
  padding: 20px;
}

.modal-footer {
  padding: 15px 20px;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

.btn {
  padding: 10px 20px;
  border-radius: var(--border-radius);
  border: none;
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.2s;
}

.btn.secondary {
  background-color: var(--input-bg);
  color: var(--text-color);
}

.btn.secondary:hover {
  background-color: var(--gray-color);
  color: white;
}

.btn.danger {
  background-color: var(--danger-color);
  color: white;
}

.btn.danger:hover {
  background-color: #d31665;
}

.modal-content.small {
  max-width: 400px;
}

.profile-avatar-large {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background-color: var(--primary-color);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  margin: 0 auto 15px;
}

.profile-info {
  text-align: center;
  margin-bottom: 20px;
}

.profile-info h4 {
  font-size: 1.3rem;
  margin-bottom: 5px;
}

.profile-info p {
  color: var(--gray-color);
}

.member-since {
  font-size: 0.8rem;
  color: var(--gray-color);
  margin-top: 5px;
}

.profile-actions {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.profile-action-btn {
  padding: 12px;
  border-radius: var(--border-radius);
  border: none;
  background-color: var(--input-bg);
  color: var(--text-color);
  cursor: pointer;
  text-align: left;
  display: flex;
  align-items: center;
  gap: 10px;
  transition: all 0.2s;
}

.profile-action-btn:hover {
  background-color: var(--primary-color);
  color: white;
}

.logout-btn {
  background-color: rgba(247, 37, 133, 0.1);
  color: var(--danger-color);
}

.logout-btn:hover {
  background-color: var(--danger-color);
  color: white;
}

.text-muted {
  color: var(--gray-color);
  font-size: 0.9rem;
}

/* Hiệu ứng dấu ba chấm nhún nhảy khi bot đang suy nghĩ */
.typing-indicator {
  display: inline-flex;
  gap: 4px;
  padding-left: 8px;
}

.typing-indicator span {
  display: inline-block;
  font-size: 24px;
  line-height: 1;
  animation: bounce 1s infinite ease-in-out;
}

.typing-indicator span:nth-child(2) {
  animation-delay: 0.2s;
}

.typing-indicator span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-6px);
  }
}




/* Toast notification */
.toast {
  position: fixed;
  bottom: 20px;
  right: 20px;
  padding: 15px 25px;
  background-color: var(--card-bg);
  color: var(--text-color);
  border-radius: var(--border-radius);
  box-shadow: var(--shadow);
  transform: translateY(100px);
  opacity: 0;
  transition: all 0.3s;
  z-index: 1000;
  max-width: 300px;
}

.toast.show {
  transform: translateY(0);
  opacity: 1;
}

/* Scrollbar styles */
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: var(--input-bg);
  border-radius: 10px;
}

::-webkit-scrollbar-thumb {
  background: var(--primary-color);
  border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
  background: var(--secondary-color);
}

/* Responsive styles */
@media (max-width: 768px) {
  .app-container {
    flex-direction: column;
  }
  
  .sidebar {
    width: 100%;
    flex-direction: row;
    padding: 10px;
    align-items: center;
  }
  
  .sidebar-header, 
  .sidebar-footer {
    display: none;
  }
  
  .sidebar-menu {
    flex-direction: row;
    flex: 1;
    justify-content: space-around;
  }
  
  .menu-item {
    flex-direction: column;
    padding: 8px;
    font-size: 0.8rem;
    gap: 5px;
  }
  
  .menu-item i {
    font-size: 1.2rem;
  }
  
  .content-tab {
    padding: 15px;
  }
  
  .courses-grid {
    grid-template-columns: 1fr;
  }
  
  .progress-charts {
    grid-template-columns: 1fr;
  }
  
  .courses-filter {
    flex-direction: column;
  }
  
  #course-category {
    width: 100%;
  }
  
  .quick-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .input-wrapper {
    flex-direction: column;
  }
  
  .send-btn {
    width: 100%;
    border-radius: var(--border-radius);
    height: auto;
    padding: 12px;
  }
  
  .stat-card {
    flex-direction: column;
    text-align: center;
  }
  
  .settings-actions {
    flex-direction: column;
  }
  
  .save-btn, .reset-btn {
    width: 100%;
    justify-content: center;
  }
}
.message-text ul {
  margin: 0;
  padding-left: 20px;
}

.message-text li {
  margin-bottom: 5px;
}

.message-text strong {
  font-weight: bold;
}

.message-text em {
  font-style: italic;
}
.message-bot ol {
  padding-left: 20px;
  margin: 8px 0;
}

.message-bot li {
  margin-bottom: 6px;
  list-style-position: inside; /* hoặc outside nếu bạn muốn canh ngoài */
}


# js
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

