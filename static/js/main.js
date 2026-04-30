document.addEventListener('DOMContentLoaded', () => {
    // Only run this logic if we are on the chat page
    const messageForm = document.getElementById('message-form');
    if (!messageForm) return;

    const socket = io();
    const messageInput = document.getElementById('message-input');
    const chatMessages = document.getElementById('chat-messages');
    const membersCount = document.getElementById('members-count');

    // Auto-scroll to bottom
    const scrollToBottom = () => {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    };

    // Listen for incoming messages
    socket.on('message', (data) => {
        const { name, message, timestamp } = data;
        
        const wrapper = document.createElement('div');
        wrapper.classList.add('message-wrapper');
        
        if (name === 'System') {
            wrapper.classList.add('system');
            wrapper.innerHTML = `<div class="message-bubble">${message}</div>`;
        } else {
            if (name === currentUser) {
                wrapper.classList.add('self');
            } else {
                wrapper.classList.add('other');
            }
            
            wrapper.innerHTML = `
                <div class="message-info">
                    <span class="sender-name">${name}</span>
                    <span class="timestamp">${timestamp}</span>
                </div>
                <div class="message-bubble">${message}</div>
            `;
        }

        chatMessages.appendChild(wrapper);
        scrollToBottom();
    });

    // Listen for room info updates (e.g. member count)
    socket.on('room_info', (data) => {
        if (membersCount) {
            membersCount.textContent = data.members;
        }
    });

    // Handle sending messages
    messageForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const msg = messageInput.value.trim();
        
        if (msg) {
            socket.emit('message', { data: msg });
            messageInput.value = '';
        }
    });

    // Mobile slide menu logic
    const menuToggle = document.getElementById('menu-toggle');
    const sidebar = document.getElementById('chat-sidebar');
    const overlay = document.getElementById('sidebar-overlay');

    if (menuToggle && sidebar && overlay) {
        menuToggle.addEventListener('click', () => {
            sidebar.classList.add('active');
            overlay.classList.add('active');
        });

        overlay.addEventListener('click', () => {
            sidebar.classList.remove('active');
            overlay.classList.remove('active');
        });
    }
});
