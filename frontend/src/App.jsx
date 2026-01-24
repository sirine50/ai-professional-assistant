import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const API_BASE = "http://localhost:8000";

export default function App() {
  const [view, setView] = useState('login');
  const [user, setUser] = useState({ id: null, username: '' });
  const [formData, setFormData] = useState({ username: '', password: '' });
  const [chatMessage, setChatMessage] = useState('');
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    if (view === 'chat' && user.username) {
      axios.get(`${API_BASE}/history/${user.username}`)
        .then(res => setMessages(res.data))
        .catch(err => console.error("History error:", err));
    }
  }, [view, user.username]);

  const handleInputChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleRegister = async () => {
    try {
      const res = await axios.post(`${API_BASE}/register`, formData);
      if (res.data.message === "username already exists") {
        alert("Username taken!");
      } else {
        setUser({ id: res.data.user_id, username: res.data.username });
        setView('chat');
      }
    } catch (err) { alert("Registration failed"); }
  };

  const handleLogin = async () => {
    try {
      const res = await axios.post(`${API_BASE}/login`, formData);
      setUser({ id: res.data.user_id, username: res.data.username });
      setView('chat');
    } catch (err) { alert("Login failed"); }
  };

  const handleUpdate = async () => {
    try {
      const res = await axios.put(`${API_BASE}/update/${user.id}`, formData);
      if (res.data.message === "username already exists") {
        alert("Username taken!");
      } else {
        setUser({ id: res.data.user_id, username: res.data.username });
        alert("Updated!");
        setView('chat');
      }
    } catch (err) { alert("Update failed"); }
  };

  const sendToAI = async () => {
    if (!chatMessage || !user.id) return;
    const currentMsg = chatMessage;
    setMessages(prev => [...prev, { role: 'user', content: currentMsg }]);
    setChatMessage('');

    try {
      const res = await axios.post(`${API_BASE}/ai/ask/${user.id}`, { question: currentMsg });
      setMessages(prev => [...prev, { role: 'ai', content: res.data.answer }]);
    } catch (err) { console.error("AI Error:", err); }
  };

  return (
    <div className="app-shell">
      {(view === 'login' || view === 'register' || view === 'settings') && (
        <div className="auth-overlay">
          <div className="glass-panel animate-up">
            <h1 className="brand-title">AI.ASSISTANT</h1>
            {view === 'login' && (
              <div className="view-content">
                <h2>Login</h2>
                <form onSubmit={(e) => { e.preventDefault(); handleLogin(); }} className="stack">
                  <input name="username" type="text" placeholder="Username" className="ui-input" onChange={handleInputChange} />
                  <input name="password" type="password" placeholder="Password" className="ui-input" onChange={handleInputChange} />
                  <button className="ui-button primary" onClick={handleLogin}>Access Terminal</button>
                </form>
                <p className="toggle-text">New? <span className="link-underline" onClick={() => setView('register')}>Create Account</span></p>
              </div>
            )}
            {view === 'register' && (
              <div className="view-content">
                <h2>Register</h2>
                <form onSubmit={(e) => { e.preventDefault(); handleRegister(); }} className="stack">
                  <input name="username" type="text" placeholder="Choose Username" className="ui-input" onChange={handleInputChange} />
                  <input name="password" type="password" placeholder="Choose Password" className="ui-input" onChange={handleInputChange} />
                  <button className="ui-button success" onClick={handleRegister}>Initialize Identity</button>
                </form>
                <p className="toggle-text">Back to <span className="link-underline" onClick={() => setView('login')}>Login</span></p>
              </div>
            )}
            {view === 'settings' && (
              <div className="view-content">
                <h2>Settings</h2>
                <form onSubmit={(e) => { e.preventDefault(); handleUpdate(); }} className="stack">
                  <input name="username" type="text" placeholder="New Username" className="ui-input" onChange={handleInputChange} />
                  <input name="password" type="password" placeholder="New Password" className="ui-input" onChange={handleInputChange} />
                  <button className="ui-button primary" onClick={handleUpdate}>Save Changes</button>
                </form>
                <button className="ui-button ghost" onClick={() => setView('chat')}>Cancel</button>
              </div>
            )}
          </div>
        </div>
      )}

      {view === 'chat' && (
        <div className="dashboard animate-fade">
          <aside className="sidebar">
            <div className="sidebar-header">AI.PRO</div>
            <nav className="sidebar-nav">
              <button className="nav-item active">Chat Session</button>
              <button className="nav-item" onClick={() => setView('settings')}>Settings</button>
            </nav>
            <button className="logout-btn" onClick={() => setView('login')}>Sign Out</button>
          </aside>
          <main className="chat-area">
            <header className="chat-top-bar"><div className="user-badge">{user.username}</div></header>
            <div className="message-list">
              {messages.map((m, i) => (
                <div key={i} className={`msg ${m.role === 'user' ? 'user' : 'bot'}`}>{m.content}</div>
              ))}
            </div>
            <div className="chat-input-row">
              <input value={chatMessage} onChange={(e) => setChatMessage(e.target.value)} onKeyDown={(e) => e.key === 'Enter' && sendToAI()} type="text" placeholder="Message the AI..." className="ui-input chat-box" />
              <button className="ui-button primary send-btn" onClick={sendToAI}>Send</button>
            </div>
          </main>
        </div>
      )}
    </div>
  );
}